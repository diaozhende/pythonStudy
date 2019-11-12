class Student(object):
    def __init__(self,name):
        self.name = name
    name = "zhangsan"

stu = Student("lisi")
del stu.name
print(stu.name)