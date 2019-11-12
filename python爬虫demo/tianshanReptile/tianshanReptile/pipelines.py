# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TianshanreptilePipeline(object):
    def __init__(self):
        self.file = open("E:/reptileContent/天善智能/lesson.txt","a")
    def process_item(self, item, spider):
        self.file.write(item["title"][0]+"\n")
        self.file.write(item["link"][0]+"\n")
        self.file.write(item["studentNum"][0]+"\n")
        return item
    def close_spider(self):
        print("写入完成！")
        self.file.close()