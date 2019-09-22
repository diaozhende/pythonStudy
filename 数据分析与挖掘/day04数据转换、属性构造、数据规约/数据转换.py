import numpy
import pandas
import matplotlib.pylab
import pymysql

conn = pymysql.connect("127.0.0.1","root","root","pythontestdb")
sql = "select price,comment from taob"
dbData = pandas.read_sql(sql,conn)
print(dbData.describe())
# 离差标准化：（当前数据-数据中的最小值）/（数据最大值-数据最小值）
deviationData = (dbData - dbData.min())/(dbData.max()-dbData.min())
# print(deviationData)

# 标准差标准化（standard）:(当前数据-平均数)/标准差
standard =(dbData-dbData.mean())/dbData.std()
# print(standard)
# 小数定标标准化（scaling）:（当前数据/10**(k)、k=log10(x的绝对值的最大值)）
k = numpy.log10(dbData.abs().max())
scaling = (dbData/10)**k
# print(scaling)


# 等宽数据离散化
priceData = dbData[u"price"].copy()
inersionPriceData =priceData.T
inersionPriceDataValue = inersionPriceData.values
discretizationData1 = pandas.cut(inersionPriceDataValue,3,labels=["便宜","适中","贵"])
# print(discretizationData1)
k = [0,50,100,300,500,2000,inersionPriceDataValue.max()]
discretizationData2 = pandas.cut(inersionPriceDataValue,k,labels=["非常便宜","便宜","适中","有点贵","很贵","非常贵"])
print(discretizationData2)