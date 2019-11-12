class Studnet(object):
    def __init__(self,name,score):
        self.__name = name;
        self.score = score;
    def get_name(self):
        return self.__name
    def set_name__(self, name):
        self.__name = name
stu = Studnet("张三","100")
stu.set_name__("李四")

print("姓名:%s"%stu.get_name())