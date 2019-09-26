from selenium import webdriver
import re
js = webdriver.PhantomJS()
url = "http://74.41.0.1:8080/index.html#modules/customer/importcust.html"
js.get(url)
js.get_screenshot_as_file("E:/reptileContent/crm/test.jpg")
data = js.page_source
with open("E:/reptileContent/crm/test.html","w") as file:
    file.write(data)
js.quit()