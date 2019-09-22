import urllib.request
import re
def use_proxy(url,proxy_addr):
    proxy = urllib.request.ProxyHandler({"http:":proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data  = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    return data
url = "http://www.baidu.com"
proxy_addr = "163.204.240.201:9999"
data = use_proxy(url,proxy_addr)
print(len(data));

