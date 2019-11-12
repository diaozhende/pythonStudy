import urllib.request
import re
from lxml import etree
# opener = urllib.request.build_opener()
# header={"User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
# opener.addheaders=[header]
# urllib.request.install_opener(opener)
url = "https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=0&page=5&lefnav=0&cursor=&__rnd=1569246690272"
data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
# 去掉所有的img标签
patimg = "<img*.?>"
img = re.compile(patimg)
dataimg = re.sub(img,"",data)
# 去掉所有的em标签
patem = "<em.*?>"
em = re.compile(patem)
dataem = re.sub(em,"",dataimg)
# 去掉所有的a标签
pata = "<a.*?>"
a = re.compile(pata)
dataa = re.sub(a,"",dataem)
# 去掉所有br标签
patbr = "<br.*?>"
br = re.compile(patbr)
databr = re.sub(br,"",dataa)
# 去掉所有span标签
patspan = "<br.*?>"
span = re.compile(patspan)
dataspan = re.sub(span,"",databr)
edata = etree.HTML(dataspan)
xdata = edata.xpath('//h3@[class="list_title_s"]/text()')
print(xdata)
# with open("E:/reptileContent/phantomjs/weibo/weobo.html","w",encoding="utf-8") as file:
#     file.write(dataspan)

