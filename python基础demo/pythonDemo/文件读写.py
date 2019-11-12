# 读文件
# readFile = open("D:/pythonFile.txt","r")
# txt = readFile.read()
# print(txt)
# readFile.close()

# with open("D:/pythonFile.txt","r",encoding="UTF-8") as f:
#     print(f.read())

# 写文件

# f = open("D:/pythonFile.txt", "w")
# f.write("这是python写入文件的内容")
# f.close()
with open("D:/pythonFile.txt", "w") as  f:
    f.write("这是用with函数写入的内容")

with open("D:/pythonFile.txt", "r") as r:
    print(r.read())
