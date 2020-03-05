import scrapy
import urllib.request
from zlzp.zlzp.items import ZlzpItem
from scrapy.http import Request

class zlzpSpiders(scrapy.Spider):
    name = 'zlzp'
    allowed_domains = ['zhaopin.com']

    def start_requests(self):
        url = "https://sou.zhaopin.com/?jl=708"
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
        yield Request(url, headers=header)

        def parse(self, response):
            keyName = "软件开发"
            item = ZlzpItem()
            # item["productName"] = response.xpath('//a[@name="itemlist-title"]/@title').extract()
            # item["price"] = response.xpath('//p[@class="price"]/span[@class="search_now_price"]/text()').extract()
            # item["shopPrice"] = response.xpath('//p[@class="price"]/span[@class="search_pre_price"]/text()').extract()
            # item["content"] = response.xpath('//p[@class="detail"]/text()').extract()
            # item["press"] = response.xpath('//a[@name="P_cbs"]/@title').extract()
            # item["commentCount"] = response.xpath('//a[@class="search_comment_num"]/text()').extract()
            # item["imageUrl"] = response.xpath('//a[@class="pic"]/img/@data-original').extract()
            yield item
            for i in range(1, 101):
                url = "http://search.dangdang.com/?key=" + urllib.request.quote(keyName) + "&page_index=" + str(i)
                yield Request(url, callback=self.parse)
    #         http://search.dangdang.com/?key=%C8%ED%BC%FE%BF%AA%B7%A2&page_index=1