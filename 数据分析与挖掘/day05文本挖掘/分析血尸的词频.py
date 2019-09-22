import jieba.analyse
data = open("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/血尸.txt").read()
result = jieba.analyse.extract_tags(data,10)#10代表个数
print(result)