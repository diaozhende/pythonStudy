import urllib.request
data = urllib.request.urlopen("http://www.baidu.com").read()
print(str(data))