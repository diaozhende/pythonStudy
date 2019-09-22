import urllib.request
import urllib.parse
# url = "http://www.iqianyue.com/mypost/"
# mydata = urllib.parse.urlencode(
#     {"name":"ceo@iqianyue.com","pass":"admin"}
# ).encode("utf-8")
# req = urllib.request.Request(url,mydata)
# data = urllib.request.urlopen(req).read()
# file = open("E:/reptileContent/login.html","wb")
# file.write(data)
# file.close()

import urllib.request
import urllib.parse
url="http://qzone.qq.com/"
mydata=urllib.parse.urlencode({
"u":"987020051",
"p":"zhangyujie520"
    }).encode("utf-8")
req=urllib.request.Request(url,mydata)
response=urllib.request.urlopen(req)
code = response.getcode()
print(code)
data=urllib.request.urlopen(req).read()
fh=open("E:/reptileContent/login1.html","wb")
fh.write(data)
fh.close()