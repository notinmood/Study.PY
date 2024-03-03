"""
 * @file   : 装饰器的应用-01.py
 * @time   : 9:51
 * @date   : 2024/1/24
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import time
from typing import Callable


def timeit_wrapper[T, ** P](func: Callable[P, T]):
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        print(f"{func.__name__} 开始执行")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行结束，耗时：{(end - start) * 1000}ms")
        return result

    return wrapper


def timeit_directly[T, ** P](func: Callable[[..., P], T]):
    # 如果被调用函数func后面没有其他代码，那么可以省略内部的包装函数，直接将func返回。
    print(f"{func.__name__} 开始执行")
    start = time.time()
    result = func
    end = time.time()
    print(f"{func.__name__} 执行结束，耗时：{(end - start) * 1000}ms")
    return result


pass


@timeit_wrapper
def my_func1(a: int, b: int) -> int:
    # time.sleep(1)
    print("这是被装饰的函数内部的逻辑")
    return a + b


@timeit_directly
def my_func2(a: int, b: int) -> int:
    # time.sleep(1)
    print("这是被装饰的函数内部的逻辑")
    return a + b


pass

if __name__ == "__main__":
    my_func1(3, 4)
    print("──分割线───────────────────────────────────")
    # my_func2(6, 7)
