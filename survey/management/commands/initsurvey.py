__author__ = 'belendia@gmail.com'

from django.conf import settings
from django.core.management.base import BaseCommand
from survey.models import Survey

class Command(BaseCommand):

    def handle(self, *args, **options):
        if Survey.objects.count() == 0:
            for s in settings.SURVEY:
                survey = Survey(title=s.title, published=s.published, journeys=s.journeys)
                survey.save()
                
                print('%s saved.' % (s.title))
               
        else:
            print('Survey table already initialized')