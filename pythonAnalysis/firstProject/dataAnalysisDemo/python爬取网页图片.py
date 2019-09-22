import urllib.request
import re

keyname = "上衣"
key = urllib.request.quote(keyname)
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
for i in range(1,10):
    print("第"+str(i)+"次爬取")
    # url = "https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.3.5af911d9ZyWh1G&q="+key+"&cat=16&style=grid&seller_type=taobao&bcoffset=0&s="+str(i*60)
    url = "http://s.taobao.com/list?spm=a21bo.2017.201867-links-0.5.5af911d9MHNWNK&q="+key+"&style=grid&seller_type=taobao&bcoffset=0&s="+str(i*60)
    print("爬取地址："+url)
    # url = "https://list.jd.com/list.html?cat=670,671,672&page="+str(i)+"&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"
    # print(url)
    data = urllib.request.urlopen(url).read()
    path = "C:/Users/diaozhende/Desktop/data.html"
    file = open(path, "wb")
    file.write(data)
    file.close()
    # "picUrl": "//g-search3.alicdn.com/img/bao/uploaded/i4/i3/2168647576/TB2.oJmgwHqK1RjSZFkXXX.WFXa_!!2168647576.jpg"
    # pat = '"picUrl": "//g-search3.alicdn.com/img/bao/uploaded/i4/(.*?).jpg'
    # imageUrl = re.compile(pat).findall(data)
    # print(imageUrl)
    # pat = 'src="//img(.*?)"'
    # imageurl = re.compile(pat).findall(data)
    # print(imageurl)
    # for j in range(0,len(imageurl)):
    #     thisImgUrl = "http://img"+imageurl[j]
    #     file = "E:/reptileContent/图片/"+str(i)+str(j)+".jpg"
    #     urllib.request.urlretrieve(thisImgUrl,filename=file)

# file = open("E:/reptileContent/图片地址/imageUrl.txt","wb")
# file.write(content)
# file.close()


