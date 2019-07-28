# python笔记
## 1.list
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
#  直接给指定的数据赋值
list[索引] = "数据内容";
```
5)获取list的元素个数
```python
len(list)
```

## 2.tuple
tuple是一个不可变的元组,tuple一旦被初始化就不能被修改
```python 
#  tuple初始化
text=("1","2","3")#  /当tuple只有一个元素的时候初始化的时候元素后面必须加一个,
text=(1,)

#  /查看元素的值
text[索引]
```

## 3.条件判断
if条件判断格式
```python
if <条件判断1>:
	<执行1>
else:
	<执行else>
    
#  多条件的格式
if <条件判断 1>:
 	<执行 1>
elif <条件判断 2>:
	 <执行 2>
elif <条件判断 3>:
 	<执行 3>
else:
	 <执行 4>

```


## 4.循环
python中的循环有两种,一种是for in迭代循环,另一种是while循环
1)for in 循环
格式:
```python 
for obj in list
列如:
list = ['1','2','3']
for value in list
	print(value)
#  依次输出list的值
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

## 5.dict- - -字典
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
# 通过in判断key是否在这个dictzhong,如果存在返回True,如果不存在返回False
"key" in text
# 通过get方法获取dict的值,如果不存在返回None
text.get("newText")

# get方法获取值当不存在的时候还可以返回指定的值
text.get("newText",-1)
```


## 6.set
set和dict 类似，也是一组key的集合，但不存储value由于key不能重复，所以，在set中,没有重复的key,是无序的
1)创建一个set
```python
demoSet = ([1,2,3,4])
```
2)向set添加数据
```python
#  如果向set中添加重复数据的话，程序不会报错，重复数据会被忽略
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
## 7.replace函数
replace函数是将字符串中的字符进行替换
```python
test = "abcd"
test1 = test.replace("a","A")
```

## 8.函数模块
1)定义函数
```python
#  函数的基本格式
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
#  pass表示展位
def nulFunction():
	pass
#  在if判断中也可以加入pass
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
#  调用函数,函数返回多值实际上就是返回了一个tuple
x,y,z = moreResult(1,2,3)
```
## 9.isinstance函数,类型检查函数
```python
def typeCheck(param):
    if not isinstance(param,(int,float)):
        raise TypeError("参数类型错误")
    if param >0:
        print("参数大于零")
    else:
        print("参数小于零")
```

## 10.函数的参数
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
#  参数为list
def changeParam(param):
	for n in param:
    	print(n);
changeParam([1,2,3,4])

#  参数为tuple
def changeParam(param):
	for n in param:
    	print(n);
changeParam((1,2,3,4))

#  参数简写
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

4)命名关键字参数

通过 `in` 函数判断是否有这个参数

``` python
def personCheck(name, age, **kw):
    if 'address' in kw:
        print("address", kw.get("address"))
personCheck("李四","28",qw="shandong")
```

命名关键字参数来限制关键字参数名称，用*分隔

```python
def function(name,age,*,address,phone):#*号后面的参数视为命名关键字参数
    print("name",name)
    print("age",age)
    print("address",address)
    print("phone",phone)
function("李四","24",address="jinan",phone="123321")#如果传入参数与方法不匹配，程序会报错

#如果命名关键字参数有默认值得话，调用函数的时候也可以不传递命名关键字参数
```

4)参数组合

在python中定义函数，可以用必选参数，默认参数，可变参数，关键字参数和命名关键字参数，其中可变参数和命名关键字参数无法混合，参数的定义顺序是：必选参数，默认参数，可变参数，关键字参数/命名关键字参数。

 ### **注意  ：** *args是可变参数**，**args接收的是一个tuple，**kw是关键字参数，接收的是一个dict。

## 11.递归函数

在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。



## 12.切片

切片就是去一个list和tuple的部分元素，也可以用作字符串的截取

```python
listText = list(range(100)) 
result1 = listText[0:10]# 取前十个元素 :左边的是开始索引，右边的结束索引
result1 = listText[-10:] #取后十个元素，如果从第一个开始取索引是0，那么0可以省略
print(result1)
tupleText = (1,2,3,4,5,6,7,8,9,10)
result2 = tupleText[-5:]
print(result2)
text = "QWERTYUIOP" # 字符串的截取，把字符串看成一个数组，根据索引来对字符串进行截取
result3 = text[-4:]
print(result3)
```

