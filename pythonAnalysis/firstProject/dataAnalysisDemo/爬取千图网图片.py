import urllib.request
import re
"""
    url = "https://www.58pic.com/piccate/3-0-0.html"
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat = 'data-original="//(.*?).jpg!'
    imageurl = re.compile(pat).findall(data)
    print(imageurl)
    for i in range(0,len(imageurl)):
        imgUrl = "http://"+imageurl[i]+".jpg!w1024_new_0"
        file = "E:/reptileContent/千图网图片/"+str(i)+".jpg"
        urllib.request.urlretrieve(imgUrl,filename=file)
"""

headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
for i in range(1,10):
    url = "https://www.58pic.com/piccate/2-130-0-p"+str(i)+".html"
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat = 'data-original="//(.*?).jpg!'
    imageUrlList = re.compile(pat).findall(data)
    for j in range(0,len(imageUrlList)):
        imgUrl = "http://"+imageUrlList[j]+".jpg!w1024_new_0"
        file = "E:/reptileContent/千图网图片/"+str(i)+str(j)+".jpg"
        urllib.request.urlretrieve(imgUrl,filename=file)
