# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Event(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    title = scrapy.Field()
    runtime = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    
    
    pass

class Movie(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    movie_id = scrapy.Field()
    runtime = scrapy.Field()
    director = scrapy.Field()
    stars = scrapy.Field()
    writers = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    
    
    pass

class Celeb(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    name = scrapy.Field()
    desc = scrapy.Field()
    
    image_urls = scrapy.Field()
    images = scrapy.Field()
    
    
    pass
