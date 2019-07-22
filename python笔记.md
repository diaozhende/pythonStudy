### python笔记
##### 1.list
list是一个可变的有序表，类似于java的list,list中的数据类型可以不相同,list元素可以是可以是另一个list
方法:
1)向一个集合末尾添加数据
```python 
list.append("数据内容")
```

2)将数据添加到list中的指定位置
```python 
list.insert(索引,数据内容);
```
3)删除list中的数据
```python
//删除末尾数据
list.pop();
//删除指定位置的数据
list.pop(索引);
```
4)修改list数据
```python
//直接给指定的数据赋值
list[索引] = "数据内容";
```
5)获取list的元素个数
```python
len(list)
```

##### 2.tuple
tuple是一个不可变的元组,tuple一旦被初始化就不能被修改
```python 
//tuple初始化
text=("1","2","3")
//当tuple只有一个元素的时候初始化的时候元素后面必须加一个,
text=(1,)


//查看元素的值
text[索引]
```

##### 3.条件判断
if条件判断格式
```python
if <条件判断1>:
	<执行1>
else:
	<执行else>
    
//多条件的格式
if <条件判断 1>:
 	<执行 1>
elif <条件判断 2>:
	 <执行 2>
elif <条件判断 3>:
 	<执行 3>
else:
	 <执行 4>

```


##### 4.循环
python中的循环有两种,一种是for in迭代循环,另一种是while循环
1)for in 循环
格式:
```python 
for obj in list
列如:
list = ['1','2','3']
for value in list
	print(value)
//依次输出list的值
```
2)while循环
格式
```python
n=0
while n < 10:
	print(n)
	n=n+1
```
3)rang函数
rang函数,可以生成一个整数序列,再通过 list()函数可以转换为 list。比如 range(5)生成的序列是从 0 开始小于 5 的整数：
```python
 list(range(5))
 print(list)
```

#####5.dict- - -字典
dict相当于一个map,是key-value的形式,类似于java中的map集合,是无序的
1)dict初始化
```python
text = {"key1":"value1","key2":"value2","key3":"value3"}
```
2)
