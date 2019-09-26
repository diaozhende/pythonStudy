from numpy import *
import operator


# knn算法：原理就是计算出测试数据的坐标到每一个训练数据坐标的距离(公式：((x1-x2)²+(y1-y2)²)开方)，
# 通过k来制定选取的点，判断这些点都是属于哪些类别，哪个类别的点多，测试数据就属于哪个类别

# K:选取点的个数
# testData:测试数据
# trainData：训练数据
# labes：类别
def knn(k, testData, trainData, labes):
    # 将测试数据和训练数据扩展成同纬度
    # shape返回值（行，列）
    trainDataSize = trainData.shape[0]
    # tile(数组,重复次数)：从列的方向扩展，增加列
    # tile(数组,(重复次数,1))：从行的方向进行扩展，增加行
    tileTestData = tile(testData, (trainDataSize, 1))
    # 求测试数据和训练数据的差值,进行平方
    sqdif = (tileTestData - trainDataSize) ** 2
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
