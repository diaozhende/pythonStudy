import pandas
import pymysql
import matplotlib.pylab
import numpy
import xlwt

conn = pymysql.connect("127.0.0.1","root","root","pythontestdb")
sql = "select * from myhexun"
hexunDbData = pandas.read_sql(sql,conn)
print(hexunDbData.describe())

# 评点比（评论数/阅读数）
dpData = hexunDbData[u"comment"]/hexunDbData["hits"]
# print(ch)
hexunDbData[u"评点比"] = dpData
file = "E:/python大数据资料/Python3数据分析与挖掘实战/源码/第6周/myhexun.xls"
hexunDbData.to_excel(file,index=False)