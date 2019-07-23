# 1.默认参数
# def staticParam(param1,n=321):
#     print("参数1",param1,"默认参数:",n)
# staticParam(123)
#
# def enroll(name,age,city="beijing"):
#     print("name",name)
#     print("age",age)
#     print("city",city)
# enroll("张三",28);


# def add_end(L=[]):
#     L.append("END")
#     print(L)
# add_end([1,2,3])
# add_end(["x","y","z"])
# add_end()

# def changeParam(*param):
#     for n in param:
#         print(n);
# changeParam(1,2,3,4)
# list=[1,23,4]
# def changeParam(*param):
#     for n in param:
#         print(n);
# changeParam(list)

def person(name,age,**kw):
    print("name:",name)
    print("age:",age)
    print("kw:",kw)
person("张三","28",address="北京",phone="1234567890")
person("张三","28")