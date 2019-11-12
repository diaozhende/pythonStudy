# BP人工神经网络的实现
# 1、读取数据
# 2、keras.models Sequential   /keras.layers.core Dense Activation
# 3、Sequential建立模型
# 4、Dense建立层
# 5、Activation激活函数
# 6、compile模型编译
# 7、fit训练（学习）
# 8、验证（测试，分类预测）
import pandas
import numpy
from keras.models import Sequential
from keras.layers.core import Dense,Activation

# 1、读取数据
lessonData = pandas.read_csv("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第9周/lesson.csv", encoding="gbk")
xData = lessonData.iloc[:, 1:5].as_matrix()
yData = lessonData.iloc[:, 5].as_matrix()
for i in range(0, len(xData)):
    for j in range(0, len(xData[i])):
        thisData = xData[i][j]
        if (thisData == "是" or thisData == "多"or thisData == "高"):
            xData[i][j] = int(1)
        else:
            xData[i][j] = int(-1)

for k in range(0, len(yData)):
    if (yData[k] == "高"):
        yData[k] = int(1)
    else:
        yData[k] = int(-1)

# 将数据转换成数据框
xf = pandas.DataFrame(xData)
yf = pandas.DataFrame(yData)
# 将数据框的数据类型转换成int类型
xLesson = xf.as_matrix().astype(int)
yLesson = yf.as_matrix().astype(int)

# 3、Sequential建立模型
model = Sequential()
# 4、Dense建立输入层
model.add(Dense(10, input_dim=len(xLesson[0])))  # 10:输入层的层数，input_dim:自变量数据的维度
# 5、Activation设置激活函数
model.add(Activation("relu"))
# 输出层
model.add(Dense(1, input_dim=1))  # 1:输出层的层数，input_dim:输出数据的维度
# 激活函数
model.add(Activation("sigmoid"))
# 6、模型编译
# loss:损失函数(binary_crossentropy这个为二元分类的损失函数，mean_squared_error多元损失函数)，
# optimizer:求解方法，
# class_mode:模式(binary:二元)
model.compile(loss="binary_crossentropy", optimizer="adam")
#7、训练数据
# nb_epoch:学习次数
# batch_size:批大小
model.fit(xLesson,yLesson,nb_epoch=1000,batch_size=100)
# 8、预测分类
# reshape函数中如果有一个参数就是一维，如果有两个参数就是二维，len(x)表示结果又多少个值
str = model.predict_classes(xLesson).reshape(len(xLesson))
params = numpy.array([[1,-1,-1,1],[1,1,1,1],[-1,1,-1,1]])
result = model.predict_classes(params).reshape(len(params))
x = 0
print(len(yLesson))
for i in range(0,len(xLesson)):
    if (str[i] != yLesson[i]):
        x+=1
res = 1-x/len(xLesson)
print("正确率：%s"%res)
for item in result:
    if(item == 1):
        print("销量高")
    elif(item == 0):
        print("销量低")



