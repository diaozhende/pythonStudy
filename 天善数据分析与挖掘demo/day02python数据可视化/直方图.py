import numpy
import matplotlib.pylab
# 生成随机数 random_integers代表随机数为整数
data = numpy.random.random_integers(1,20,10)#(最小值，最大值，个数)
# 生成正态分布数据
dataZ = numpy.random.normal(5.0,3,10)#(均数，西格玛，个数)
# matplotlib.pylab.hist(dataZ)
# matplotlib.pylab.show()

data1 = numpy.random.random_integers(1,50,10)
# matplotlib.pylab.hist(data1)
# matplotlib.pylab.show()

# 设置直方图的宽度和上下限
sty = numpy.arange(1,30,2)#(最小值，最大值，步长)
# matplotlib.pylab.hist(sty)
# matplotlib.pylab.show()

#子图：一张图中绘制多个子图

x1=[1,2,3,4,5]
y1=[5,3,5,23,5]
x2=[5,2,3,8,6]
y2=[7,9,12,12,3]
x3=[5,6,7,10,19,20,29]
y3=[6,2,4,21,5,1,5]
matplotlib.pylab.subplot(2,2,1)#(行，列，当前区域)
matplotlib.pylab.plot(x1,y1,"m")

matplotlib.pylab.subplot(2,2,2)
matplotlib.pylab.plot(x2,y2,"r")

matplotlib.pylab.subplot(2,1,2)
matplotlib.pylab.plot(x3,y3,"g")

matplotlib.pylab.show()
