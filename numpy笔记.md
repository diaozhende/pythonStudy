## numpy笔记

### 1、array属性

#### （1）定义一个array数组

```python
numpy.array([1,2,3,4],[5,6,7,8])
```

#### （2）形状

```python
data = numpy.array([1,2,3,4],[5,6,7,8])
data.shape
# (行，列)
```

#### （3）维度

```python
data.ndim
```

#### （4）类型

```python
data.dtype
```

### 2、ndarray类型

#### （1）创建指定类型的数组

```python
numpy.array([1,2,3,4],dtype="int32")
numpy.array([1,2,3,4],dtype=numpy.int32)
```

### 3、生成一个array数组

#### （1）生成0和1的数组

```python
# 生成0的数组
numpy.zeros((4,4),dtype="int32")# （行,列）
# 生成1的数组
numpy.ones((4,4),dtype="int32")
```

#### （2）从现有数组中生成

##### 1）深拷贝

```python
newdata1 = numpy.array(data)
newdata2 = numpy.copy(data)
```

##### 2）浅拷贝

```python
newData = numpy.asarray(data)
```

##### 深拷贝和浅拷贝的总结

`深拷贝和浅拷贝的区别在于，深拷贝当原始值改变之后，浅拷贝的值保持不变，浅拷贝的值发生改变`

##### 3）生成固定范围的数组

```python
numpy.linspace(1,10,100)# 下限，上限，数量，左闭右闭
numpy.arange(1,10,3)# 下限，上限，步长，左闭右开
```

### 4、生成随机数组

#### （1）生成均匀分布的数组

```python
data = numpy.random.uniform(low=-1,scale=1,size=10000)# 下限，上限，数量，左闭右开
# size一个以填形状，如：(3,4)
```

#### （2）生成正态分布的数组

```python
data = numpy.random.normal(low=-1,scale=1,size=1000)# 下限，上限，数量，左闭右开
# size一个以填形状，如：(3,4)
```

### 5、数组切片

```python
data = numpy.array([[1,2,3,4],[5,6,7,8]])
newData = data[0,:3]# 第一行，前三列

newData = data[:2,:-1]
#array([[1, 2, 3],[5, 6, 7]])
```

### 6、修改形状

#### （1）reshape

```python
data = numpy.array([[1,2,3,4],[5,6,7,8]])#(2,4)
# 将数组进行重新排列，排列成(4,2),对原始值没有影响
newData = data.reshape(4,2)
```

#### （2）resize

```python
data = numpy.array([[1,2,3,4],[5,6,7,8]])#(2,4)
data.resize(4,2)
# 没有返回新的值，对原始值进行修改
```

#### （3）T

```python
# 将数组进行翻转，行变列，列变行
data = numpy.array([[1,2,3,4],[5,6,7,8]])#(2,4)
newData = data.T
```

### 7、类型修改

```python
data = numpy.array([[1,2,3,4],[5,6,7,8]])#(2,4)
data.astype("float32")
```

### 8、数组去重

```python
data = numpy.array([[1,2,3,4],[2,6,2,8]])#(2,4)
newData = numpy.unique(data)
```

### 9、adarray逻辑运算

#### （1）>

```python
# 将大于4的数标记为True，否则标记为False
data = numpy.array([[1,2,3,4],[5,6,7,8]])#(2,4)
newData = data>4
```

#### （2）data[data>4]

```python
# 取出大于4的数据
newdata = data[data>4]
```

#### （3）对数据进行统一操作

```python
data = numpy.array([[1,2,3,4],[2,6,2,8]])#(2,4)
# 将大于4的数据改成100
data[data>4] = 100
```

#### （4）通用判断符

```python
# numpy.all() 传进一个布尔值数组，如果有一个False就返回False
# numpy.any() 传进一个布尔值，如果有一个True就返回True

# 判断pg[:2][:5]数据是否全是上涨的
allData = gp[:2][:5]>0
numpy.all(allData)

# 判断前五支股票是否有上涨的
allData = gp[:5,:]>0
numpy.any(allData)
```

