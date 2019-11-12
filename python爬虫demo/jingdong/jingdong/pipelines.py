# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JingdongPipeline(object):
    def process_item(self, item, spider):
        # print(item["shop"])
        # productName = scrapy.Field()
        # price = scrapy.Field()
        # shop = scrapy.Field()
        # content = scrapy.Field()
        # detailsUrl = scrapy.Field()
        # for i in range(0,len(item["productName"])):
        #     print(item["productName"][i])
        #     # print(item["price"][i])
        #     # print(item["shop"][i])
        #     print(item["content"][i])
        #     print(item["detailsUrl"][i])
        '''
            productName = scrapy.Field()
            price = scrapy.Field()
            pid = scrapy.Field()
            weight = scrapy.Field()
            shop = scrapy.Field()
            commentNum = scrapy.Field()
            goodCommentNum = scrapy.Field()
        '''
        return item
