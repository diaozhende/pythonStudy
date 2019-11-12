# ***********************列表生成式********************************
# 生成一个[1x1,2x2,....,10x10]
listText1 = [x * x for x in range(1,11)]
print(listText1)

# for循环后面还可以加判断
listText2 = [x*x for x in range(1,11) if x%2 == 0]
print(listText2)

# 两层for循环
listText3 = [x+n for x in "ABC" for n in "XYZ"]
print(listText3)
# 列出当前目录下所有的文件名
import os
listText4 = [d for d in os.listdir('.')]
print(listText4)

# 通过isinstance函数判断一个变量是不是字符串类型
text = '123'
text1 = 123
flag = isinstance(text1,str)
print(flag)


# L1 = ['Hello', 'World', 18, 'Apple', None]   期待输出: ['hello', 'world', 'apple']
L1 = ['Hello', 'World', 18, 'Apple', None]
result = [text for text in L1 if isinstance(text,str)]
print(result)