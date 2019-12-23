# -*- coding: utf-8 -*-
import scrapy
from moviews_scrapy.items import Celeb

class CelebsSpider(scrapy.Spider):
    name = 'celebs'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/name?gender=male,female&ref_=nv_cel_m']
    
    custom_settings = {
                       'CLOSESPIDER_ITEMCOUNT': 9950,
                       
                       }

    def parse(self, response):
        
        
        
        
        list_items = response.css('.lister-item')
        
        for item in list_items:
            
            celebs = Celeb()
            
            name = item.xpath('.//h3[@class="lister-item-header"]/a/text()').extract()
            
            list_image = item.xpath('.//div[@class="lister-item-image"]/a/img/@src').extract()
            
            desc = item.xpath('.//p/node()').extract()
            
            
            
            celebs['name'] = name
            celebs['image_urls'] = list_image
            celebs['desc'] = desc
            
            yield celebs
            
            
        
        
        
       
        next_button = response.css(".lister-page-next::attr(href)").get()
        
        yield scrapy.Request(response.urljoin(next_button), self.parse)
         
            
        
        
        
        pass
