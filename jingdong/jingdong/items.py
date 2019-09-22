# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    # productName = scrapy.Field()
    # price = scrapy.Field()
    # shop = scrapy.Field()
    # content = scrapy.Field()
    # detailsUrl = scrapy.Field()
    pid = scrapy.Field()
    productName = scrapy.Field()
    price = scrapy.Field()
    pid = scrapy.Field()
    shop = scrapy.Field()
    commentNum = scrapy.Field()
    goodCommentNum = scrapy.Field()