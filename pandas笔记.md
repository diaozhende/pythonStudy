

## pandas笔记

### 1、DataFrame数据框

#### （1）将数组数据转换成DataFrame

```python
pandas.DataFrame(data)
```

#### （2）向DataFrame中添加行索引

```python
# 生成索引
stock = ["股票{}".format(i+1)for i in range(10)]
# 添加索引
pandas.DataFrame(data,index=stock)
```

#### （3）向DataFrame中添加列索引

```python
# 生成索引
date = pandas.date_range(start="20191101",periods="5",freq="B") # 开始时间，数量，格式
# DatetimeIndex(['2019-11-01', '2019-11-04', '2019-11-05', '2019-11-06',            '2019-11-07'],dtype='datetime64[ns]', freq='B')
# 添加列索引
pandas.DataFrame(data,columns=date)
```

#### （4）DataFrame的属性

##### 1）形状

```python
data.shape
```

##### 2）获取行索引和列索引

```python
# 行索引
data.index
# 列索引
data.columns
```

##### 3）获取DataFrame中数组的值

```python
data.values
```

##### 4）DataFrame转置(行变列，列变行)

```python
data.T
```

##### 5）获取DataFrame的前几行和后几行,如果不指定的话默认是5行

```python
# 前几行
data.head(2)
# 后几行
data.tail(3)
```

### 2、基本数据操作

#### （1）读取数据文件

```python
# 读取csv文件
data = pandas.read_csv("文件路径")
# 读取json文件
sa = pandas.read_json("Sarcasm_Headlines_Dataset.json", orient="records", lines=True)
# 读取HDF5文件
day_close = pandas.read_hdf("./stock_data/day/day_close.h5")
```

#### （2）删除某些列数据

```python
data.drop(["ma5","ma10","ma20","v_ma5","v_ma10","v_ma20"],axis=1)
```

#### （3）获取某一项的值

```python
data["high"]["2018-2-27"]#必须先列后行

new_data.loc["2018-2-27"]["high"]# 先行后列

new_data.iloc[2,1]# 先行后列，根据索引
```

#### （4）指定索引

```python
data.set_index("date",drop=True)
```

#### （5）批量获取数据

```python
data.ix[:4,['open', 'close', 'high', 'low']]
```

#### （6）赋值操作

```python
# 将某一列进行统一赋值
data.open = 100

# 对某一个项进行赋值
data.iloc[1,2] = 9999
```



####  （7）排序

```python
# 按照某一列进行排序,也可以指定多行
# ascending = True时是升序排列，False为降序排列
data.sort_values(by=["high"],ascending=False)
```

### 3、算数运算

```python
# 对某一列进行统一操作
stock_data["open"].add(3).head() # 加
stock_data.sub(100) # 减
```

### 4、逻辑运算<、 >、|、 &

####  （1）>

```python
# 例如筛选p_change > 2的日期数据
stock_data[stock_data["p_change"]>2]
```

#### （2）&

```python
# 完成一个多个逻辑判断， 筛选p_change > 2并且low > 15
stock_data[(stock_data["p_change"]>2) & (stock_data["low"]>15)]
```

#### （3）query()

```python
# query()方法
stock_data.query("p_change>2 & low <15")
```

#### （4）isin

```python
# 判断'turnover'是否为4.19, 2.39
stock_data[stock_data["turnover"].isin([4.19,2.39])]
```

### 5、统计运算

#### （1） DataFram表数据的平均数，方差，标准差等信息

```python
stock_data.describe()
```

#### （2）获取最大值和最大值索引

```python
# 获取最大值
# axis=0时是获取每一列的最大值，1为获取每一行的最大值
stock_data.max(axis=0)

# 获取最大值的索引
stock_data.idxmax(axis=0)
```



### 6、数据的缺失值处理

#### （1）isnull()

```python
data.isnull()
# 返回一个布尔列表，缺失值的项的值为True，其他的为False
```

#### （2）notnull()

```python
data.notnull()
# 返回一个布尔列表，缺失值的项的值为False，其他的为True
```



#### （3）判断数据中是否含有缺失值

```python
numpy.any(pandas.isnull(data))# 返回True，说明数据中存在缺失值
numpy.all(pandas.notnull(data))# 返回False，说明数据中存在缺失值

pandas.isnull(data).any() # 输出所有列是否缺失值，True表示有缺失值
pandas.notnull(data).all() # 输出所有列是否缺失值，False表示有缺失值
```

#### （4）缺失值处理

##### *1、删除

```python
# 将含有缺失值的样本删除
data.dropna()
```

#####  *2、替换

```python
# 方法二：替换
# 找出缺失值的列，Revenue (Millions)，Metascore
# 将缺失值替换成平均值或者是中位数
data["Revenue (Millions)"].fillna(data["Revenue (Millions)"].mean(),inplace=True)
data["Metascore"].fillna(data["Metascore"].mean(),inpalce=True)
```

##### *3、其他符号的缺失值

```python
# 并不是所有的缺失值都是nan，还有可能是其他标志，遇到这种情况，先将标志转换成nan标志，再通过nan处理的方式进行处理
data.replace(to_replace="?",value=numpy.nan)
```

### 7、数据离散化（one-hot编码）

#### （1）自动分组

```python
# 数据，组数
pandas.qcut(data,3)
```

#### （2）自定义分组

```python
# 定义区间
bins=[-100, -7, -5, -3, 0, 3, 5, 7, 100]
# 分组
pandas.cut(data,bins)
```

#### （3）查看每组数据数量

```python
groupData.value_counts()
```

#### （4）将分组好的数据转换成one-hot编码

```python
pandas.get_dummines(groupData,prefix="height")# prefix：分组区间的前缀
```

### 8、表的合并

#### （1）concat()

```python
pandas.concat([data1,data2],axis=1)# axis=1代表水平合并，=0代表竖直合并
```

#### （2）merge()

##### *left

```python
# on：以哪一列为准进行合并
pandas.merge(left,right,how="left",on=["key1","key2"])# 以左表为准，右表没有的填Nan
```

##### *inner

```python
# 将两个表相同的key1和key2合并
pandas.merge(left,right,how="inner",on=["key1","key2"])
```

##### *outer

```python
# 将两个表的数据全部进行合并，没有的数据用NaN填充
pandas.merge(left,right,how="outer",on=["key1","key2"])
```

### 9、corsstab交叉表

```python
# 统计股票涨跌数量
# gpData["pona"]=1表示涨，=0表示跌
pandas.crosstab(gpData["week"],gpData["pona"])
```

### 10、透视表

```python
# 统计gpData["pona"] = 1的数据所占的百分比，index指定行索引
gpData.pivot_table(gpData["pona"],index=gpData["week"])
```

### 11、分组和聚合

```python
col =pandas.DataFrame({'color': ['white','red','green','red','green'], 'object': ['pen','pencil','pencil','ashtray','pen'],'price1':[5.56,4.20,1.30,0.56,2.75],'price2':[4.75,4.12,1.60,0.75,3.15]})
# 进行分组，对颜色分组，price1进行聚合
# 用dataframe的方法进行分组
col.groupby(by="color")["price1"].max()
# 或者
col["price1"].groupby(col["color"]).max()
```

