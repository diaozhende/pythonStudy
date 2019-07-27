class Student(object):
    def __init__(self,name):
        self._name = name

stu = Student("zhangsan")
from types import MethodType


def set_name(self,name):
    self.name = name


stu.set_name = MethodType(set_name,stu)
print(stu._name)