##  13.迭代

迭代就是对一个list和tuple进行遍历，在python中通过for ... in进行迭代

```python
listText = {"第一个key":"第一个value","第二个key":"第二个value","第三个key":"第三个value","第四个key":"第四个value","第五个key":"第五个value"};
# python中默认是通过key进行迭代
for key in listText:
    print(key)

# 迭代value
for value in listText.values():
    print(value)

#迭代字符串
text = "ABCDEFG"
for val in text:
    print(val)

# 判断一个对象是否是可迭代对象
from collections import Iterable
flag = isinstance("123",Iterable)
print(flag)

# 迭代显示索引
userList = ["zhangsan","lisi","wangwu","zhaoliu"]
for i ,t in enumerate(userList):
    print("索引:",i,"值：",t)

 # for循环中同时引用两个变量
userListText = [("zhangsan","jinan"),("lisi","weifang"),("wangwu","qingzhou"),("zhaoliu","qingzhou")]
for x,y in userListText:
    print(x,y)

# 同时迭代dict的key和value
dictList = {"A":"a","B":"b","C":"c"}
for x,y in dictList.items():
    print(x+":"+y)
```



## 14.列表生成式

```python
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
flag = isinstance(text1,str)
print(flag)# 如果是返回True，如果不是返回False

# L1 = ['Hello', 'World', 18, 'Apple', None]   期待输出: ['hello', 'world', 'apple']
L1 = ['Hello', 'World', 18, 'Apple', None]
result = [text for text in L1 if isinstance(text,str)]
print(result)
```



## 15.生成器

这个模块没看明白

## 16.迭代器

```python
it=iter([1,2,3,4,5]);
while True:
    try:
        # 获取下一值
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration异常退出循环
        break
```



## 17.高阶函数

### 1) 变量可以指向函数

```python
# 求绝对值函数
x = abs(-100)
print(x)
# 将函数本身赋值给变量
x1 = abs
print(x1)
# 通过赋值的变量也可以直接调用该变量，跟调用原方法没有区别
x2 = x1(-99)
print(x2)
```

### 2)函数名也是变量名

```python
abs = 10
print(abs)
```

 把 abs 指向 10 后，就无法通过 abs(-10)调用该函数了！因为 abs 这个变量已经不指向求绝对值函数而是指向一个整数 10！当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢复 abs 函数，请重启 Python 交互环境。

**注：由于 abs 函数实际上是定义在__builtin__模块中的，所以要让修改 abs 变量的指向在其它模块也生效，要用      `__builtin__.abs = 10`**

### 3)传入函数

将函数当做函数的参数传入到另一个函数中

```python
f = abs
def function(x,y,z):
    print("X:",z(x))
    print("Y:",z(y))

function(-100,-200,f)
```



## 18.map和reduce

### 1)map

```python
# 得到list中每个元素的平方值
def function(x):
    return x*x
listText = [1,2,4,5,6,7,8,9]
result1 = map(function,listText)
print(list(result1))

# 将int转换成str
listText = [1,2,4,5,6,7,8,9]
result2 = map(str,listText)
print(list(result2))
```



### 2)reduce

```python
# 将str序列转换成int整数
from functools import reduce
def fn(x,y):
    return x*10+y
def paramNum(s):
    return s
s = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'7': 7, '8': 8, '9': 9}
result5 = reduce(fn,map(paramNum,s))
print(result5)
# 输出结果:12456789

# 利用lambda函数进行简化
from functools import reduce
def str2int():
    return reduce(lambda x,y:x*10+y,map(paramNum,s))
result6 = str2int()
print(result6)
```

### 章节练习

```python
# 输入：['adam', 'LISA', 'barT']，输出：['Adam','Lisa', 'Bart']
listTextChange1 = ['adam', 'LISA', 'barT']
def change(x):
    text = x.title()
    return text
result7 = map(change,listTextChange1)
print(list(result7))


# 请编写一个 prod()函数，可以接受一个 list 并利用 reduce()求积
listNum = [1,2,3,4,5,6]
def functionResult(x,y):
    return x*y
def listResult(list):
    return list
result8 = reduce(functionResult,map(listResult,listNum))
print(result8)
```



