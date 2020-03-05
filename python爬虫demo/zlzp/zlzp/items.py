# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZlzpItem(scrapy.Item):
    name = scrapy.Field() # 岗位名称
    moneyrange = scrapy.Field() # 薪资范围
    address = scrapy.Field() # 地址
    experience = scrapy.Field() # 经验
    education = scrapy.Field() # 学历
    welfare = scrapy.Field() # 福利
