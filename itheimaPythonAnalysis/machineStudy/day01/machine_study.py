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
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,SGDRegressor,Ridge
from sklearn.metrics import mean_squared_error

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

# 用knn算法对鸢尾花数据集进行分类
def knn_iris():
    # 1、获取数据
    irisData = load_iris()
    # 2、划分数据集
    x_train,x_test,y_train,y_test = train_test_split(irisData.data,irisData.target,random_state=10)
    # 3、特征工程(标准化)
    trainfer = StandardScaler()
    x_train = trainfer.fit_transform(x_train)
    x_test = trainfer.transform(x_test)
    # 4、knn算法预估器
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(x_train,y_train)
    # 5、模型评估
    # 方法1：直接对比真实值和预估值
    x_predict = knn.predict(x_test)
    print("x_predict:\n",x_predict)
    print("直接对比真实值和预估值:\n",y_test == x_predict)
    # 方法2：计算准确率
    score = knn.score(x_test,y_test)
    print("准确率：",score)
    return None

# 用knn算法对鸢尾花数据集进行分类,加上网格搜索和交叉验证
def knn_iris_gscv():
    # 1、获取数据
    irisData = load_iris()
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(irisData.data, irisData.target, random_state=10)
    # 3、特征工程(标准化)
    trainfer = StandardScaler()
    x_train = trainfer.fit_transform(x_train)
    x_test = trainfer.transform(x_test)
    # 4、knn算法预估器
    knn = KNeighborsClassifier()
    # 添加网格搜索和交叉验证
    # 参数准备
    param_dict = {"n_neighbors": [1, 3, 5, 7, 9, 11]}  # knn中的k值，批量验证哪个k值最佳
    # cv:进行几折交叉验证
    knn = GridSearchCV(knn, param_grid=param_dict, cv=10)
    knn.fit(x_train, y_train)

    # 5、模型评估
    # 方法1：直接对比真实值和预估值
    x_predict = knn.predict(x_test)
    print("x_predict:\n", x_predict)
    print("直接对比真实值和预估值:\n", y_test == x_predict)
    # 方法2：计算准确率
    score = knn.score(x_test, y_test)
    print("准确率：", score)
    # 最佳参数：best_params_
    print("最佳参数：",knn.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：",knn.best_score_)
    # 最佳估计器：best_estimator
    print("最佳估计器：",knn.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果：",knn.cv_results_)
    return None

# 用朴素贝叶斯算法进行对新闻进行分类
def nb_news():
    # 1、获取数据
    # data_home:指定数据的下载目录
    # subset:数据类型，all(测试集和训练集)，train(训练集),test(测试集)
    news_data = fetch_20newsgroups(data_home="D:/news/",subset="all")
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(news_data.data,news_data.target)
    # 3、特征工程，文本特征抽取-tfidf
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4、贝叶斯算法预估器流程
    nb = MultinomialNB(alpha=1.0)
    nb.fit(x_train,y_train)
    # 5、模型评估
    # 方法一：直接比对真实值和预测值
    x_predict = nb.predict(x_test)
    print("x_predict:\n",x_predict)
    print("直接比对真实值和预测值:\n",x_predict == y_test)
    # 方法二：计算准确率
    score = nb.score(x_test,y_test)
    print("准确率：",score)
    return None

# 使用决策树对鸢尾花进行分类
def tree_iris():
    # 1、获取数据
    iris_data = load_iris()
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris_data.data,iris_data.target,random_state=22)
    # 3、决策树预估器
    tree = DecisionTreeClassifier(criterion="entropy")
    tree.fit(x_train,y_train)
    # 模型评估
    # 方法一：直接比对真实值和预测值
    x_predict = tree.predict(x_test)
    print("x_predict:\n",x_predict)
    print("比对真实值和预测值:\n",x_predict == y_test)
    # 方法二：计算准确率
    score = tree.score(x_test,y_test)
    print("准确率：",score)
    return None
# 使用正规方程来预测波士顿房价
def liner1():
    # 1、获取数据
    bostonData = load_boston()
    # 2、划分数据集
    x_train,x_test,y_train,y_test = train_test_split(bostonData.data,bostonData.target,random_state=22)
    # 3、特征工程：进行标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4、预估器
    liner = LinearRegression()
    liner.fit(x_train,y_train)
    # 5、得出模型
    print("正规方程-权重系数：",liner.coef_)
    print("正规方程-偏置：",liner.intercept_)
    # 6、模型评估
    x_predict = liner.predict(x_test)
    print("预测房价：",x_predict)
    error = mean_squared_error(y_test,x_predict)
    print("正规方程的方差：",error)
    return None

# 使用梯度下降来预测波士顿房价
def liner2():
    # 1、获取数据
    bostonData = load_boston()
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(bostonData.data, bostonData.target, random_state=22)
    # 3、特征工程：进行标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4、预估器
    # max_iter:迭代次数
    liner = SGDRegressor(learning_rate="constant", eta0=0.01, max_iter=10000, penalty="l1")
    liner.fit(x_train, y_train)
    # 5、得出模型
    print("梯度下降-权重系数：", liner.coef_)
    print("梯度下降-偏置：", liner.intercept_)
    # 6、模型评估
    x_predict = liner.predict(x_test)
    print("预测房价：", x_predict)
    error = mean_squared_error(y_test, x_predict)
    print("梯度下降的方差：", error)
    return None

# 使用岭回归来预测波士顿房价
def liner3():
    # 1、获取数据
    bostonData = load_boston()
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(bostonData.data, bostonData.target, random_state=22)
    # 3、特征工程：进行标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4、预估器
    # max_iter:迭代次数
    liner = Ridge(alpha=0.5,max_iter=10000)
    liner.fit(x_train, y_train)
    # 5、得出模型
    print("岭回归-权重系数：", liner.coef_)
    print("岭回归-偏置：", liner.intercept_)
    # 6、模型评估
    x_predict = liner.predict(x_test)
    print("预测房价：", x_predict)
    error = mean_squared_error(y_test, x_predict)
    print("岭回归的方差：", error)
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
    # 代码一：用knn算法对鸢尾花数据集进行分类
    # knn_iris()
    # 代码二：用knn算法对鸢尾花数据集进行分类, 加上网格搜索和交叉验证
    # knn_iris_gscv()
    # 代码三：用朴素贝叶斯算法进行对新闻进行分类
    # nb_news()
    # 代码四：使用决策树对鸢尾花进行分类
    # tree_iris()
    # 代码1：使用正规方程来预测波士顿房价
    # liner1()
    # 代码2：使用梯度下降来预测波士顿房价
    # liner2()
    # 代码3：使用岭回归来预测波士顿房价
    # liner3()