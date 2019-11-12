import jieba
import jieba.posseg
import jieba.analyse
txt = "我喜欢上海东方明珠"
# 全模式分词
word1 = jieba.cut(txt,cut_all=True)
for item in word1:
    print(item)
print("")
#精准模式（cut_all参数可以省略，默认是精准模式）
word2 = jieba.cut(txt,cut_all=False)
for item in word2:
    print(item)
print("")
# 搜索引擎模式
word3= jieba.cut_for_search(txt)
for item in word3:
    print(item)
print("")

# 词性标注
word2 = jieba.posseg.cut(txt)
for item in word2:
    # item.word:返回词语
    # item.flag:返回词性
    print(item.word+"*************"+item.flag)
print("")
'''
a:形容词
c:连词
d:副词
e:叹词
f:方位词
i:成语
m:数词
n:名词
nr:人名
ns:地名
nt:机构团体
nz:其他专有名词
p:介词
r:代词
t:时间
u:助词
v:动词
vn:名动词
w:标点符号
un:未知词语
'''

# 加载词典
jieba.load_userdict("D:/Program Files/python/Lib/site-packages/jieba/dict1.txt")
txt2 = "济南绿灯行是一个广告传媒公司"
word4 = jieba.posseg.cut(txt2)
for item in word4:
    print(item.word+"***************"+item.flag)
print("")
# 提取关键字
# txt:数据
# 3：关键字的个数（默认是20个）
word5 = jieba.analyse.extract_tags(txt,2)
print(word5)
# 返回词语的位置
word6 = jieba.tokenize(txt)
for item in word6:
    print(item)
print("")
# 使用搜索引擎模式返回词语位置
word7 = jieba.tokenize(txt,mode="search")
for item in word7:
    print(item)