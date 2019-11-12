import os
# print(os.name)
# print(os.environ)

# 查看当前目录的绝对路径
# print(os.path.abspath("."))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
# path = os.path.join("D:/pythonFile","test1File.txt")
# print(path)
# 创建一个目录
# os.mkdir(path)
# 删除一个目录
# os.rmdir(path)

# D:\pythonFile\test1File\file1.txt

# fileName = os.path.split("D:/pythonFile/test1File/file1.txt")
# print(fileName)
#
# # 获取文件的扩展名
# fileType = os.path.splitext("D:/pythonFile/test1File/file1.txt")
# print(fileType)

# 对文件重命名
# os.rename("D:\\pythonFile\\test1File\\file1.txt","fileText.txt")

print( [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])