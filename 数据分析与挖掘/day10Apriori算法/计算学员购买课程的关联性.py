from apriori import *
import pandas
# 读取数据
lessonData = pandas.read_excel("E:\\python大数据资料\\Python3数据分析与挖掘实战\\源码\\lesson_buy.xls",header=None)
# 转换数据
change = lambda x:pandas.Series(1,index=x[pandas.notnull(x)])
dataMap = map(change,lessonData.as_matrix())
data = pandas.DataFrame(list(dataMap)).fillna(0)
# 设置临界支持度、置信度
spt = 0.1# 支持度
cfd = 0.3# 置信度
# 使用apriori算法计算关联结果
find_rule(data,spt,cfd,"-->")# data：数据，spt：支持度，cfd：置信度，-->:连接符
