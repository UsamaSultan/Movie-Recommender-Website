import scrapy
import re
import bleach
from moviews_scrapy.items import Event






class FathomEventsSpider(scrapy.Spider):
    name = "fathomevents"
    
    

    
    start_urls = [
        'https://www.fathomevents.com/events'
            
    ]
        

    def parse(self, response):
        
        
        
        events = response.css("div.card-event")
        for event in events:
            
            eventItem = Event()
            event_date = event.css("p.date::text")[0].extract()
            event_date2 = re.sub(r'[^a-zA-Z0-9,]', ' ', event_date)
        
            event_text = event.css("h3.card__title::text").extract()
            event_text2 = re.sub(r'[^a-zA-Z0-9]', ' ', event_text[0])
            eventItem['title'] = event_text2
            eventItem['date'] = event_date2.strip()
            
            event_link = event.css("a.card--event::attr(href)")[0].extract()
            event_link = response.urljoin(event_link)
            yield scrapy.Request(event_link, callback=self.parse_event, meta={'event': eventItem})
            
    
    def parse_event(self, response):
        
        event = response.meta['event']
        
    
        event_desc_block = response.css("div.event-detail__synopsis").extract()
        
        event_desc = bleach.clean(event_desc_block[0], tags=['p'], strip="True")
                            
    
        event_runtime = response.css('p.event-detail__runtime::text').extract()
        event['runtime'] = event_runtime[0].strip()
        
        
        category_block = response.css('p.event-detail__category')
        event_category = category_block.css('a::text').extract()
        
        event['category'] = event_category[0]
        
        
        event['description'] = event_desc
        
        
        
        event_image_url = response.css("img.event-detail__img::attr(src)").extract()
        event['image_urls'] = event_image_url
        
        yield event
        
        
        