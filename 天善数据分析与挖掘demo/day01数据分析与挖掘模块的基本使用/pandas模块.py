import pandas
# series 某一串数字,在表格中代表一行或者一列
# DataFrame 数据框，表格中行和列整合出来的数据
a = pandas.Series([1,6,3,5],index=["a","b","c","d"])

b = pandas.DataFrame([[1,2,3,4],[5,6,7,8],[0,9,8,7]],columns=["a","b","c","d"])
print(b)

# 通过数组的方式创建数据框
data = pandas.DataFrame({
    "one":4,
    "two":[5,6,7],
    "three":["a","b","c"]
})

# head():头部数据，默认取前五行
headerData = b.head()
# head(行数)：取前几行
twoHeaderData = b.head(2)
# print(twoHeaderData)

# tail():尾部数据，默认取后五行
tailData = b.tail()
# print(tailData)
# tail(行数)：取后几行
oneTailData = b.tail(1)
# print(oneTailData)

# 列表数据信息
dataInfo = b.describe()
# print(dataInfo)

# 转置 行和列交换位置
bt = b.T
print(bt)

