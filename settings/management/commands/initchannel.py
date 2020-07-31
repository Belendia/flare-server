__author__ = 'belendia@gmail.com'

from django.conf import settings
from django.core.management.base import BaseCommand
from settings.models import Channel

class Command(BaseCommand):

    def handle(self, *args, **options):
        if Channel.objects.count() == 0:
            for chnl in settings.CHANNEL:
                channel = Channel(name=chnl.name)
                channel.save()
                
                print('%s saved.' % (chnl.name))
               
        else:
            print('Channel table already initialized')