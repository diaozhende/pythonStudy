# 常用的内建模块

# 获取当前时间
from datetime import datetime
now = datetime.now()
print(now)

# 获取指定日期和时间
dt = datetime(1997,5,5,15,55,55)
print(dt)
# 将datetime转换成timestamp
print(dt.timestamp())

# 将timestamp 转换成datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))

# str 转换成 datetime
from datetime import datetime
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime 转换成str
from datetime import datetime
nowTime = datetime.now()
print(now.strftime("%a %b %d %H:%M"))

# datetime加减
from datetime import datetime,timedelta
now = datetime.now()
print("现在的时间为：",now)
resultNow = now+timedelta(hours=10)
resultNow1 = now + timedelta(days=2, hours=12)
print("现在的时间为：",resultNow)
print("第二次计算的时间为：",resultNow1)