## 19.sorted 排序函数

```python
# 从小到大排序
listText=[45,-10,1,35,-89]
result = sorted(listText)
print(result)
# 从大到小排序
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
```



### 章节练习

```python
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 根据名字进行排序
nameList = []
def by_name(t):
    for key,value in t:
        nameList.append(key)
nameResult = sorted(nameList,key=by_name(L))
print(nameResult)

# 根据分数进行排序
scoreList = []
def by_score(t):
    for key,value in t:
        scoreList.append(value)
scoreResult = sorted(scoreList,key=by_score(L))
print(scoreResult)
```



## 20.返回函数

将函数当做返回值进行返回

```python
# 返回求和函数
def calc_num(*args):
    def sum():
        ax = 0
        for num in args:
            ax = ax + num
        return ax
    return sum

result = calc_num(1,2,3,4,5,6)
print(result())
```

### 闭包

在函数 lazy_sum 中又定义了函数 sum，并且，内部函数 sum 可以引用外部函数 lazy_sum 的参数和局部变量，当 lazy_sum 返回函数 sum 时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

## 21.匿名函数

拿计算f(x) = x²

```python
 list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#输出结果:[1, 4, 9, 16, 25, 36, 49, 64, 81]

#匿名函数相当于
#def f(x):
# return x * x
# 关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数，匿名函数有个限制，就是只能有一个表达式，不用写 return，返回值就是该表达式的结果。
```



##  22.装饰器

```python
# 在函数调用前后打印日志
def log(text):
    def decorator(func):
        @functools.wraps(func) # 把原始函数的__name__等属性复制到 wrapper()函数中
        def wrapper(*args,**kw):
            print("%s  %s()"%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
```



## 23.偏函数

### 1) int转换函数

```python
# int转换函数
text = '12345'
result = int(text) # 默认是转换十进制 可以简写成result = int(text,8)
result = int(text,base=8)# 转换八进制
result = int(text,base=16)# 转换十六进制
result = int("1010101",base=2)# 转换二进制
```

### 2)偏函数

functools.partial 就是帮助我们创建一个偏函数的，不需要我们自己定义 int2()，可以直接使用下面的代码创建一个新的函数 int2

```python
import functools
int2 = functools.partial(int, base=2)
int2('1000000')
# 输出结果:64 
```



所以，简单总结 functools.partial 的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

`总结：当函数的参数个数太多，需要简化时，使用 functools.partial 可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。`

## 24.模块

python中每一个.py文件就是一个模块

### 1)包

包的目录下有一个__init__.py文件，这个问价是必须存在的，如果不存在就是一个普通的目录

### 2)使用模块

python中有很多模块，要使用模块之前要进行安装

##### 安装模块命令

```shell
pip install 模块名
```

##### 引入模块代码

```python
import 模块名
```

##### 实例代码

```python
_author_ = 'Michael Liao'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello %s!"% args[1])
    else :
        print("Too many arguments!")
test()
```

### 3)作用域

一般的变量和方法都是公开的(public)，以下划线开头的变量(例：password)和方法(例：login())是私有的(private)，我们不应该直接调用这些私有的变量和方法，调用程序也是不会报错的。

### 4)安装第三方模块

在 Python 中，安装第三方模块，是通过包管理工具 pip 完成的。

```shell
# 安装Pillow
pip3 install Pillow
```



## 25.面向对象编程

```python
class studnet(object): #object表示继承的类
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:%s" %(self.name,self.score))

zhangsan = studnet("zhangsan","100")
zhangsan.print_score()
```



## 26.类和实例

类（class），实例（Instance）

```python
# 创建类的格式及使用
class Student(object)  #object表示继承的类
	def __init__(self,name.score) # 类的属性，相当于java类中的构造函数，
    	self.name = name #赋值
        self.score = score
    def print_score()： # 类中封装的方法
    	print("%s:%s" %(self.name,self.score))
#创建对象，调用类中封装的方法
stu = Student("lisi","99") 
stu.print_score();


# self永远在第一个，创建对象的时候不用传递该参数，Python 解释器自己会把实例变量传进去 表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到 self，因为 self就指向创建的实例本身
```

