# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib.request
import uuid
import pymysql


class Book(declarative_base()):
    __tablename__ = "book"
    id = Column(String(100), primary_key=True)
    productName = Column(String(200))
    price = Column(String(20))
    shopPrice = Column(String(20))
    content = Column(String(1000))
    press = Column(String(100))
    commentCount = Column(String(20))
    imageUrl = Column(String(200))


class DangdangPipeline(object):
    def process_item(self, item, spider):
        engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/pythontestdb")
        DBSession = sessionmaker(bind=engine)
        sessio = DBSession()
        print(len(item["shopPrice"]))
        for i in range(0, len(item["productName"])):
            productName = item["productName"][i]
            price = item["price"][i]
            # shopPrice = item["shopPrice"][i]
            shopPrice ="111"
            # content = item["content"][i]
            content = "商品简介"
            press = item["press"][i]
            commentCount = item["commentCount"][i]
            # imageUrl = item["imageUrl"][i]
            imageUrl = "http://img3m6.ddimg.cn/14/29/23920196-1_b_5.jpg"
            imgName = uuid.uuid1()
            file = "E:/reptileContent/dangdangImg/" + str(imgName) + ".jpg"
            imgUrl = "/img/" + str(imgName) + ".jpg"
            urllib.request.urlretrieve(imageUrl, filename=file)
            bookid = str(uuid.uuid1())
            book = Book(id=bookid, productName=productName, price=price, shopPrice=shopPrice, content=content,
                        press=press, commentCount=commentCount, imageUrl=imgUrl)
            sessio.add(book)
            sessio.commit()
        sessio.close()
        return item
