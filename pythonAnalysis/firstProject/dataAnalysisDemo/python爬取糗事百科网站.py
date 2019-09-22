# https://www.qiushibaike.com/hot/page/1/
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36
import urllib.request
import re
opener = urllib.request.build_opener()
header = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
opener.addheaders = [header]
urllib.request.install_opener(opener)
for i in range(1,10):
    url = "http://www.qiushibaike.com/hot/page/"+str(i)+"/"
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat = '<div class="content">*.?<span>(.*?)</span>*.?</div>'
    dataList = re.compile(pat,re.S).findall(data)
    print("****************第"+str(i)+"次爬取成功*************************")
    print(dataList)


