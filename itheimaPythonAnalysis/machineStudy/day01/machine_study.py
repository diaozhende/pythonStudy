from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import  CountVectorizer
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
# sklearn数据集的使用
def sklearnDataUse():
    irsiData = load_iris()
    print("莺尾花数据集：\n",irsiData)
    print("查看莺尾花数据集的描述：\n",irsiData["DESCR"])
    print("查看莺尾花数据集特征的名字：\n",irsiData.feature_names)
    print("查看莺尾花数据集特征值：\n",irsiData.data.shape)

    # 数据集的划分 data:特征值，target：目标值
    # x_train:训练集特征值
    # x_test:测试集的特征值
    # y_train:训练集目标值
    # y_test:测试集目标值
    x_train,x_test,y_train,y_test = train_test_split(irsiData.data,irsiData.target,test_size=0.2)
    print("训练集的特征值：\n",x_train,x_train.shape)

# 字典特征抽取
def dict_demo():
    data = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}]
    # 如果sparse=True的话返回的值是one-hot编码，如果是False的话返回稀疏矩阵(返回值在one-hot编码中的位置)，默认值是False
    transfer = DictVectorizer(sparse=True)
    dictData = transfer.fit_transform(data)
    print(dictData.toarray(),type(dictData))
    print("特征名称：\n",transfer.get_feature_names())
    return None

# 文本的特征抽取
def txt_demo():
    data = ["life is short,i like like python", "life is too long,i dislike python"]
    # stop_words:停用词，参数为列表的形式，该列表中的词不会进行特征抽取
    countVectorizer = CountVectorizer(stop_words=["is","too"])
    data_new = countVectorizer.fit_transform(data)
    print(data_new.toarray())
    print("特征名称：",countVectorizer.get_feature_names())
    return None

# jieba分词方法
def jieba_cut(txt):
    data = jieba.cut(txt)
    return " ".join(list(data))

# 使用jieba分词对中文进行分词
def txt_chinese_jieba_demo():
    # data = ["我爱北京天安门","天安门上太阳升"]
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    data_new = []
    for item in data:
       data_new.append(jieba_cut(item))
    countVectorizer = CountVectorizer()
    result = countVectorizer.fit_transform(data_new)
    print(result.toarray())
    print("特征名称：",countVectorizer.get_feature_names())
    return None

# 用TF-IDF的方法进行文本特征抽取
def tf_idf_demo():
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    data_new = []
    for item in data:
        data_new.append(jieba_cut(item))
    tfidf = TfidfVectorizer()
    data_final = tfidf.fit_transform(data)
    print(data_final.toarray())
    print("特征名称：",tfidf.get_feature_names())
    return None

# 标准化
def minmax_demo():
    # 1、读取数据
    data = pandas.read_csv("E:/python大数据资料/黑马-02-最简单快速入门python机器学习/资料/机器学习day1资料/02-代码/dating.txt")
    print(data)
    # 2、实例一个转换器
    transfer = StandardScaler(feature_range=(0,1))
    # 3、调用fit_transform
    data_new = transfer.fit_transform(data)
    print(data_new)
    return None

# 归一化
def stand_demo():
    # 1、读取数据
    data = pandas.read_csv("E:/python大数据资料/黑马-02-最简单快速入门python机器学习/资料/机器学习day1资料/02-代码/dating.txt")
    print(data)
    # 2、实例化一个转换器类
    transfer = MinMaxScaler()
    # 3、调用fit_transform
    data_new = transfer.fit_transform(data)
    print(data_new)
    return None

# 过滤低方差特征
def variance_demo():
    # 1、读取数据
    data = pandas.read_csv("E:/python大数据资料/黑马-02-最简单快速入门python机器学习/资料/机器学习day1资料/02-代码/factor_returns.csv")
    data = data.iloc[:,1:-2]
    # 2、创建一个转换器类
    # threshold:设置阈值，指定方差，当方差在<=时将这些特征过滤掉
    transfer = VarianceThreshold(threshold=10)
    # 3、调用fit_transform
    data_new = transfer.fit_transform(data)
    print(data_new)
    print(data_new.shape)
    return None

# PCA降维
def pca_demo():
    data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]
    # n_components:当数值为小数是表示保留对少数据，当数值为整数的时候表示降低到多少特征
    transfer = PCA(n_components=3)
    data_new = transfer.fit_transform(data)
    print(data_new)
    return None

if __name__ =="__main__":
    # 代码1：sklearn数据集的使用
    sklearnDataUse()
    # 代码2：字典特征抽取
    # dict_demo()
    # 代码3：文本的特征抽取
    # txt_demo()
    # 代码4：使用jieba分词对中文进行分词
    # txt_chinese_jieba_demo()
    # 代码5：用TF - IDF的方法进行文本特征抽取
    # tf_idf_demo()
    # 代码6：标准化
    # minmax_demo()
    # 代码7：归一化
    # stand_demo()
    # 代码8：过滤低方差特征
    # variance_demo()
    # PCA降维
    # pca_demo()