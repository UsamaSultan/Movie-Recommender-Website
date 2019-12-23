# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from moviews_scrapy.items import Movie
import mysqlx


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/']
    
    
    def start_requests(self):
        
        session = mysqlx.get_session({
            'host': 'localhost',
            'port': 33060,
            'user': 'root',
            'password': 'abcd123'
        })

        schema = session.get_schema('moviews')

        movies = schema.get_table('movie_data')

        rows = movies.select('title', 'movieId').execute().fetch_all()
        
        for row in rows:
            base_url = 'https://www.imdb.com/find?q='
            title = row['title']
            url = base_url + title
            request = Request(url, self.parse_search)
            request.meta['movie_id'] = row['movieId']
            yield request
        
        
        
            

    def parse(self, response):
        
        
        movieItem = Movie()
        
        movie_id = response.meta['movie_id']
        
        movieItem['movie_id'] = movie_id
        
        
        director = response.xpath('//h4[text()="Director:"]/../a/text()').extract()
        writer = response.xpath('//h4[text()="Writer:"]/../a/text()').extract()
        
        if len(writer)==0:
             writer = response.xpath('//h4[text()="Writers:"]/../a/text()').extract()
        
        stars = response.xpath('//h4[text()="Stars:"]/../a/text()').extract()
        
        title_wrapper = response.xpath("//div[contains(@class,'title_wrapper')]/div[contains(@class,'subtext')]/time/text()").extract()
        
        poster = response.xpath("//div[contains(@class,'poster')]/a/img/@src").extract()
        
        desc = response.xpath("//div[contains(@class,'summary_text')]/text()").extract()
        
        movieItem['description'] = desc
        
        
        movieItem['image_urls'] = poster
        
       
        
        movieItem['runtime'] = title_wrapper
        
        
        movieItem['director'] = director
        
        
        
        
        
        
        if len(writer)==3:
            
            writer.pop(2)
        
        stars.remove("See full cast & crew")
        
        
        movieItem['writers'] = writer
        movieItem['stars'] = stars
        
        
        yield movieItem
        
        
        pass
    
    def parse_search(self, response):
        
        
        url = response.xpath('//td[contains(@class, "result_text")]/a/@href').extract_first()
        request = Request(self.start_urls[0] + url, self.parse)
        request.meta['movie_id'] = response.meta['movie_id']
        yield request
        
        
        
        pass
