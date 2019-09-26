import numpy
class bayes:
    # 初始化
    def __init__(self):
        self.length = -1
        self.labelcount = dict()
        self.vectorcount = dict()
    # 数据训练
    def fit(self,testData:list,labels:list):
        if(len(testData) != len(labels)):
            raise ValueError("您输入的测试数组跟类别数据长度不一致")
        self.length = len(testData[0]) # 测试数组的长度
        labelsCount = len(labels) # 所有类别的数量
        notLabelsCount = set(labels) # 不重复类别的数量
        for item in notLabelsCount:
            self.labelcount[item] = labels.count(item)/labelsCount # 计算当前类别占总类别的比例
        for vector,label in zip(testData,labels):
            if(label not in self.vectorcount):
                self.vectorcount[label] = []
            self.vectorcount[label].append(vector)
        print("训练结束")
        return self

    def bayesTest(self,TestData,labelsSet):
        if(self.length == -1):
            raise ValueError("您还没有进行训练，请先训练")
        lbDict = dict()
        for thislb in labelsSet:
            p = 1
            allLabel = self.labelcount[thislb]
            allvector = self.vectorcount[thislb]
            vnum = len(allvector)
            allvector = numpy.array(allvector).T
            for index in range(0,len(TestData)):
                vector = list(allvector[index])
                p*=vector.count(TestData[index])/vnum
            lbDict[thislb] = p*allLabel
        labels = sorted(lbDict,key=lambda x:lbDict[x],reverse=True)
        return labels
