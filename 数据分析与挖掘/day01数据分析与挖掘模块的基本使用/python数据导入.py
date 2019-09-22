import pandas
import xlrd

# 导入cvs数据
cvsData = pandas.read_csv("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第5周/hexun.csv")
# print(cvsData.describe())
# 查看某一列的详细信息
# print(cvsData.sort_values(by="21"))

# 导入excel数据
excelData = pandas.read_excel("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第5周/abc.xls")


# 导入mysql数据
import pymysql
conn = pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="pythontestdb")
sql = "select * from book"
sqlData = pandas.read_sql(sql,conn)
# print(sqlData.describe())

# 导入html数据
htmlData = pandas.read_html("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第5周/abc.html")
# print(htmlData)

# 导入txt数据
txtData = pandas.read_table("E:/python大数据资料/Python3数据分析与挖掘实战/源码/第5周/abc.txt")
# print(txtData.describe())