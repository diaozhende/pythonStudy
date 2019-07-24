# ********************filter*********************

# list中删除偶数，保留奇数
def is_odd(x):
    return x%2==1
is_odd_param = [1,2,3,4,5,6,7,8,9,10,11,12,13]
is_odd_result = list(filter(is_odd,is_odd_param))
print(is_odd_result)

# 把一个list中的空字符串删除
def not_empty(x):
    return x and x.strip()
not_empty_param = ['1','2','',None,'77','','9898']
not_empty_result = list(filter(not_empty,not_empty_param))
print(not_empty_result)