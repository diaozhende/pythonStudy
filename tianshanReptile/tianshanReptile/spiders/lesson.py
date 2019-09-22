# -*- coding: utf-8 -*-
import scrapy
from tianshanReptile.items import TianshanreptileItem
from scrapy.http import Request

class LessonSpider(scrapy.Spider):
    name = 'lesson'
    allowed_domains = ['hellobi.com']
    start_urls = ['https://edu.hellobi.com/course/1']

    def parse(self, response):
        item = TianshanreptileItem()
        # < div
        # class ="course-info" >
        # < h1 > Hellobi
        # Live | PySpark搭建金融实时数据挖掘系统 < / h1 >
        item["title"]=response.xpath('//div[@class="course-info"]/h1/text()').extract()
        '''
         <ul class="nav nav-tabs" role="tablist">
            <li role="presentation" class="active"><a href="https://edu.hellobi.com/course/311/overview">课程概览</a></li>
        '''
        item["link"]=response.xpath('//ul[@class="nav nav-tabs"]/li[@class="active"]/a/@href').extract()
        '''
            <span class="course-view">609 人学习</span>
        '''
        item["studentNum"]=response.xpath('//span[@class="course-view"]/text()').extract()
        yield item
        for i in range(1,11):
            url = "https://edu.hellobi.com/course/"+str(i)
            yield Request(url,callback=self.parse)