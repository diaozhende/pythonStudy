# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrpayReptile.items import ScrpayreptileItem
from scrapy.http import Request

class QsbkcrawlSpider(CrawlSpider):
    name = 'qsbkCrawl'
    allowed_domains = ['qiushibaike.com/']
    # start_urls = ['http://qiushibaike.com/']
    def start_requests(self):
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        yield Request("http://qiushibaike.com/",headers=header)
    rules = (
        Rule(LinkExtractor(allow='article'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ScrpayreptileItem()
        # <div class="content">
        item["content"] = response.xpath('//div[@class="content"]/text()').extract()
        # <link rel="canonical" href="//www.qiushibaike.com/article/122215695"/>
        item["link"] = response.xpath('//link[@rel="canonical"]/@href').extract()
        return item
