import pandas
import numpy

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
print(xf)
print(yf)
# 将数据框的数据类型转换成int类型
xI = xf.as_matrix().astype(int)
yI = yf.as_matrix().astype(int)
from sklearn.tree import DecisionTreeClassifier
# 创建决策树对象
dtc = DecisionTreeClassifier(criterion="entropy")
# 训练数据
dtc.fit(xI,yI)
# 可视化决策树
# dot文件转换命令：dot -Tpng dot文件名+.文件类型 -o 要转换成的文件名+.文件类型
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第9周/lessontree.dot","w") as file:
    file = export_graphviz(dtc,feature_names=["shizhan","keshishu","cuxiao","ziliao"],out_file=file)


# 预测销量高低
testData = numpy.array([[1,-1,1,1],[1,-1,-1,1],[1,11,1,1]])
reslut = dtc.predict(testData)
print(reslut)