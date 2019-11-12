# -*- coding: utf-8 -*-
import scrapy
from scrpayReptile.items import ScrpayreptileItem
from scrapy.http import Request

class QsbkbasicSpider(scrapy.Spider):
    name = 'qsbkbasic'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['http://qiushibaike.com/']
    # def start_requests(self):
    #     header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    #     yield Request("http://qiushibaike.com/",header=header)
    def start_requests(self):
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        yield Request("http://qiushibaike.com/",headers=header)
    def parse(self, response):
        item = ScrpayreptileItem()
        item["content"] = response.xpath('//div[@class="content"]/span/text()').extract()
        # class="contentHerf"
        item["link"] = response.xpath('//a[@class="contentHerf"]/@href').extract()
        yield item
