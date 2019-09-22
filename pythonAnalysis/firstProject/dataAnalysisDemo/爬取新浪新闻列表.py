import urllib.request
import urllib.error
import re
url = "http://news.sina.com.cn/"
responseData = urllib.request.urlopen(url).read()
data = responseData.decode("utf-8","ignore") # 将data编码改成utf-8，ignore：设置编码会报错，ignore作用是将错误忽略
# href = "http://slide.news.sina.com.cn/c/slide_1_2841_389292.html"
pat = 'href="(http://slide.news.sina.com.cn/.*?)"'
newsList = re.compile(pat).findall(data)
for i in range(0,len(newsList)):
    try:
        print("第"+str(i)+"次爬取")
        thisurl = newsList[i]
        path = "E:/rerequestptileContent/sinaNews/"+str(i)+".html"
        urllib.urlretrieve(thisurl,path)
        print("**************爬取成功********************")
    except urllib.error.URLError as e :
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)