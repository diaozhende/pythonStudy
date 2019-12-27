from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import matplotlib.pylab as py
import numpy as np


# Create your views here.
def iris_knn(request):
    '''
    Iris-Setosa：山鸢尾
    Iris-Versicolour：变色鸢尾
    Iris-Virginica：为吉尼亚鸢尾
    :param request:
    :return:
    '''
    code = 200
    msg = ''
    try:
        calyxLong = request.GET.get("calyxLong")
        calyxWide = request.GET.get("calyxWide")
        petalLong = request.GET.get("petalLong")
        petalWide = request.GET.get("petalWide")
        param_x = [[calyxLong, calyxWide, petalLong, petalWide]]
        # param_x = [[6.3, 2.7, 4.9, 1.8]]
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
        result = ''
        if predict[0] == 0:
            result = '山鸢尾'
            print("预测结果：山鸢尾")
        elif predict[0] == 1:
            result = '变色鸢尾'
            print("预测结果：变色鸢尾")
        elif predict[0] == 2:
            result = '为吉尼亚鸢尾'
            print("预测结果：为吉尼亚鸢尾")
    except Exception as e:
        code = 500
        msg = str(e)
    res = {'code': code, 'data': result, 'msg': msg}
    setosaCount = iris_data.target[iris_data.target == 0].size
    versicolourCount = iris_data.target[iris_data.target == 1].size
    virginicaCount = iris_data.target[iris_data.target == 2].size
    iris_count = [setosaCount, versicolourCount, virginicaCount]
    iris_label = ['山鸢尾', '变色鸢尾', '为吉尼亚鸢尾']
    py.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    py.figure(figsize=(8, 6), dpi=80)
    py.pie(iris_count, labels=iris_label, colors=['#CA8243', '#42B874', '#D25D51'])
    py.legend()
    py.axis('equal')
    py.savefig('E:/pythonStudy/pythonProject/irisProject/static/img/iris/iris.jpg')
    py.show()
    # return HttpResponse('<h1>预测结果为：' + result + '</h1><br>')
    return JsonResponse(res)
