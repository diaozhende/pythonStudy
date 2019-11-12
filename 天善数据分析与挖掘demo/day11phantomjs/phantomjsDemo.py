from selenium import webdriver
import re
from lxml import etree
from selenium import webdriver
import time
import re
from lxml import etree
bs=webdriver.PhantomJS()
time.sleep(3)
url="https://s.weibo.com/weibo?q=NBA&wvr=6&Refer=SWeibo_box"
bs.get(url)
bs.get_screenshot_as_file("D:/pythonFile/test.jpg")
data=bs.page_source
fh=open("D:/pythonFile/test.html","w")
fh.write(data)
fh.close()
bs.quit()
# js = webdriver.PhantomJS()
# url = "http://www.baidu.com"
# # 爬取网站
# js.get(url)
# # 将爬取的网站进行截图
# js.get_screenshot_as_file("E:/reptileContent/phantomjs/baidu/phantomjs.jpg")
# # 获取网站源码
# data = js.page_source
# with open("E:/reptileContent/phantomjs/baidu/baidu.html","w",encoding="utf-8") as file:
#     file.write(data)
# # 退出phantomjs窗口
# js.quit()