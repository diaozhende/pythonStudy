# ***********************sorted 排序函数****************************

# 从小到大排序
listText=[45,-10,1,35,-89]
result = sorted(listText,reverse=True)
print(result)

# 按照绝对值大小排序
resultAbs = sorted(listText,key = abs)
print(resultAbs)

# 字符串排序
paramStr = ['bob', 'about', 'Zoo', 'Credit']
resultStr = sorted(paramStr)
print(resultStr)
# 字符串排序忽略大小写
resultStrLower = sorted(paramStr,key = str.lower)
print(resultStrLower)
# 反向排序
resultStrLowerReverse = sorted(paramStr,key = str.lower,reverse=True)
print(resultStrLowerReverse)

# 章节练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
nameList = []
scoreList = []

def by_name(t):
    for key,value in t:
        nameList.append(key)
def by_score(t):
    for key,value in t:
        scoreList.append(value)
nameResult = sorted(nameList,key=by_name(L))
print(nameResult)
scoreResult = sorted(scoreList,key=by_score(L))
print(scoreResult)