import numpy
import matplotlib.pylab
x=[1,2,3,4,8]
y=[5,7,2,1,5]
# matplotlib.pylab.plot(x,y)#plot(x轴数据，y轴数据，展现形式)
# o代表散点图
matplotlib.pylab.plot(x,y,"mo--")
matplotlib.pylab.plot(x,y,"p")
matplotlib.pylab.show()
'''
颜色：
c-cyan--青色
r-red--红色
m-magente-品红
g-green--绿色
b-blue--蓝色
y-yellow--黄色
k-black--黑色
w-white-白色

线的样式：
- 直线
-- 虚线
-. -.形式
: 细小虚线
点的形状：
s--方形
h--六角形
H--六角形
*--星形
+--加号
x--x型
d--菱形
D--菱形
p--五角形
'''
#matplotlib.pylab.title("show")#标题
#matplotlib.pylab.xlabel("ages")x轴
#matplotlib.pylab.ylabel("temp")y轴