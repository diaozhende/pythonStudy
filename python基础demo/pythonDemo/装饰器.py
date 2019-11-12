# ********************装饰器*********************
import functools
# def log(func):
#     def wrapper(*args,**kw):
#         print("call %s()"%func.__name__)
#         return func(*args,**kw)
#     return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s  %s()"%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log("call")
@log("end")
def now():
    print('2019-7-24 16:16:27')


now()
print(now.__name__)