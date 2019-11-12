import pandas
import numpy
import matplotlib.pylab
import pymysql
conn = pymysql.connect('127.0.0.1','root','root','pythontestdb')
sql = "select  id,productName,floor(price) as price,shopPrice,content,press,commentCount,imageUrl from book"
dbData = pandas.read_sql(sql,conn)
print(dbData.describe())
bookData = dbData.T
price =bookData.values[2]
comment = bookData.values[6]
matplotlib.pylab.plot(price,comment,"om")
matplotlib.pylab.show()
# 价格>600，评论大于>2000为异常数据
exceptionData = dbData.values
line = len(exceptionData)
row = len(exceptionData[0])
num = 0
for i in range(0,line):
    for j in range(0,row):
        if(exceptionData[i][2]>100):
            print(exceptionData[i][j])
            exceptionData[i][j] = 64
        if(exceptionData[i][6]>400):
            print(exceptionData[i][j])
            exceptionData[i][j] = 17
        num+=1

afterData = exceptionData.T
afterPrice = afterData[2]
afterCommentNum = afterData[6]
matplotlib.pylab.plot(afterPrice,afterCommentNum,"o")
matplotlib.pylab.show()

# 绘制价格的直方图
#极差
priceMin = afterData[2].min()
priceMax = afterData[2].max()
pricejc = priceMax - priceMin
priceData = afterData[2]
# 组距
pricezj = pricejc/12
pricesty = matplotlib.pylab.arange(afterData[2].min(),afterData[6].max(),pricezj)
matplotlib.pylab.hist(priceData,pricesty)
matplotlib.pylab.show()

#绘制评论的直方图
#极差
commentMin = afterData[6].min()
commentMax = afterData[6].max()
commentjc = commentMax - commentMin
commentData = afterData[6]
# 组距
commentzj = commentjc/12
commentsty = matplotlib.pylab.arange(commentMin,commentMax,commentzj)
matplotlib.pylab.hist(commentData,commentsty)
matplotlib.pylab.show()