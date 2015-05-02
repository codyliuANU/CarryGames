from django.core.management.base import BaseCommand, CommandError
from tournament.models import Tournament
from datetime import date, datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Starting")
        # try:
        tournaments = Tournament.objects.filter(t_data__properties__status="Not started")
        i = 0
        for t in tournaments:
            if (t.date and t.time) is not None:
                date_object = datetime.strptime(str(t.date) + " " + str(t.time), '%Y-%m-%d %H:%M:%S')
                if date_object <= datetime.now():
                    self.stdout.write(
                        "CALL GENERATE FOR: " + str(t.id) + " tournament (starts on: " + str(
                            date_object) + " attendants: " + str(t.attendant_set.all().__len__()) + ")")
                    self.stdout.write(t.generate(False)) #TODO: Play-bronze param is hardcoded. Have to add the param to tournament creating form.
                    i += 1
        self.stdout.write(str(i) + "/" + str(tournaments.__len__()) + " tournaments started at " + str(datetime.now()))
        # except Exception:
        # raise CommandError('Something bad happened in a tournamentstart command :(')