_author_ = 'Michael Liao'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello %s!"% args[1])
    else :
        print("Too many arguments!")
test()