#### （5）numpy.where(三目运算符)

```python
# numpy.where(一组布尔值，True的位置，False的位置)
# 判断前5只股票前四天的涨幅，大于0置为1，否则为0
numpy.where(data[:5,:4]>0 ,1 ,0)
```

#### （6）复合逻辑：numpy.logical_and,numpy.logical_or

```python
# 判断前5只股票前四天的涨幅，大于0.5且小于1的置为1，否则为0
numpy.where(numpy.logical_and(data>0.5,data<1),1,0)

# 判断前5只股票前四天的涨幅，大于0.5或小于-0.5的置为1，否则为0
numpy.where(numpy.logical_or(data>0.5,data<-0.5),1,0)
```

### 10、统计运算

```python
# 用法：numpy.函数名(data)或data.方法名()
# max：最大值，min：最小值，mean：平均值，median：中位数，var：方差，std：标准差

# 前四只股票前四天的每天最大涨幅
temp = data[:4,:4]
temp.max(axis=0)# 指定坐标轴，axis=0按行，axis=1按列

# 获取最大值的位置
temp.argmax(axis=1)
```

### 11、数组之间的运算

#### （1）数组与数之间的运算

```python
data = numpy.array([[1,2,3,4],[5,6,7,8]])
data+10 # 数组中的每一项都+10
```

#### （2）数组与数组之间的运算

```python
data1 = numpy.array([[1,2,3,4],[5,6,7,8]])#(2,4)
data2 = numpy.array([[1],[5]])#(2,1)
# 满足这两个条件才能进行数组之间的运算
# 1.维度相等
# 2.shape(其中相对应的一个地方为1)
data1+data2
# array([[ 2,  3,  4,  5],[10, 11, 12, 13]])
```

#### （3）矩阵运算

```python
score = numpy.array([[80,86],[82,80],[85,78],[90,90],[86,82],[82,90],[78,80],[92,94]])
```

##### 1）将数组转换成矩阵

```python
numpy.matrix(score)
```

##### 2）矩阵相乘

```python
# 矩阵相乘形状的变化
#（m行，n列）*（n行，l列） = （m行，l列）
score = numpy.array([[80,86],[82,80],[85,78],[90,90],[86,82],[82,90],[78,80],[92,94]])#（8，2）
qz = numpy.array([[0.3],[0.7]])#（2，1）
matscore = numpy.mat(score)
matqz = numpy.mat(qz)
matscore*matqz

# numpy.matmul(data1,data2)
numpy.matmul(score,qz)
```

### 12、合并与分割

#### （1）合并

```python
# numpy.hstack():水平拼接
# numpy.vstack():竖直拼接
# numpy.concatenate((data1,data2),axis):指定轴拼接
data1 = numpy.array([1,2,3])
data2 = numpy.array([4,5,6])
```

##### 1）水平拼接

```python
numpy.hstack(data1,data2)
#array([1, 2, 3, 4, 5, 6])
```

##### 2）竖直拼接

```python
numpy.vstack(data1,data2)
#array([[1, 2, 3],[4, 5, 6]])
```

##### 3）指定轴拼接

```python
# axis=1：水平拼接
# axis = 0：竖直拼接
data1 = numpy.array([[1,2],[3,4]])
data2 = numpy.array([[4],[5]])
numpy.concatenate((data1,data2),axis=1)
```

#### （2）分割

##### 1）按数量进行分割

```python
data = numpy.arange(0,9)
numpy.split(data,3)
# [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
```

##### 2）按索引进行分割

```python
arrIndex = numpy.arange(0,9)
numpy.split(arrIndex,[2,4,5])
# [array([0, 1]), array([2, 3]), array([4]), array([5, 6, 7, 8])]
```









