# StringIO

from io import StringIO
# f = StringIO()
# f.write("hello")
# f.write("  ")
# f.write("world")
# print(f.getvalue())

# 初始化StringIO
# f = StringIO("StringIO初始化")
# print(f.getvalue())

# BytesIO
from io import BytesIO
b = BytesIO()
b.write("中文".encode("UTF-8"))
print(b.getvalue())

# 初始化BytestIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
