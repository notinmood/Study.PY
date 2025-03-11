"""
 * @file   : 02.__call__使用在类装饰器中.py
 * @time   : 10:07
 * @date   : 2025/3/5
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: Less is more.Simple is best!
"""
import time


class LogExecutionTime:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"{self.func.__name__} 执行耗时: {end - start:.2f}秒")
        return result


@LogExecutionTime
def my_function():
    time.sleep(1)


my_function()  # 输出：my_function 执行耗时: 1.00秒
