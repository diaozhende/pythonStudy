import pandas
import numpy
import pymysql
import matplotlib.pylab
from sklearn.decomposition import PCA
conn = pymysql.connect("127.0.0.1","root","root","pythontestdb")
sql = "select hits,comment from myhexun"
dbData = pandas.read_sql(sql,conn)
ch = dbData[u"comment"]/dbData[u"hits"]
dbData[u"评点比"] = ch
# 主成分分析
pca1 = PCA()
pca1.fit(dbData)
# 返回模型中的各个特征量
Characteristic = pca1.components_
print(Characteristic)

# 各个成分中各自的方差百分比，贡献率
rate = pca1.explained_variance_ratio_
print(rate)