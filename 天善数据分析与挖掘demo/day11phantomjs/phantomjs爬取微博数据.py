from selenium import webdriver
import re
from lxml import etree
url = "https://s.weibo.com/weibo/nba?topnav=1&wvr=6&b=1"
js = webdriver.PhantomJS()
js.get(url)
js.get_screenshot_as_file("E:/reptileContent/phantomjs/weibo/weibo.jpg")
dataHTML = js.page_source
# 去掉所有的em标签
patem = '<em class="s-color-red".*?>'
em = re.compile(patem)
dataEM = re.sub(em,"",dataHTML)
# 去掉所有的img标签
patimg = "<img.*?>"
img = re.compile(patimg)
dataIMG = re.sub(img,"",dataEM)
# 去掉所有的a标签
pata = "<a.*?>"
a = re.compile(pata)
dataA = re.sub(a,"",dataIMG)

# 提取微博数据
# pat = '<p class="txt" node-type="feed_list_content".*?(.*?)</p>'
# weiboData = re.compile(pat).findall(dataA)
# print(weiboData)
# 将data转换成tree，然后用xpath表达式提取
edata = etree.HTML(dataA)
title = edata.xpath('//p[@node-type="feed_list_content"]/text()')
print(title)
with open("E:/reptileContent/phantomjs/weibo/weibo.html","w",encoding="utf-8") as file:
    file.write(dataA)
js.quit()
