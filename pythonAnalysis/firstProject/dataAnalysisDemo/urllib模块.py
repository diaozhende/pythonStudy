# 1.urlretrieve()方法：直接将要爬取的网页下载到本机
import urllib.request
#urllib.request.urlretrieve("http://www.baidu.com",filename = "E:/reptileContent/baidu.html")

# 2.urlclearup():清除urllib缓存
urllib.request.urlcleanup()

# 3.info()：显示当前环境的信息
file = urllib.request.urlopen("http://www.baidu.com")
#print(file.info())

# 4.getcode()：获取返回的状态码
code = file.getcode()
print(code)

# 5.geturl()：获取当前爬取的网址
thisUrl = file.geturl()
print(thisUrl)

# 6.timeout()：设置超时时间
try:
    file = urllib.request.urlopen("http://www.baidu.com", timeout=0.01)
except Exception as e:
    print("连接超时")
