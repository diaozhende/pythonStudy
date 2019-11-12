def test(x):
    print(x)

test("这是一个函数。。。")

def typeCheck(param):
    if not isinstance(param,(int,float)):
        raise TypeError("参数类型错误")
    if param >0:
        print("参数大于零")
    else:
        print("参数小于零")
typeCheck(-123)

def moreResult(x,y,z):
	return x,y,z
x,y,z = moreResult(1,2,3)
print(x,y,z)

import math
