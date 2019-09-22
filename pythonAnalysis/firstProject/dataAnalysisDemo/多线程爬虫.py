import urllib.request
import re
import threading
opener = urllib.request.build_opener()
header = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
opener.addheaders = [header]
urllib.request.install_opener(opener)
class One(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,36,2):
            print("one"+str(i))
            url = "http://www.qiushibaike.com/hot/page/" + str(i) + "/"
            data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
            pat = '<div class="content">*.?<span>(.*?)</span>*.?</div>'
            dataList = re.compile(pat, re.S).findall(data)
            print("****************第" + str(i) + "次爬取成功*************************")
            print(dataList)

class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0, 36, 2):
            print("two"+str(i))
            url = "http://www.qiushibaike.com/hot/page/" + str(i) + "/"
            data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
            pat = '<div class="content">*.?<span>(.*?)</span>*.?</div>'
            dataList = re.compile(pat, re.S).findall(data)
            print("****************第" + str(i) + "次爬取成功*************************")
            print(dataList)

# one = One()
# one.start()
# two = Two()
# two.start()

class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,10):
            print("我是线程A")
class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,10):
            print("我是线程B")
t1=A()
t1.start()
t2=B()
t2.start()