import urllib.request
import re
"""
url = "http://74.41.0.1:8080/index.html#modules/tips/custquery.html"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0")
opener = urllib.request.build_opener()
opener.add_handler = [headers]
urllib.request.install_opener(opener)

data = urllib.request.urlopen(url).read()
path = "C:/Users/diaozhende/Desktop/data.html"
file = open(path,"wb")
file.write(data)
file.close()
"""
url = "http://74.41.0.1:8080/login.html"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
opener = urllib.request.build_opener()
opener.add_handler = [headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
# path = "C:/Users/diaozhende/Desktop/login.html"
# file = open(path,"wb")
# file.write(data)
pat = "background-image: url(.*?);"
result = re.compile(pat).findall(data)
for i in range(0,len(result)):
    img = result[i]
    imgPath = img[1:len(img)-1]
    imgUrl = "http://74.41.0.1:8080/"+imgPath
    print(imgUrl)
    path = "C:/Users/diaozhende/Desktop/login.jpg"
    urllib.request.urlretrieve(imgUrl,filename=path)
