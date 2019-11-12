import pandas
import numpy
import matplotlib.pylab

#E:/python大数据资料/Python3数据分析与挖掘实战/源码/第6周/hexun.xls
data = pandas.read_excel("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第6周/hexun.xls")
#data.values#[第几行][第几列]
dataT = data.T

x = dataT.values[3]
# y = dataT.values[4]
ids = dataT.values[0]
matplotlib.pylab.plot(ids,x)
matplotlib.pylab.show()
