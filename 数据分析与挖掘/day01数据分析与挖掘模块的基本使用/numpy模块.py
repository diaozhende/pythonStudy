import numpy
# 一维数组
x = numpy.array([4, 3, 2, 1])
print(x[1])
# 二维数组
y = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(y)
print(y[2][2])
# 数组排序
x.sort()
print(x)
y.sort()
print(y)

# 最大值和最小值
xm = x.max()
xn = x.min()
ymax = y.max()
ymin = y.min()
print("x的最大值:"+str(xm)+"----------------x的最小值："+str(xn))
print("y的最大值:"+str(ymax)+"----------------y的最小值："+str(ymin))

# 切片
xArray = x[:3]
print(xArray)
