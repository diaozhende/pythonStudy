# 导入mysql驱动
import mysql.connector
# 连接数据库
conn = mysql.connector.connect(user='root', password='root',database='pythontestdb')
cursor = conn.cursor()
# 执行sql语句
cursor.execute("insert into user(id,username,password) values(%s,%s,%s)",["2","lisi","123321"])
cursor.execute("select * from user where id = %s",["1"])
result = cursor.fetchall()
print(result)
conn.commit()
cursor.close()


