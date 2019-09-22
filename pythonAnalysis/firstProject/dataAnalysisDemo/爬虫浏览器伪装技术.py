import urllib.request
url="http://blog.csdn.net/weiwei_pig/article/details/52123738"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
file = open("E:/reptileContent/headers.html","wb")
file.write(data)
file.close()