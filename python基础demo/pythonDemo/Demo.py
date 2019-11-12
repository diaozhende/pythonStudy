# **********************list练习**********************
# list = ['a','b','c','d']
# 在末尾添加数据
# list.append('123')
# 在指定位置添加数据
# list.insert(1,'指定位置添加数据')
# 删除末尾数据
# list.pop()
# 删除指定位置的数据
# list.pop(0)
# 修改指定位置的数据
# list[0] = "修改指定位置的数据"
# print(list)
# num = len(list);
# print(num)

# **********************tuple练习****************
# text = ("1","2","3")
# print(text)

# *********************tuple和list章节练习************************
# L = [
#  ['Apple', 'Google', 'Microsoft'],
#  ['Java', 'Python', 'Ruby', 'PHP'],
#  ['Adam', 'Bart', 'Lisa']
# ]
# # 打印Apple
# print(L[0][0])
# # 打印 Python:
# print(L[1][1])
# # 打印 Lisa:
# print(L[2][2])


# *********************if条件判断************************
# flag = False
# if flag:
#     print("flag的值为true")
# else:
#     print("flag的值为false")

# *********************if条件判断章节练习************************
# height = 1.75
# weight = 80.5
# result = weight/height
# print(result)
# if result<18.5:
#     print("过轻")
# elif result>=18.5 and result<=25:
#     print("正常")
# elif result>=28 and result <=32:
#     print("肥胖")
# else:
#     print("严重肥胖")

# *********************for循环************************
# list = ["1","2","3","4","5"]
# for value in list:
#     print(value)

# *********************while循环************************
# n=0
# while n<5:
#     print(n)
#     n = n+1

# *********************循环章节练习************************
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print("hello  "+name)

# ********************dict和set*****************************

# map = {"A":"1","B":"2","C":"3"};
# print(map)
# map.pop("A")
# print(map)
# flag = "C" in map
# print(map.get("D"))

demoSet1 = set([1,2,4,5,6,7,1])
demoSet2 = set([2,4,6])
# demoSet1.add(2)
# demoSet1.remove(1)
# result = demoSet1 & demoSet2
# result = demoSet1 | demoSet2
# print(result)

test = "abcd"
test1 = test.replace("a","A")
print(test1)
