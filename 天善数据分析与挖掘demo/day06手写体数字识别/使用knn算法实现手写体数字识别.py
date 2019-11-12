from numpy import *
import operator
from os import listdir

def knn(k, testData, trainData, labes):
    # 将测试数据和训练数据扩展成同纬度
    # shape返回值（行，列）
    trainDataSize = trainData.shape[0]
    # tile(数组,重复次数)：从列的方向扩展，增加列
    # tile(数组,(重复次数,1))：从行的方向进行扩展，增加行
    tileTestData = tile(testData, (trainDataSize, 1))
    # 求测试数据和训练数据的差值,进行平方
    sqdif = (tileTestData - trainData) ** 2
    # 进行每行求和
    sumsqdif = sqdif.sum(axis=1)
    # 进行开放
    distance = sumsqdif ** 0.5
    # 将结果进行排序（升序）,返回的是值得下标
    sortDistance = distance.argsort()
    # 定义一个空字典，遍历结果，如果结果在字典中不存在，将结果添加到字典中，如果结果存在将此结果的计数+1
    count = {}
    for i in (0, k):
        labeName = labes[sortDistance[i]]
        count[labeName] = count.get(labeName, 0) + 1

    # 将字典进行降序排序
    # count.items()：排序的数据
    # operator.itemgetter(1)：依据那个进行排序(依据[("item1",1),("item2",2)]依据1这个列进行排序)
    # reverse:默认是升序的，True为降序
    result = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    return result[0][0]

# 图片处理
# from PIL import Image
# image = Image.open("C:/Users/diaozhende/Desktop/three.png")
# file = open("C:/Users/diaozhende/Desktop/three")
# width = image.size[0]
# height = image.size[1]
# for i in range(0,width):
#     for j in range(0,height):
#         color = image.getpixel((i,j))
#         call = color[0]+color[1]+color[2]
#         if(call == 0):
#             file.write("1")
#         else:
#             file.write("0")
#     file.write("\n")
# file.close()

# 加载数据
def dataToArray(path):
    arr = []
    file = open(path)
    for i in range(0,32):
        thisLine = file.readline()
        for j in range(0,32):
            arr.append(int(thisLine[j]))
    return arr

# 获取文件名前缀
def seplabel(fileName):
    fname = fileName.split(".")[0]
    labelName = int(fname.split("_")[0])
    return labelName

# 建立训练数据
def trainData():
    labels=[]
    # 获取文件夹下所有的文件名
    fileNameList = listdir("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/data/traindata/")
    count = len(fileNameList)
    # 长度为1024列，每一行存一个文件
    # 用一个数组存储所有的训练数据，行：文件总数，列：1024
    # zeros:方法是生成一个多少行，多少列的数组
    trainArr = zeros((count,1024))
    for i in range(0,count):
        thisFileName = seplabel(fileNameList[i])
        labels.append(thisFileName)
        trainArr[i,:] = dataToArray("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/data/traindata/"+fileNameList[i])
    return trainArr,labels

def dataTest():
    trainArr,labels = trainData()
    testDataFileNameList = listdir("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/data/testdata/")
    for i in range(0,len(testDataFileNameList)):
        print(testDataFileNameList[i])
        testDataArr = dataToArray("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/data/testdata/"+testDataFileNameList[i])
        result = knn(10,testDataArr,trainArr,labels)
        print(result)

# dataTest()
# C:\Users\diaozhende\Desktop
# 图片处理
from PIL import Image
image = Image.open("C:/Users/diaozhende/Desktop/three.jpg")
file = open("C:/Users/diaozhende/Desktop/three.txt","a")
im_rotate = image.rotate(90)
im = im_rotate.transpose(Image.FLIP_TOP_BOTTOM)
width = im.size[0]
height = im.size[1]
for i in range(0,width):
    for j in range(0,height):
        color = im.getpixel((i,j))
        call = color[0]+color[1]+color[2]
        if(call == 0):
            file.write("1")
        else:
            file.write("0")
    file.write("\n")
file.close()
trainArr,labels = trainData()
testDataArr = dataToArray("C:\\Users\\diaozhende\\Desktop\\three.txt")
result = knn(10, testDataArr, trainArr, labels)
print(result)


