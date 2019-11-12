# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jingdong.items import JingdongItem
import urllib.request
import re
from scrapy.http import Request




class JingdongproductSpider(CrawlSpider):
    name = 'jingdongProduct'
    allowed_domains = ['jd.com']
    # start_urls = ['http://jd.com/']
    def start_requests(self):
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        yield Request("http://jd.com/",headers=header)
    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = JingdongItem()
        thisUrl = response.url
        print("爬取地址："+thisUrl)
        urlPat = "item.jd.com/(.*?).html"
        x = re.search(urlPat,thisUrl)
        if x:
            pid = re.compile(urlPat).findall(thisUrl)[0]
            '''
                productName = scrapy.Field()
                price = scrapy.Field()
                pid = scrapy.Field()
                weight = scrapy.Field()
                shop = scrapy.Field()
                commentNum = scrapy.Field()
                goodCommentNum = scrapy.Field()
            '''
            # 商品id
            item["pid"] = pid
            # 商品名称
            productNamePat = "商品名称：(*.?)</li>"
            item["productName"] = response.xpath("//html/head/title/text()").extract()
            # 商品价格
            priceUrl = "https://p.3.cn/prices/mgets?type=1&skuIds="+pid+"&callback=jQuery4789589&_=1568120643749"
            priceData = urllib.request.urlopen(priceUrl).read().decode("utf-8","ignore")
            pricePat = '"p":"(.*?)"'
            item["price"] = re.compile(pricePat).findall(priceData)
            # 店铺
            item["shop"] = response.xpath('//div[@class="name"]/a/text()').extract()
            # 评论数
            commentUrl = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds='+pid+'&callback=jQuery9309431&_=1568120057650'
            commentPat = '"CommentCountStr":"(.*?)"'
            commentData = urllib.request.urlopen(commentUrl).read().decode("utf-8","ignore")
            item["commentNum"] = re.compile(commentPat).findall(commentData)
            goodcommentPat = '"GoodRateShow":(.*?),'
            goodcommentData = urllib.request.urlopen(commentUrl).read().decode("utf-8","ignore")
            item["goodCommentNum"] = re.compile(goodcommentPat).findall(goodcommentData)
            print("商品名称"+item["productName"][0])
            print("商品价格"+item["price"][0])
            print("商品id"+item["pid"][0])
            print("店铺名称"+item["shop"][0])
            print("评论数"+item["commentNum"][0])
            print("好评"+item["goodCommentNum"][0])
        else:
            pass

