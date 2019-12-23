from django.core.management.base import BaseCommand, CommandError
from events.models import Event
import json

class Command(BaseCommand):
    
    
    def handle(self, *args, **options):
        
        
        with open('E:/moviews_scrapy/events.json') as f:
            events = json.load(f)
            
            
            for event in events:
                event_object = Event()
                event_object.title = event['title']
                event_object.date = event['date']
                event_object.description = event['description']
                event_object.category = event['category']
                event_object.runtime = event['runtime']
                event_object.image_url = event['images'][0]['path']
                
                event_object.save()
        
        
        self.stdout.write(self.style.SUCCESS('Sucessfully Imported Events'))