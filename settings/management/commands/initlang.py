__author__ = 'belendia@gmail.com'

from django.conf import settings
from django.core.management.base import BaseCommand
from settings.models import Language

class Command(BaseCommand):

    def handle(self, *args, **options):
        if Language.objects.count() == 0:
            for lang in settings.LANGUAGES:
                language = Language(name=lang.name, code=lang.code)
                language.save()
                
                print('Language name %s saved.' % (lang.name))
               
        else:
            print('Language table already initialized')