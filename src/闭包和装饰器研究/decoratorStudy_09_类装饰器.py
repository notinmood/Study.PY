"""
 * @file   : decoratorStudy_09_类装饰器.py
 * @time   : 23:03
 * @date   : 2024/1/18
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import time


# +--------------------------------------------------------------------------
# |::::TIPS::::| 定义类装饰器的说明
# ---------------------------------------------------------------------------
# 1.  类装饰器与函数装饰器类似，都是接收一个函数作为参数，然后返回一个函数。
# 2.  类装饰器包装函数是通过初始化方法init来实现的，即将要装饰的函数作为参数传入到类的实例化构造器中。
# 3.  通过 XX(func)创建得道类型的一个实例xx后，可以在这个实例xx上，继续调用()，这个时候就是调用__call__方法了。
# 4.  __call__方法中，可以访问到被装饰的函数func，也可以对其附加新的逻辑，从而实现在__call__方法中对func进行装饰。
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
