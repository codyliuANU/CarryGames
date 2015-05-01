from django.db import models
from authentication.models import Account


class Properties(models.Model):
    status = models.CharField(max_length=20)
    unbalanced = models.CharField(max_length=10, null=True)


class TournamentData(models.Model):
    type = models.CharField(max_length=10)
    properties = models.OneToOneField(Properties)
    # tournament = models.ForeignKey(Tournament)
    # matches: [] (Match)


# Base tournament description
class Tournament(models.Model):
    name = models.CharField(max_length=80)
    allmatches = models.CharField(max_length=3)
    semi = models.CharField(max_length=3)
    finals = models.CharField(max_length=3)
    maxplayers = models.PositiveIntegerField(max_length=3)
    rules = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    fare = models.IntegerField(max_length=4)
    account = models.ForeignKey(Account)
    background = models.ImageField(upload_to='tournaments_background/', null=True)
    region = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    t_data = models.OneToOneField(TournamentData)

    @classmethod
    def create(cls, allmatches='Bo3', semi='Bo3', finals='Bo5', fare=0, **kwargs):
        ac = Account.objects.get(id=kwargs['account'])
        props = Properties(status="Not started")
        props.save()
        tournament_data = TournamentData(type=kwargs['format'], properties=props)
        tournament_data.save()
        tour = cls(name=kwargs['name'],
                   allmatches=allmatches,
                   semi=semi,
                   finals=finals,
                   maxplayers=kwargs['maxplayers'],
                   rules=kwargs['rules'],
                   date=kwargs['date'],
                   time=kwargs['time'],
                   fare=fare,
                   # account=kwargs['account']
                   account=ac,
                   background=kwargs['background'],
                   region=kwargs['region'],
                   t_data=tournament_data
                   )
        tour.save()
        conference = Conference(tournamentData=tournament_data)
        conference.save()
        return tour

    @staticmethod
    def create_match(round_number, match_number, conference):
        meta = Meta(matchId="match-" + conference + '-' + str(round_number) + '-' + str(match_number))
        meta.save()
        contestant1 = Contestant()
        contestant1.save()
        contestant2 = Contestant()
        contestant2.save()
        return Match(meta=meta, contestant1=contestant1, contestant2=contestant2)

    @staticmethod
    def get_even_distribution(round_len, number_of_attendants, promoted_round):
        dist = []
        x = (2 * round_len) - number_of_attendants if promoted_round else number_of_attendants
        step = round_len / (
            abs((2 * round_len) - number_of_attendants)) if promoted_round else round_len / number_of_attendants

        for i in range(0, round_len):
            dist.append(2 if promoted_round else 0)

        for i in range(0, x):
            ind = round(i * step)
            dist[ind] = dist[ind] - 1 if promoted_round else dist[ind] + 1

        return dist

    @staticmethod
    def shift_previous_round(current_round, previous_round):
        x = 0
        for match in list(current_round.matches.all()):
            if match.meta.matchType != 2:
                x += 1 if match.meta.matchType == 1 else 2
        for i, match in enumerate(list(previous_round.matches.all()), start=x):
            match.meta.UIShiftDown = match.meta.UIShiftDown + 1 if match.meta.UIShiftDow else 1

    def generate_round(self, attendants, round_number, conference):
        new_round = Round()
        closest_balance_tree = 1
        balancing_round = None

        if round_number == 1:
            # find the closest balanced tree
            while closest_balance_tree * 2 < attendants.__len__():
                closest_balance_tree *= 2
            # closestBalancedTree / 2 is the target for round 2
            excess_participants = attendants.__len__() - closest_balance_tree

            if excess_participants > 0:
                shifted_matches = excess_participants - (closest_balance_tree / 2)
                start_index = closest_balance_tree if shifted_matches == 0 else (
                    closest_balance_tree + (shifted_matches * 2) if shifted_matches > 0 else closest_balance_tree - (
                        abs(shifted_matches) * 2))
                balancing_round = attendants[start_index:]
                del attendants[start_index:]

        # Loop through teams / previous round matches and create following match
        for index, attendant in enumerate(attendants):
            match = self.create_match(round_number=round_number, match_number=new_round.matches.all().__len__() + 1,
                                      conference=conference)

            if round_number == 1:
                # normal brackets untill reaching biggest possible balanced tree...
                if index % 2 != 0:
                    continue
                # c1 = Contestant(account=attendant.account)
                # c1.save()
                # match.contestant1_id = c1.id
                match.contestant1.account = attendant.account
                match.contestant1.save()
                # c2 = Contestant(account=attendants[index+1].account)
                # c2.save()
                # match.contestant2_id = c2.id
                match.contestant2.account = attendants[index + 1].account
                match.contestant2.save()

            elif index % 2 != 0:
                continue

            new_round.save()
            new_round.matches.add(match)

        dist = None
        if round_number == 1 and balancing_round is not None and balancing_round.__len__() > 0:
            self.tournamentdata_set.last().conferences.last().rounds.add(new_round)

            self.tournamentdata_set.last().properties.unbalanced = True
            self.tournamentdata_set.last().properties.save()
            round_b = Round()
            # Round 1 and Round 2 are equally long --> have to balance every match.
            if shifted_matches == 0:
                for bal_round in balancing_round:
                    match = self.create_match(round_number=round_number + 1,
                                              match_number=round_b.matches.all().__len__() + 1, conference=conference)
                    # c1 = Contestant(account=bal_round.account)
                    # c1.save()
                    # match.contestant1_id = c1.id
                    match.contestant1.account = bal_round.account
                    match.contestant1.save()
                    match.meta.matchType = '1'
                    match.meta.save()
                    round_b.save()
                    round_b.matches.add(match)
            elif shifted_matches > 0:
                dist = self.get_even_distribution(closest_balance_tree / 2, balancing_round.__len__(), False)
                p = 0
                for i in range(0, dist.__len__()):
                    match = self.create_match(round_number=round_number + 1,
                                              match_number=round_b.matches.all().__len__() + 1, conference=conference)
                    if dist[i] == 1:
                        # c1 = Contestant(account=balancing_round[p].account)
                        # c1.save()
                        # match.contestant1_id = c1.id
                        match.contestant1.account = balancing_round[p].account
                        match.contestant1.save()
                        match.meta.matchType = '1'
                        match.meta.save()
                        p += 1
                    round_b.save()
                    round_b.matches.add(match)
            elif shifted_matches < 0:
                dist = self.get_even_distribution(closest_balance_tree / 2, balancing_round.__len__(), True)
                j = 0
                for i in range(0, closest_balance_tree / 2):
                    match = self.create_match(round_number=round_number + 1,
                                              match_number=round_b.matches.all().__len__() + 1, conference=conference)
                    # c1 = Contestant(account=balancing_round[j].account)
                    # c1.save()
                    # match.contestant1_id = c1.id
                    match.contestant1.account = balancing_round[j].account
                    match.contestant1.save()
                    match.meta.matchType = '1'
                    match.meta.save()

                    if dist[i] == 2:
                        # c2 = Contestant(account=balancing_round[j+1].account)
                        # c2.save()
                        # match.contestant2_id = c2.id
                        match.contestant2.account = balancing_round[j + 1].account
                        match.contestant2.save()
                        match.meta.matchType = '2'
                        match.meta.save()
                        self.shift_previous_round(round_b, new_round)
                        j += 1
                    j += 1

                    round_b.save()
                    round_b.matches.add(match)

            del attendants
            return round_b

        del attendants
        return new_round

    def create_tournament(self, attendants, play_bronze_match, conference):
        round_number = 1
        previous_round = Round()
        # Create new rounds untill there is only one match, the finals, left.
        while round_number == 1 or previous_round.matches.all().__len__() > 1:
            partic = list(previous_round.matches.all())

            if round_number == 1:
                partic = attendants.copy()

            previous_round = self.generate_round(attendants=partic, round_number=round_number, conference=conference)
            td_conference = self.tournamentdata_set.last().conferences.last()

            td_conference.save()
            td_conference.rounds.add(previous_round)

            round_number = td_conference.rounds.all().__len__() + 1

        rounds = list(self.tournamentdata_set.last().conferences.last().rounds.all())
        meta = rounds[rounds.__len__() - 1].matches.last().meta
        meta.matchType = 'finals'
        meta.save()

        if play_bronze_match:
            bronze_match = self.create_match(rounds.__len__(), rounds[rounds.__len__() - 1].matches.all().__len__() + 1,
                conference)
            bronze_match.meta.matchType = 'bronze'
            bronze_match.meta.save()

            rounds[rounds.__len__() - 1].save()
            rounds[rounds.__len__() - 1].matches.add(bronze_match)

    def generate(self, play_bronze_match):
        attendants = list(self.attendant_set.all())

        if attendants.__len__() < 3:
            return

        self.create_tournament(attendants=attendants, play_bronze_match=play_bronze_match, conference="C1")


class Conference(models.Model):
    tournamentData = models.ForeignKey(TournamentData, related_name='conferences')


class Attendant(models.Model):
    account = models.ForeignKey(Account)
    gameClass = models.CharField(max_length=30)
    tournament = models.ForeignKey(Tournament)


############################################


class Contestant(models.Model):
    account = models.ForeignKey(Account, null=True)
    score = models.CharField(max_length=2, default="")


class Meta(models.Model):
    matchId = models.CharField(max_length=15)
    UIShiftDown = models.PositiveIntegerField(null=True)
    matchType = models.CharField(max_length=10, null=True)


class Round(models.Model):
    conference = models.ForeignKey(Conference, related_name='rounds', null=True)


class Match(models.Model):
    round = models.ForeignKey(Round, related_name='matches', null=True)
    contestant1 = models.OneToOneField(Contestant, related_name='contestant1')
    contestant2 = models.OneToOneField(Contestant, related_name='contestant2')
    meta = models.OneToOneField(Meta, related_name='meta')


class Reporter(models.Model):
    pass


class Article(models.Model):
    text = models.CharField(max_length=10)
    reporter = models.ForeignKey(Reporter, null=True)