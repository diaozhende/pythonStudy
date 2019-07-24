# **************************迭代**************************

listText = {"第一个key":"第一个value","第二个key":"第二个value","第三个key":"第三个value","第四个key":"第四个value","第五个key":"第五个value"};
# python中默认是通过key进行迭代
for key in listText:
    print(key)

# 迭代value
for value in listText.values():
    print(value)

#迭代字符串
text = "ABCDEFG"
for val in text:
    print(val)

# 判断一个对象是否是可迭代对象
# from collections import Iterable
# flag = isinstance("123",Iterable)
# print(flag)

userList = ["zhangsan","lisi","wangwu","zhaoliu"]
for i ,t in enumerate(userList):
    print("索引:",i,"值：",t)

userListText = [("zhangsan","jinan"),("lisi","weifang"),("wangwu","qingzhou"),("zhaoliu","qingzhou")]
for x,y in userListText:
    print(x,y)