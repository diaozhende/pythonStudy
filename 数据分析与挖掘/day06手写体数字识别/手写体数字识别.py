from numpy import *
import operator
from os import listdir


def knn(k, testData, trainData, labels):
    traindatasize = trainData.shape[0]
    dif = tile(testData, (traindatasize, 1)) - trainData
    sqdif = dif ** 2
    sumsqdif = sqdif.sum(axis=1)
    distance = sumsqdif ** 0.5
    sortdistance = distance.argsort()
    count = {}
    for i in range(0, k):
        vote = labels[sortdistance[i]]
        count[vote] = count.get(vote, 0) + 1
    sortcount = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    return sortcount[0][0]


# 读取图片
from PIL import Image

im = Image.open("C:/Users/diaozhende/Desktop/three.png")
fh = open("C:/Users/diaozhende/Desktop/three.txt", "a")
# im.save("C:/Users/me/Pictures/weixin.bmp")
width = im.size[0]
height = im.size[1]
# k=im.getpixel((1,9))
# print(k)
for i in range(0, width):
    for j in range(0, height):
        cl = im.getpixel((i, j))
        clall = cl[0] + cl[1] + cl[2]
        if (clall == 0):
            # 黑色
            fh.write("1")
        else:
            fh.write("0")
    fh.write("\n")
fh.close()


# 加载数据
def datatoarray(fname):
    arr = []
    fh = open(fname)
    for i in range(0, 32):
        thisLine = fh.readline()
        for j in range(0, 32):
            arr.append(int(thisLine[j]))
        return arr


# 建立一个函数去文件名的前缀
def seplabel(fname):
    fileStr = fname.split(".")[0]
    label = int(fileStr.split("_")[0])
    return label


# 建立训练数据
def trainData():
    labels = []
    trainFile = listdir("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/data/traindata/")
    trainNum = len(trainFile)
    print(trainNum)
    trainarr = zeros((trainNum, 1024))
    for i in range(0, trainNum):
        thisfname = trainFile[i]
        thislabel = seplabel(thisfname)
        labels.append(thislabel)
        trainarr[i, :] = datatoarray("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/data/traindata/" + thisfname)
    return trainarr, labels


def testData():
    trainarr, labels = trainData()
    testFile = listdir("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/data/testdata/")
    testNum = len(testFile)
    for i in range(0, testNum):
        thisTestFile = testFile[i]
        testDataArr = datatoarray("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第7周/data/testdata/" + thisTestFile)
        rknn = knn(3, testDataArr, trainarr, labels)
        print(rknn)


testData()
