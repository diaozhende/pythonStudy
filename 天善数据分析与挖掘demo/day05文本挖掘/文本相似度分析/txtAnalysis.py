import jieba
from gensim import corpora, models, similarities
from collections import defaultdict

# 读取数据
txt1Path = "E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/txt1.txt"
txt2Path = "E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/txt2.txt"
txtData1 = open(txt1Path).read()
txtData2 = open(txt2Path).read()
# 对文本进行分词
data1 = jieba.cut(txtData1)
data2 = jieba.cut(txtData2)

# 将分词数据转换成指定的格式
# "词语1 词语2 词语3 词语4"
termsData1 = ""
termsData2 = ""
for item in data1:
    termsData1 += item + " "
for item in data2:
    termsData2 += item + " "
docuemnts = [termsData1, termsData2]

# 将数据转换成数组的形式
texts = [[word for word in document.split()]
         for document in docuemnts]
# 计算词频
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
# 对词频第的数据进行筛选
texts = [[word for word in text if frequency[token] > 3]
         for text in texts]
# 读取要比对的数据
txt3 = "E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/txt3.txt"
txtData3 = open(txt3).read()
# 对数据进行分词
data3 = jieba.cut(txtData3)
# 将分词数据转换成指定的格式
termsData3 = ""
for item in data3:
    termsData3 += item + " "
# 通过语料库建立词典
dictionary = corpora.Dictionary(texts)
# 建立数据的稀疏向量
test_doc = dictionary.doc2bow(termsData3.split())
# 依据稀疏向量进一步处理，得到新的语料库
corups = [dictionary.doc2bow(word) for word in texts]
# 将新的语料库通过tfidfmodel进行处理，得到tfidf
tfidf = models.TfidfModel(corups)
# 通过token2id得到特征数
featuresNum = len(dictionary.token2id.keys())
# 计算系数矩阵的相似度，建立索引
index = similarities.SparseMatrixSimilarity(tfidf[corups], num_features=featuresNum)
# 依据索引得到相似度
sim = index[tfidf[test_doc]]
# 输出相似度
print(sim)
