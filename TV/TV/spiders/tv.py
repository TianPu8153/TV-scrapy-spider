# -*- coding: utf-8 -*-
import scrapy
from TV.items import TvItem


class TvSpider(scrapy.Spider):
    name = 'tv'
    
    start_urls = ['http://www.meijutt.com/content/meiju23213.html']

    def parse(self, response):
        item=TvItem()
        item['title']=response.xpath('//h1/text()').extract_first()
        item['url']=response.url

        item['start']=response.xpath('//li[1]/font[1]/text()').extract()
        item['end']=response.xpath('//font[2]/text()').extract()
        yield item
