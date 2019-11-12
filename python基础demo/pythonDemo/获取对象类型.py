# 1。type()函数
# print(type(1) == int)

# 使用type判断一个对象是否是函数
import types


def test():
    pass


# print(type(test) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# print(type(lambda x: x) == types.LambdaType)
# print(type((x for x in range(10))) == types.GeneratorType)


# 2.isinstance()函数


class MyObject(object):
    def __init__(self):
        self.x = 9

        def power(self):
            return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))  # 有属性'x'吗？
print(obj.x)
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(setattr(obj, 'y', 19))  # 设置一个属性'y'
print(hasattr(obj, 'y') ) # 有属性'y'吗？
print(getattr(obj, 'y'))  # 获取属性'y'
print(obj.y ) # 获取属性'y'
