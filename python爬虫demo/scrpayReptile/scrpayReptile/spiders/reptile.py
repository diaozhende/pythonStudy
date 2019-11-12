# -*- coding: utf-8 -*-
import scrapy

from scrpayReptile.items import ScrpayreptileItem


class ReptileSpider(scrapy.Spider):
    name = 'reptile'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        item = ScrpayreptileItem()
        item["content"] = response.xpath("/html/head/title/text()").extract()
        yield item
