# ************************生成器******************************
def opp():
    print("step1")
    yield (1)
    print("step2")
    yield (3)
    print("step5")
    yield (5)

o = opp()
print(o)
# print(next(0))
next(o)
next(o)
next(o)
