import jieba.analyse
txt = "我喜欢上海东方明珠"
result = jieba.analyse.extract_tags(txt,3)
for item in result:
    print(item)

# 返回词语的位置
result1 = jieba.tokenize(txt)
for item in result1:
    print(item)

result2 = jieba.tokenize(txt,mode="search")
for item in result2:
    print(item)