## 27.访问限制

在python中，class类中的属性分为以下几种：

### 1）__name（两个下划线开头）

这个表示私有变量，在外部直接访问程序会报错，通过get和set方法来进行操作

```python
class Studnet(object):
    def __init__(self,name,score):
        self.__name = name;
    def get_name(self):
        return self.__name
    def set_name__(self, name):
        self.__name = name
stu = Studnet("张三","100")
stu.set_name__("李四")

print("姓名:%s"%stu.get_name())
```



### 2）_name（一个下划线开头）

这个是外部可以直接访问的，虽然不报错，但是我们把它看做是私有变量，不能随意访问。



### 3） ` __name__`    两个下划线开头和结尾

变量名类似 `__xxx__` 的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是 private 变量，所以，不能用__name__、__score__这样的变量名

## 28.继承和多态

### 1）继承

```python
class Animal(object):
     def out(self):
         print("Animal run...")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
class Cat(Animal):
    def __init__(self,name):
        self.name = name
dog = Dog("Dog")
dog.out();
```



### 3）多态

```python
class Animal(object):
     def out(self):
         print("Animal run...")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def out(self):
        print("Dog run...")

class Cat(Animal):
    def __init__(self,name):
        self.name = name

    def out(self):
        print("Cat run...")
animal = Animal()
def run_twice(animal):
    animal.out()
run_twice(Dog("name"))
# 输出结果:Dog run...
run_twice(Cat("name"))
# 输出结果：Cat run...
```



## 29.获取对象信息

### 1）type()

```python
print(type(1)==int)
# 如果是输出True，如果不是输出False


# 使用type判断一个对象是否是函数
import types
def test():
    pass
print(type(test) == types.FunctionType)
print( type(abs)==types.BuiltinFunctionType)
print( type(lambda x: x)==types.LambdaType)
print( type((x for x in range(10)))==types.GeneratorType)
```



### 2）isinstance

```python
isinstance(h, Husky)
# 判断是否是某个对象，如果是为True，如果是为False

isinstance('a', str)
isinstance(123, int)
isinstance(b'a', bytes)
isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))

```



### 3）dir()

如果要获得一个对象的所有属性和方法，可以使用 dir()函数，它返回一个包含字符串的 list，比如，获得一个 str 对象的所有属性和方法：

```python
dir("ABC")
```



类似`__xxx__`的属性和方法在 Python 中都是有特殊用途的，比如`__len__`方法返回长度。在 Python 中，如果你调用 len()函数试图获取一个对象的长度，实际上，在 len()函数内部，它自动去调用该对象的`__len__()`方法，所以，下面的代码是等价的：

```python
 len('ABC')
'ABC'.__len__()
```



#### 常用函数

```python
class MyObject(object):
    def __init__(self):
        self.x = 9
        def power(self):
            return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))  # 有属性'x'吗？
print(obj.x) # 获取属性'x'
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(setattr(obj, 'y', 19))  # 设置一个属性'y'
print(hasattr(obj, 'y') ) # 有属性'y'吗？
print(getattr(obj, 'y'))  # 获取属性'y'
print(obj.y ) # 获取属性'y'

getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值 404
 fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量 fn
```



## 30.实例属性和类属性

```python
class Student(object):
    name = "zhangsan"
stu = Student()
print(stu.name) # 输出结果：zhangsan
print(Student.name) # 输出结果：zhangsan

class Student(object):
    def __init__(self,name):
        self.name = name
    name = "zhangsan"
stu = Student("lisi")
print(stu.name) # 输出结果：lisi

class Student(object):
    def __init__(self,name):
        self.name = name
    name = "zhangsan"
stu = Student("lisi")
del stu.name
print(stu.name) # 输出张三
```

**从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性**



## 31.面向对象高级编程

### 1）使用`__slots__`

通过代码给类中的实例属性添加一个方法

```python

```



## 32.多重继承



## 33.定制类

看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python 中是有特殊用途的

### 1）`__str__`

这个方法相当于java中toString方法

```python
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "name实例的值为:%s"%self.name
stu = Student("111")
print(stu)
```



