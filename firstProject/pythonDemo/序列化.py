import pickle

d = dict(name="zhangsan", age=18, address="shandong")
# D:\pythonFile\test1File
# f = open("D:\\pythonFile\\test1File\\file1.txt","wb")
# pickle.dump(d,f)
# r = open("D:\\pythonFile\\test1File\\file1.txt", "rb")
# result = pickle.load(r)
# r.close()
# print(result)

# json
import json

text = dict(name="zhangsan", age=18, address="shandong")
print(json.dumps(text))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student("zhangsan",18,100)
jsonText = json.dumps(s,default=lambda obj:obj.__dict__)
print(jsonText)

objText = json.loads(jsonText,object_hook=lambda d:Student(d["name"],d["age"],d["score"]))
print(objText)