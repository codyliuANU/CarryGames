import random
import string
import datetime
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from authentication.models import Account
from tournament.models import Tournament, Attendant, Match


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class TournamentTestCase(APITestCase):
    players = 21

    @classmethod
    def setUpClass(cls):
        super(TournamentTestCase, cls).setUpClass()

        Account.objects.create(id=37, battle_tag='ADMIN', account_id='99999')
        for i in range(0, cls.players):
            Account.objects.create_user(id_generator(), random.randint(100000, 999999))
        cls.new_tour = Tournament.create('All', 'Semi', 'Finals', fare=10, name='Name', maxplayers=12, rules='Rules',
                                         date='2015-01-01', format='SE',
                                         time='15:00', account=Account.objects.last(), background='', region='Europe')
        cls.client = APIClient()

        accounts = Account.objects.all()
        for acc in accounts:
            new_attendant = Attendant(account=acc, tournament=cls.new_tour, gameClass='rus.png')
            new_attendant.save()


    def test_can_create_tournament(self):
        self.assertEqual(self.new_tour.allmatches, 'All')
        self.assertEqual(self.new_tour.semi, 'Semi')
        self.assertEqual(self.new_tour.finals, 'Finals')
        self.assertEqual(self.new_tour.fare, 10)
        self.assertEqual(self.new_tour.name, 'Name')
        self.assertEqual(self.new_tour.maxplayers, 12)
        self.assertEqual(self.new_tour.rules, 'Rules')
        self.assertEqual(self.new_tour.date, '2015-01-01')
        self.assertEqual(self.new_tour.time, '15:00')
        self.assertEqual(self.new_tour.t_data.type, 'SE')
        self.assertEqual(self.new_tour.account, Account.objects.last())
        self.assertEqual(self.new_tour.background, '')
        self.assertEqual(self.new_tour.region, 'Europe')

    def test_players_can_participate_in_tournament(self):
        accounts = Account.objects.all()
        self.assertEqual(self.new_tour.attendant_set.all().count(), accounts.count())

    def test_generating_tournament(self):
        self.assertGreater(self.new_tour.attendant_set.all().count(), 0)
        self.new_tour.generate(False)
        if Attendant.objects.all().count() < 3:
            self.assertEqual(self.new_tour.t_data.properties.status, 'Canceled')
        else:
            self.assertEqual(self.new_tour.t_data.properties.status, 'In progress')
            self.assertEqual(
                Match.objects.filter(round__conference__tournamentData__tournament=self.new_tour).all().count(),
                Attendant.objects.all().count() - 1)

