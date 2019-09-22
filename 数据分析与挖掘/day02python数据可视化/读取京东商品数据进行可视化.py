import numpy
import pandas
import matplotlib.pylab
import pymysql
# 读取数据库数据
conn = pymysql.connect("127.0.0.1","root","root","template")
sql = "select * from book LIMIT 1,20"
sqlData = pandas.read_sql(sql,conn)
data = sqlData.T
y = data.values[2]
x = data.values[6]
# matplotlib.pylab.plot(x,y,"m")
# matplotlib.pylab.show()
sty = numpy.arange(int(data.values[6].min()),int(data.values[6].max()),85)
matplotlib.pylab.hist(y,sty)
matplotlib.pylab.show()
