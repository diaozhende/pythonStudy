import jieba.analyse
import urllib.request
data = urllib.request.urlopen("http://127.0.0.1:8080/dmbj/dmbj.html").read().decode("utf-8","ingore")
result = jieba.analyse.extract_tags(data,5)
print(result)