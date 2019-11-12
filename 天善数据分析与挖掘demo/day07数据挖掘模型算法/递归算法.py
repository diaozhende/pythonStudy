import learn as learn
import pandas
# 读取数据
data = pandas.read_csv("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第8周/luqu.csv")
# x = data.iloc[:,1:4].as_matrix()
# y = data.iloc[:,0:1].as_matrix()
x = data.iloc[:,1:4].values
y = data.iloc[:,0:1].values

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression
# 特征筛选
r1 = RandomizedLogisticRegression()
r1.fit(x,y)
r1.get_support()
print(data.columns[r1.get_support()])