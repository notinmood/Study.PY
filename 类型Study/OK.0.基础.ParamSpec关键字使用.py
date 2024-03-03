"""
 * @file   : sd.py
 * @time   : 10:37
 * @date   : 2024/1/22
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from typing import Callable


# 1. 在定义函数的时候，可以使用ParamSpec泛型类型来定义位置参数和命名参数的类型

# 2. 定义ParamSpec泛型类型的两种方式
# 2.1.  使用typing.ParamSpec来定义ParamSpec泛型类型
# from typing import ParamSpec, Callable
#
# P = ParamSpec("P")


# 2.2.  在函数（或者class）上使用[**P]来定义ParamSpec泛型类型
def func_name[** P](arg_name: str, func_called: Callable[P, int], *args, **kwargs):
    print(f"{arg_name} 在主函数中 do something...")
    result = func_called(*args, **kwargs)
    print(f"回调函数返回的结果为{result}")


pass


def func_called_detail1(*args):
    print(f"do something...{args}")
    return 1


def func_called_detail2(**kwargs):
    print(f"do something...{kwargs}")
    return 2


def func_called_detail3(*args, **kwargs):
    print(f"do something...{args}{kwargs}")
    return 3


pass

if __name__ == '__main__':
    func_name("zhangsan", func_called_detail1)
    func_name("lisi", func_called_detail1, 1, 2, 3)
    func_name("zhaoliu", func_called_detail2, a=1, b=2)
    func_name("wangwu", func_called_detail3, 1, 2, 3, a=1, b=2)
