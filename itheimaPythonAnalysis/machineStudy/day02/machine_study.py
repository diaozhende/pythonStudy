from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier

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


if __name__ == "__main__":
    # 代码一：用knn算法对鸢尾花数据集进行分类
    # knn_iris()
    # 代码二：用knn算法对鸢尾花数据集进行分类, 加上网格搜索和交叉验证
    # knn_iris_gscv()
    # 代码三：用朴素贝叶斯算法进行对新闻进行分类
    # nb_news()
    # 代码四：使用决策树对鸢尾花进行分类
    tree_iris()