### 3）`__iter__` 循环对象

```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器 a，b
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration();
        return self.a  # 返回下一个值
for n in Fib():
    print(n)
```



### 4）`__getitem__` 通过下标取出元素



## 34.枚举

```python
from enum import Enum,unique
@unique
class Weekday(Enum):
    Sun = 0  # Sun 的 value 被设定为 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Mon.value)
print(Weekday.Mon == Weekday.Thu)
```

## 35.使用元类



## 36.错误、调试和测试

### 1）错误处理

这里说的错误处理就是捕获异常

```python
try:
    ....
except Exception as e:
    ...
finally:
    
# 例如
def testException(num):
    try:
        result = 100/num
    except Exception as e:
        print("Error:",e)
    print(result)
testException(0)
    
```

### 2）调用堆栈

python解释器打印异常信息

### 3）记录错误

Python 内置的 logging 模块可以非常容易地记录错误信息

```python
import logging
def testException(num):
    try:
        result = 100/num
    except Exception as e:
        logging.exception(e)
    print(result)
testException(0)
```

这个方法同样是打印错误，但是程序会继续执行，不会退出。



### 3）抛出错误

如果要抛出错误，首先定义一个错误类，选择好继承的错误，然后，用raise语句抛出一个错误

```python
class Error(ValueError):
    print("出现错误")

def foo(s):
    n = int(s)
    if n==0:
        raise Error('invalid value: %s' % s)
    return 10/n
foo(0)
```

### 4）调试

#### （1）断言

凡是用 print()来辅助查看的地方，都可以用断言（assert）来替代

```python

def foo(s):
    n = int(s)
    assert n != 0,'n is zero'
    return 10/n
foo(0)
```

assert 的意思是，表达式 n != 0 应该是 True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，assert 语句本身就会抛出 AssertionError

启动 Python 解释器时可以用-O 参数来关闭 assert，关闭后，你可以把所有的 assert 语句当成 pass 来看。

#### （2）logging

这就是 logging 的好处，它允许你指定记录信息的级别，有 debug，info，warning，error 等几个级别，当我们指定 level=INFO 时，logging.debug就不起作用了

```python
import logging
logging.basicConfig(level=logging.INFO) #指定记录信息级别
def foo(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10/n
foo(0)
```



## 37.IO编程

IO编程分为同步和异步，向外发送数据是OutputStream，接受数据是InputSteam



## 38.文件读写

### 1）读取文件

```python
# open表示打开一个文件，当成功打开一个文件，用read和readlines函数读取文件内容
readFile = open("D:/pythonFile.txt","r",encoding="UTF-8") # r表示读 encoding编码 
txt = readFile.read()
print(txt)
readFile.close()
# 在操作文件的时候最后要关闭文件流
```

可以利用with函数，当读取完文件的时候程序自动调用close方法

```python
with open("D:/pythonFile.txt","r",encoding="UTF-8") as f:
    print(f.read())
```

### 2）写文件

```python
f = open("D:/pythonFile.txt", "w") # 以写的方式打开一个文件,也可以用‘wb’的方式打开
f.write("这是python写入文件的内容") # 这是写入文件的内容
f.close() # 关闭文件流
```

也可以用with函数

```python
with open("D:/pythonFile.txt", "w") as  f:
    f.write("这是用with函数写入的内容")
```

## 39.StringIO和BytesIO

### 1）StringIO

StringIO就是从内存中读取文件

要把 str 写入 StringIO，我们需要先创建一个 StringIO，然后，像文件一样写入即可

```python
from io import StringIO
f = StringIO() # 创建StringIO对象
f.write("hello") # 向内存中写入内容
f.write("  ")
f.write("world")
print(f.getvalue()) # 获取内存中的内容

# StringIO初始化内容
f = StringIO("StringIO初始化")
print(f.getvalue()) # 获取内存中的内容
```

### 2）BytesIO

BytesIO和StringIO操作是类似的

```python
from io import BytesIO
b = BytesIO() # 创建BytesIO对象
b.write("中文".encode("UTF-8")) # 写入经过 UTF-8 编码的 bytes
print(b.getvalue())

# 初始化BytesIO
 f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
 f.read() # 读取内容
```



