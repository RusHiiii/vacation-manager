from django.core.management.base import BaseCommand, CommandError
from holidays.models import Holiday
from django.contrib.auth.models import User

class Command(BaseCommand):
  help = "Initialize holidays for a specific user"

  def add_arguments(self, parser):
    parser.add_argument("username", type=str)

  def handle(self, *args, **options):
    user = User.objects.filter(username=options['username']).first()

    if user is None:
      raise CommandError('L\'utilisateur "%s" n\'existe pas' % options['username'])

    holidays = Holiday.objects.filter(user=user)

    if holidays.count() > 0:
      raise CommandError('Les mois ont déjà été initilizé pour cette utilisateur')

    # Initilization des mois de congés
    for month_value in range(0, 24):
      holiday = Holiday(month_number=month_value, user=user)
      holiday.save()

    # Initilization des paramètres
    parameter = Parameter(user=user)
    parameter.save()

    self.stdout.write(
        self.style.SUCCESS('Initilization réalisé avec succès : "%s"' % options['username'])
    )