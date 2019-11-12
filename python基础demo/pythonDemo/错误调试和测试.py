# def testException(num):
#     try:
#         result = 100/num
#     except Exception as e:
#         print("Error:",e)
#     print(result)
#
#
# testException(0)

# def testException(num):
#     try:
#         result = 100/num
#     except Exception as e:
#         logging.exception(e)
#     print(result)
# testException(0)

# class Error(ValueError):
#     print("出现错误")
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise Error('invalid value: %s' % s)
#     return 10/n
# foo(0)

# 调试************断言
# def foo(s):
#     n = int(s)
#     assert n != 0,'n is zero'
#     return 10/n
# foo(0)

# 调试************logging
import logging
logging.basicConfig(level=logging.INFO) #指定记录信息级别
def foo(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10/n
foo(0)