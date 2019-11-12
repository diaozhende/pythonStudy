import pandas
import pymysql
import matplotlib.pylab
import numpy

# 读取数据
conn = pymysql.connect("127.0.0.1","root","root","pythontestdb")
sql = "select * from taob"
dbData = pandas.read_sql(sql,conn)
print(dbData.describe())
dbData["price"][(dbData["price"]==0)]=None
x = 0
for i in dbData.columns:
    for j in range(len(dbData)):
        if(dbData[i].isnull())[j]:
            dbData[i][j] = 36
            x+=1
print(x)
sData = dbData.T
# 获取价格数据
priceList = sData.values[2]
commentList = sData.values[3]
# matplotlib.pylab.plot(priceList,commentList,"mo")
# matplotlib.pylab.show()
da=dbData.values
line = len(da)
clo = len(da[0])
for i in range(0,line):
    for j in range(0,clo):
        if (da[i][2] > 130):
            print(da[i])
            da[i][j] = 36
        if (da[i][3] > 300):
            print(da[i])
            da[i][j] = 58
afterData = da.T
price = afterData[2]
comment = afterData[3]
matplotlib.pylab.plot(price,comment,"ro")
matplotlib.pylab.show()

# 分布分析
priceMax = afterData[2].max()
priceMin = afterData[2].min()
commentMax = afterData[3].max()
commentMin = afterData[3].min()

#极差
pricejc = priceMax - priceMin
commentjc = commentMax-commentMin

#组距
pricezj = pricejc/12
commentzj = commentjc/12

# 价格直方图
pricesty = numpy.arange(priceMin,priceMax,pricezj)
matplotlib.pylab.hist(afterData[2],pricesty)
matplotlib.pylab.show()
# 评论直方图
commentsty = numpy.arange(commentMin,commentMax,commentzj)
matplotlib.pylab.hist(afterData[3],commentsty)
matplotlib.pylab.show()

