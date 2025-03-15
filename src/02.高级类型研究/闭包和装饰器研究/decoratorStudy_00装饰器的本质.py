"""
 * @file   : decoratorStudy_00装饰器的本质.py
 * @time   : 22:43
 * @date   : 2024/1/18
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import time


# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码通过
# ---------------------------------------------------------------------------
# Python装饰器的本质是一个函数，这个函数的输入和输出也都是函数（而且可以是同一个函数）
# 以下通过一个类装饰器的例子来解释装饰器，将@Timer添加在方法def my_func():上的本质为：
# 1. my_func = Timer(my_func) # 本句将my_func函数对象作为参数传递给Timer类，并返回Timer类的一个实例对象给my_func
# 但此时的my_func函数对象已经变成了Timer类的一个实例对象
# 2. 在一个实例对象上调用(),实际上是调用__call__方法
# +--------------------------------------------------------------------------

class Timer(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("计时开始...")
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print("计时结束...")
        print("运行时间: %s 秒" % (end_time - start_time))
        return result


@Timer
def my_func():
    print("函数 my_func执行中...")
    time.sleep(2)


if __name__ == '__main__':
    my_func()
