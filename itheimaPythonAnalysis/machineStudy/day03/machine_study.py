from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,SGDRegressor,Ridge
from sklearn.metrics import mean_squared_error

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


if __name__ == "__main__":
    # 代码1：使用正规方程来预测波士顿房价
    liner1()
    # 代码2：使用梯度下降来预测波士顿房价
    # liner2()
    # 代码3：使用岭回归来预测波士顿房价
    # liner3()