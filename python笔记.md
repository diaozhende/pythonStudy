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

##### 5.dict- - -字典
dict相当于一个map,是key-value的形式,类似于java中的map集合,是无序的
1)dict初始化
```python
text = {"key1":"value1","key2":"value2","key3":"value3"}
```
2)dict添加元素
```python
text["newText"] = "newText"
```
3)删除元素
```python
text.pop(key)
```
4)获取元素
```python
\\通过in判断key是否在这个dictzhong,如果存在返回True,如果不存在返回False
"key" in text
\\通过get方法获取dict的值,如果不存在返回None
text.get("newText")

\\get方法获取值当不存在的时候还可以返回指定的值
text.get("newText",-1)
```


##### 6.set
set和dict 类似，也是一组key的集合，但不存储value由于key不能重复，所以，在set中,没有重复的key,是无序的
1)创建一个set
```python
demoSet = ([1,2,3,4])
```
2)向set添加数据
```python
//如果向set中添加重复数据的话，程序不会报错，重复数据会被忽略
demoSet.add("newText")
```
3)set通过remove删除数据
```python
demoSet.remove(4)
```
4)两个set做数学上的交集和并集
```python
demoSet1 = set([1,2,4,5,6,7,1])
demoSet2 = set([2,4,6])
demoSet1.add(2)
demoSet1.remove(1)
result = demoSet1 & demoSet2
result = demoSet1 | demoSet2
```
##### 7.replace函数
replace函数是将字符串中的字符进行替换
```python
test = "abcd"
test1 = test.replace("a","A")
```

##### 8.函数模块
1)定义函数
```python
//函数的基本格式
def 函数名(参数):
	函数的逻辑
    return result
   
```
2)调用函数
```python
函数名(参数)
```
3)定义一个空函数
```python
//pass表示展位
def nulFunction():
	pass
//在if判断中也可以加入pass
def function(x):
	if x>0:
    	print(x)
    else:
    	pass
```
4)函数返回多个值
```python
def moreResult(x,y,z):
	return x,y,z
//调用函数,函数返回多值实际上就是返回了一个tuple
x,y,z = moreResult(1,2,3)
```
##### 9.isinstance函数,类型检查函数
```python
def typeCheck(param):
    if not isinstance(param,(int,float)):
        raise TypeError("参数类型错误")
    if param >0:
        print("参数大于零")
    else:
        print("参数小于零")
```

##### 10.函数的参数
1)默认参数
```python
必选参数在前,默认参数在后,否则程序会报错
def staticParam(x,y,n="123"):
	print(”x",x,"y",y,"n",n)
staticParam(1,2)
==>输出结果是x,1 y,2 n,123
staticParam(1,2,3)
==>输出结果是x,1 y,2 n,3
```
2)可变参数
将list和tuple作为函数的参数
```python
//参数为list
def changeParam(param):
	for n in param:
    	print(n);
changeParam([1,2,3,4])

//参数为tuple
def changeParam(param):
	for n in param:
    	print(n);
changeParam((1,2,3,4))

//参数简写
def changeParam(*param):
	for n in param:
    	print(n);
changeParam(1,2,3,4)
```

3)关键字参数
关键字参数允许你传入 0 个或任意个含参数名的参数,这些关键字参数在函数内部自动组装为一个dict
```python
def person(name,age,**kw):
    print("name:",name)
    print("age:",age)
    print("kw:",kw)
person("张三","28",address="北京",phone="1234567890")//关键字的参数也可以不传
person("张三","28")
```