# https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&agent_version=9.11.5&authcookie=null&business_type=17&
# content_id=5728507900&hot_size=0&last_id=217863040921&page=&page_size=20&types=time&callback=jsonp_1567758511564_96083
import urllib.request
import re
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/69.0"}
opener = urllib.request.build_opener()
opener.add_handler = [headers]
urllib.request.install_opener(opener)
url = "https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&agent_version=9.11.5&authcookie=null&business_type=17&content_id=5728507900&hot_size=0&last_id=217917219121&page=&page_size=20"
for i in range(1,20):
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat = '"content":"(.*?)"'
    patId = '"id":"(.*?)"'
    content = re.compile(pat).findall(data)
    idList = re.compile(patId).findall(data)
    print("******************第"+str(i)+"次爬取成功**************************")
    print(content)
    url = "https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&agent_version=9.11.5&authcookie=null&business_type=17&content_id=5728507900&hot_size=0&last_id="+idList[len(idList)-1]+"&page=&page_size=20"
    for j in range(0,len(content)):
        path = "E:/reptileContent/aiqiyi/content/content.txt"
        # file = open(path, "w")
        # file.write(content[j])
        # file.close()
        with open(path,"a+",encoding="utf-8") as f:
            f.write(content[j]+"\n")