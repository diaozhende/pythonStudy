from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


# 1、获取数据
iris_data = load_iris()

# 2、划分数据集
x_train,x_test,y_train,y_test = train_test_split(iris_data.data,iris_data.target)

# 3、特征工程（标准化）
transfer = StandardScaler()
transfer.fit_transform(x_train)
transfer.fit(x_test)

# 4、转换器流程
estimator = KNeighborsClassifier()
# 用网格搜索进行模型调优
param_grid = {"n_neighbors":[1,2,5,6,7]}
estimator = GridSearchCV(estimator,param_grid=param_grid,cv=5)

# 训练数据
estimator.fit(x_train,y_train)

# 5、模型评估
# 输出预测结果
result = estimator.predict(x_test)
print("预测结果:\n",result)
# 准确率
score = estimator.score(x_test,y_test)
print("准确率：\n",score)
# 在交叉验证中最好的结果
print("在交叉验证中最好的结果:\n",estimator.best_score_)
# 最好的模型
print("最好的模型:\n",estimator.best_estimator_)