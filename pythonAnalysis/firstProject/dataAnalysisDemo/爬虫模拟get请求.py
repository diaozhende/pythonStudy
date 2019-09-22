import urllib.request
content = "python"
# 处理中文
# 如果搜索的内容是中文，用quote()方法处理一下
# content = urllib.request.quote(content)
url = "http://www.baidu.com/s?wd="+content
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()

file = open("E:/reptileContent/搜索python.html","wb")
file.write(data)
file.close()



