from builtins import *

'''
如果给自由变量在作用域内重新赋值的话，
就是启用了一个新的局部变量（只不过这个变量跟自由变量同名）
'''
x = 10
y = 20


def my_func():
    x = 15
    print("局部变量x的值为{}".format(x))


if __name__ == '__main__':
    my_func()
    print("自由变量x的值为{}".format(x))

# output
# 局部变量x的值为15
# 自由变量x的值为10




