import pandas
import numpy
import matplotlib.pylab
import pymysql
from sklearn.cluster import KMeans

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="pythontestdb")
sql = "select price,comment from taob limit 1000"
productData = pandas.read_sql(sql, conn)
print(productData)
# 取出特征数据
data = productData.iloc[:,:].as_matrix()

# 创建模型对象
k = KMeans(n_clusters=3)
# 训练数据
categoryData = k.fit_predict(data)

# 可视化
# x为价格，y为评论
for i in range(0, len(categoryData)):
    if (categoryData[i] == 0):
        matplotlib.pylab.plot(productData.iloc[i:i + 1, 0:1].as_matrix(), productData.iloc[i:i + 1, 1:2].as_matrix(),"mp")
    elif (categoryData[i] == 1):
        matplotlib.pylab.plot(productData.iloc[i:i + 1, 0:1].as_matrix(), productData.iloc[i:i + 1, 1:2].as_matrix(),"rs")
    elif (categoryData[i] == 2):
        matplotlib.pylab.plot(productData.iloc[i:i + 1, 0:1].as_matrix(), productData.iloc[i:i + 1, 1:2].as_matrix(),"gx")
matplotlib.pylab.show()
