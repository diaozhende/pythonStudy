# KMean算法
# 通过程序实现录学生的聚类
import pandas
import numpy
import matplotlib.pylab
from sklearn.cluster import KMeans

# 读取数据
studentData = pandas.read_csv("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第9周/luqu.csv")
# 取出特征数据
xData = studentData.iloc[:,1:4].as_matrix()
# 创建KMean对象
k = KMeans(n_clusters=2)#n_clusters:聚成几类，n_jobs:线程数，max_iter:最大循环次数
# 对数据进行分类
y = k.fit_predict(xData)
# 可视化
# x代表学生的序号，y代表学生类别
s = numpy.arange(0,len(y))
matplotlib.pylab.plot(s,y,"o")
matplotlib.pylab.show()