## 40.操作文件和目录

### 1）获取是什么操作系统

```python
import os
print(os.name)
# 如果是 posix，说明系统是 Linux、Unix 或 Mac OS X，如果是 nt，就是 Windows系统
```

### 2）环境变量

```python
os.environ
# 查看系统变量
os.environ.get('PATH')
# 查看系统中的某一个变量
```

### 3）操作文件和目录

#### （1）操作目录

```python
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
# 把两个路径合成一个时，不要直接拼字符串，而要通过 os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
path = os.path.join("D:/pythonFile","test1File")
print(path)
# 创建一个目录
os.mkdir(path)
# 删除一个目录
os.rmdir(path)


#要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
fileName = os.path.split("D:/pythonFile/test1File/file1.txt")
print(fileName)
# >>>('D:/pythonFile/test1File', 'file1.txt')
# 获取文件的扩展名
fileType = os.path.splitext("D:/pythonFile/test1File/file1.txt")
print(fileType)
# >>>('D:/pythonFile/test1File/file1', '.txt')
```



#### （2）操作文件

```python
# 假定当前目录下有一个 test.txt 文件
# 对文件重命名:
 os.rename('test.txt', 'test.py')
# 删除文件
os.remove('test.py')
```

#### （3）python过滤文件

```python
# 要列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]
# 要列出所有的.py 文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
```



## 41.序列化

### 1）序列化与反序列化

```python
# 将一个对象序列化后写入一个文件
import pickle
d = dict(name="zhangsan",age = 18,address = "shandong")
f = open("D:\\pythonFile\\test1File\\file1.txt","wb")
pickle.dump(d,f)
f.close()

# 将文件中的内容读出来，进行反序列化
r = open("D:\\pythonFile\\test1File\\file1.txt", "rb")
result = pickle.load(r)
r.close()
print(result)
```

###  2）JSON

#### （1）将数据转换成json

```python
text = dict(name="zhangsan", age=18, address="shandong")
print(json.dumps(text))

# 将一个class对象转换成json
# 首先将一个class对象转换成dict，然后再转换成json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student("zhangsan",18,100)
jsonText = json.dumps(s,default=lambda obj:obj.__dict__)
print(jsonText)
```



#### （2）将json数据反序列化

```python
# 将json数据转换成class对象
jsonText = {"name": "zhangsan", "age": 18, "score": 100}
objText = json.loads(jsonText,object_hook=lambda d:Student(d["name"],d["age"],d["score"]))
print(objText)
```



## 42.线程和进程（后续学习）



## 43.正则表达式

```python
import re
if re.match(r'正则表达式', test):
	print('ok')
else:
	print('failed')
# match()方法判断是否匹配，如果匹配成功，返回一个 Match 对象，否则返回 None
```





## 44.常见的内建模块

### 1）datetime

```python
# 获取当前时间
from datetime import datetime
now = datetime.now()
print(now)

# 获取指定日期和时间
dt = datetime(1997,5,5,15,55,55)
print(dt)
```



### 2）将datetime转换成timestamp

```python
dt = datetime(1997,5,5,15,55,55)
print(dt.timestamp())
```

### 3）将timestamp 转换成datetime

```python
t = 1429417200.0
print(datetime.fromtimestamp(t))
```

### 4）str 转换成 datetime

```python
from datetime import datetime
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
```

### 5)datetime 转换成str

```python
from datetime import datetime
nowTime = datetime.now()
print(now.strftime("%a %b %d %H:%M"))
```

### 6)datetime的计算

```python
from datetime import datetime,timedelta
now = datetime.now()
print("现在的时间为：",now)
resultNow = now+timedelta(hours=10)
resultNow1 = now + timedelta(days=2, hours=12)
print("现在的时间为：",resultNow)
print("第二次计算的时间为：",resultNow1)
```



## 45.collections

collections 是 Python 内建的一个集合模块，提供了许多有用的集合类。



## 46.Base64

Base64解码

```python
import base64
base64.b64encode(b'binary\x00string')
#>>>输出结果：b'YmluYXJ5AHN0cmluZw=='
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
#>>>输出结果：b'binary\x00string'
```



