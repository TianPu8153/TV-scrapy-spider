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

        item['start']=response.xpath('//div[@class="o_r_contact"]/ul/li')[0].xpath('//font/text()')[0].extract()
        item['end']=response.xpath('//div[@class="o_r_contact"]/ul/li')[0].xpath('//font/text()')[1].extract()
        yield item