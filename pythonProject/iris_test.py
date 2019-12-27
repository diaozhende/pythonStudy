from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np

'''
- Iris-Setosa
- Iris-Versicolour
- Iris-Virginica
'''
param_x = [[6.3, 2.7, 4.9, 1.8]]
param_y = [1]
param_data_x = np.array(param_x)
param_data_y = np.array(param_y)
iris_data = load_iris()
print(iris_data.DESCR)
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target)
transform = StandardScaler()
x_train = transform.fit_transform(x_train)
x_test = transform.transform(x_test)
param_data_x = transform.transform(param_data_x)
estimator = KNeighborsClassifier(n_neighbors=7)
# param_dict = {"n_neighbors": [1, 3, 5, 7, 9, 11]}
# estimator = GridSearchCV(estimator, param_grid=param_dict)
estimator.fit(x_train, y_train)
score = estimator.score(x_test, y_test)
print("准确率：", score)
predict = estimator.predict(param_data_x)
if predict[0] == 0:
    print("预测结果：Iris-Setosa")
elif predict[0] == 1:
    print("预测结果：Iris-Versicolour")
elif predict[0] == 2:
    print("预测结果：Iris-Virginica")
# print("预测结果：", predict)
# print("最佳参数:\n", estimator.best_params_)



from google.cloud import bigquery
