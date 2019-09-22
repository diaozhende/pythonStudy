import urllib.error
import urllib.request

try:
    data = urllib.request.urlopen("http://blog.csdn.net/weiwei_pig/article/details/52123738").read()
# 异常处理是通用的
except urllib.error.URLError as e:
    print(e)
    if hasattr(e,"code"): # 判断是否有状态码
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
file = open("E:/reptileContent/weiwei_pig.html","wb")
file.write(data)
file.close()