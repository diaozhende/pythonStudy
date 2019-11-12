# *********************map和reduce***************************


# 得到list中每个元素的平方值
def function(x):
    return x*x
listText = [1,2,4,5,6,7,8,9]
result1 = map(function,listText)
print(list(result1))

result2 = map(str,listText)
print(list(result2))

result3 = sum(listText)
print(result3)


# *******************reduce***********************
def fn(x,y):
    return x*10+y
from functools import reduce
result4 = reduce(fn,listText)
print(result4)

# 将str序列转换成int序列
def paramNum(s):
    return s
s = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'7': 7, '8': 8, '9': 9}
result5 = reduce(fn,map(paramNum,s))
# print(result5)

# 利用lambda函数进行简化
def str2int():
    return reduce(lambda x,y:x*10+y,map(paramNum,s))
result6 = str2int()
# print(result6)

# 输入：['adam', 'LISA', 'barT']，输出：['Adam','Lisa', 'Bart']
listTextChange1 = ['adam', 'LISA', 'barT']
def change(x):
    text = x.title()
    return text
result7 = map(change,listTextChange1)
print(list(result7))


# 请编写一个 prod()函数，可以接受一个 list 并利用 reduce()求积

listNum = [1,2,3,4,5,6]
def functionResult(x,y):
    print("x:",x)
    print("y:",y)
    return x*y
def listResult(list):
    return list
result8 = reduce(functionResult,map(listResult,listNum))
print(result8)

# 利用 map 和 reduce 编写一个 str2float 函数，把字符串'123.456'转换成浮点数 123.456

