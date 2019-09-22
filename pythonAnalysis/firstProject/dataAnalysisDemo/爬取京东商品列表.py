# //item.jd.com/100005853638.html

import urllib.request
import urllib.error
import re
url = "http://s.taobao.com/search?spm=a217h.9580640.831051.2.719325aaWhcz6D&q=iphone"
responseData = urllib.request.urlopen(url).read()
data = responseData.decode("utf-8","ignore") # 将data编码改成utf-8，ignore：设置编码会报错，ignore作用是将错误忽略
# print(data)
# href = "http://slide.news.sina.com.cn/c/slide_1_2841_389292.html"
pat = ':"(//detail.tmall.com/item.htm.*?)"'
newsList = re.compile(pat).findall(data)
for i in range(0,len(newsList)):
    try:
        print("第"+str(i)+"次爬取")
        thisurl = newsList[i]
        path = "E:/reptileContent/jdComputer/"+str(i)+".html"
        urllib.request.urlretrieve(thisurl,path)
        print("**************爬取成功********************")
    except urllib.error.URLError as e :
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)