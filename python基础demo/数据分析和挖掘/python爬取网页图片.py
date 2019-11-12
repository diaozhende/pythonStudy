import urllib.request
import re

keyname = "上衣"
key = urllib.request.quote(keyname)

for i in range(0,10):
    url = "https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.3.5af911d9ZyWh1G&q="+key+"&cat=16&style=grid&seller_type=taobao&bcoffset=0&s="+str(i*60)
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat = 'pic_url":"//(.*?)"'
    imageurl = re.compile(pat).findall(data)

