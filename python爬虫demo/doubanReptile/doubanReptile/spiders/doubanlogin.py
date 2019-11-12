# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
import urllib.request


class DoubanloginSpider(scrapy.Spider):
    name = 'doubanlogin'
    allowed_domains = ['doubai.com']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}

    # start_urls = ['http://doubai.com/']
    # def start_requests(self):
    #     return [
    #         Request("https://accounts.douban.com/j/mobile/login/basic", callback=self.parse, meta={"cookiejar":1})]
    #
    # def parse(self, response):
    #     url = "https://accounts.douban.com/j/mobile/login/basic"
    #     # username,password
    #     data = {
    #         "username": "15634122070",
    #         "password": "19970505dzd"
    #     }
    #     print("登陆中。。。")
    #     return [FormRequest.from_response(response,
    #                                       meta={"cookiejar": response.meta["cookiejar"]},
    #                                       headers=self.header,
    #                                       formdata=data,
    #                                       callback=self.nextFunction
    #                                       )]
    # def nextFunction(self,response):
    #     print("登陆成功。。。")

    def start_requests(self):
        return [FormRequest("https://accounts.douban.com/j/mobile/login/basic", callback=self.parse, meta={"cookiejar": 1})]

    def parse(self, response):
        print("此时没有验证码")
        data = {
            # "form_email": "weisuen007@163.com",
            # "form_password": "weijc7789",
            # "redir": "https://www.douban.com/people/151968962/",
            "username": "15634122070",
            "password": "19970505dzd"
        }

        print("登陆中……")
        return [FormRequest.from_response(response,
                                      meta={"cookiejar": response.meta["cookiejar"]},
                                      headers=self.header,
                                      formdata=data,
                                      callback=self.next,
                                      )]

    def next(self, response):
        print(response.status)

