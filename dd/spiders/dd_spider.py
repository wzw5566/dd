# -*- coding: utf-8 -*-
import scrapy
from dd.items import DdItem
from scrapy.http import Request
import re

class DdSpiderSpider(scrapy.Spider):
    name = 'dd_spider'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input&page_index=1']

    def parse(self, response):

        item = DdItem()
        item["title"] = response.xpath("//p[@class='name']/a/@title").extract()
        item["link"] = response.xpath("//p[@class='name']/a/@href").extract()
        item["now_price"] = response.xpath("//p[@class='price']/span[@class='search_now_price']/text()").extract()
        item["comment_num"] = response.xpath("//p/a[@class='search_comment_num']/text()").extract()
        item["detail"] = response.xpath("//p[@class='detail']/text()").extract()
        yield item

        for i in range(2,27):
            url = "http://search.dangdang.com/?key=python&act=input&page_index="+str(i)
            yield Request(url, callback=self.parse)


