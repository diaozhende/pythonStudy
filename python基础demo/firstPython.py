# try:
#     fileName = open("new.txt", 'r')
#     for eachLine in fileName:
#         print(eachLine),
#     fileName.close()
# except IOError e:
#     print("Error:",e)

def function_name():
    print("这是一个方法")
    return "1"
flag = function_name()
print(flag)