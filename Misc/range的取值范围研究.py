from builtins import *

"""
range(A,B)的时候，是包含A的，但不包含B，即是 A <= i < B
本例子中，打印的结果为0-9(包含0，但不包含10)
"""
if __name__ == '__main__':
    for i in range(0, 10):
        print(i)


