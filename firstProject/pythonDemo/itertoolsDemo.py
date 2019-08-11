import itertools
# result = itertools.count(1)
# for num in result:
#     print(num)

# 把传入的一个序列无限重复下去
# cs = itertools.cycle("ABCD")
# for item in cs:
#     print(item)

# result = itertools.repeat("A",10)
# for obj in result:
#     print(obj)

# for item in itertools.chain("ABC","XYZ"):
#     print(item)
for key,group in itertools.groupby("AABBCCDDAA"):
    print(key,list(group))