# *******************返回函数**********************
# 返回求和函数
def calc_num(*args):
    def sum():
        ax = 0
        for num in args:
            ax = ax + num
        return ax
    return sum

result = calc_num(1,2,3,4,5,6)
print(result())