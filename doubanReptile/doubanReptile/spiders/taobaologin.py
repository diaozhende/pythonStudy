# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest


class TaobaologinSpider(scrapy.Spider):
    name = 'taobaologin'
    allowed_domains = ['taobao.com']
    # start_urls = ['http://taobao.com/']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
    def start_requests(self):
        return [
            Request("https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da21bo.2017.754894437.3.5af911d9ubAiGI%26ad_id%3D%26am_id%3D%26cm_id%3D%26pm_id%3D1501036000a02c5c3739", callback=self.parse, meta={"cookiejar":1})]
    def parse(self, response):
        url = "https://accounts.douban.com/j/mobile/login/basic"
        # username,password
        data = {
            "TPL_username": "追风少年dzf",
            "TPL_password": "19970505dzd"
        }
        print("登陆中。。。")
        return [FormRequest.from_response(response,
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          headers=self.header,
                                          formdata=data,
                                          callback=self.nextFunction
                                          )]
    def nextFunction(self,response):
        print(response.status)
        # <div class="s-name"><a><em>
        username = response.xpath('//div[@class="s-name"]/a/em/text()')
        print(response)