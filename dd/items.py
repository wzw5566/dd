# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

     title = scrapy.Field()
     link = scrapy.Field()
     now_price = scrapy.Field()
     comment_num = scrapy.Field()
     detail = scrapy.Field()
