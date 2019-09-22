# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from jingdong.items import JingdongItem

class MobilephoneSpider(scrapy.Spider):
    name = 'mobilephone'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    #url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=2&s=61&click=0"

    def start_requests(self):
        header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        url = "https://search.jd.com/Search?keyword=手机&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=2&s=61&click=0"
        yield Request(url,headers=header)

    def parse(self, response):
        # productName = scrapy.Field()
        # price = scrapy.Field()
        # shop = scrapy.Field()
        # content = scrapy.Field()
        # detailsUrl = scrapy.Field()
        item = JingdongItem()
        # item["productName"] = response.xpath('//div[@class="p-name p-name-type-2"]/a/em/text()').extract()
        item["productName"] = response.xpath('//div[@class="p-img"]/a/@title').extract()
        # item["price"] = response.xpath('//strong[@data-done="1"]/i/text()').extract()
        item["price"] = response.xpath('//div[@class="p-price"]/strong/i/text()').extract()
        item["shop"] = response.xpath('//a[@class="curr-shop hd-shopname"]/@href').extract()
        item["content"] = response.xpath('//div[@class="p-img"]/a/@title').extract()
        item["detailsUrl"] = response.xpath('//div[@class="p-img"]/a/@href').extract()
        print(str(len(item["price"])))
        print(str(len(item["shop"])))
        yield item

