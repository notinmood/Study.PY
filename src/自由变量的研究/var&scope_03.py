from builtins import *

'''
如果确实要给自由变量在作用域内重新赋值的话，就是使用global关键字显示声明
'''
x = 10


def my_func():
    global x
    x = 15
    print("内部显示x的值为{}".format(x))


if __name__ == '__main__':
    my_func()
    print("全局显示x的值为{}".format(x))

# output
# 内部显示x的值为15
# 全局显示x的值为15
