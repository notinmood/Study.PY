"""
 * @file   : OK.Callable类型使用.py
 * @time   : 10:36
 * @date   : 2024/1/13
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from collections.abc import Callable
from functools import reduce
from pprint import pprint
from typing import ParamSpec

# TODO:xiedali@2024/01/13 ParamSpec的应用

# +--------------------------------------------------------------------------
# |::::TIPS::::| ParamSpec的应用(其作用是管理回调函数的位置参数和关键字参数)
# ---------------------------------------------------------------------------
# 当回调函数中，有*args或者**kwargs的时候，很难对其进行签名控制。这个时候可以使用ParamSpec进行统一管理。
#
# 注意实现：
# 1.  需要首先定义一个ParamSpec的类型参数，通常叫P
# 2.  然后使用P来约束函数的位置参数类型和关键字参数类型
# +--------------------------------------------------------------------------
P = ParamSpec('P')


def main_func_with_1param_and_args(name: str, *scores: int, func: Callable[[str, P.args], int]):
    """
    特别说明：
    P类型参数一定要放在参数列表的最后，跟其他参数一起包裹在一个双层的中括号内，否则无法正确识别函数的签名
    :param name:
    :param scores:
    :param func:
    :return:
    """
    print(f"姓名：{name}")
    print("以下是回调函数的信息")
    print("──分割线───────────────────────────────────")
    result = func(name, *scores)
    print("──分割线───────────────────────────────────")
    print(f"回调函数执行完毕,其返回值为：{result}")


def main_func_with_1param_and_args_general(name: str, *scores: int, func: Callable[[str, P], int]):
    """
    特别说明：
    即便回调函数的参数只有*args位置参数，那么不使用 P.args,而是直接使用P也是可以的。
    :param name:
    :param scores:
    :param func:
    :return:
    """
    print(f"姓名：{name}")
    print("以下是回调函数的信息")
    print("──分割线───────────────────────────────────")
    result = func(name, *scores)
    print("──分割线───────────────────────────────────")
    print(f"回调函数执行完毕,其返回值为：{result}")


def called_func_with_1param_and_args(name: str, *scores: int) -> int:
    result = reduce(lambda x, y: x + y, scores)
    print(f"学生{name} 总成绩：{result}")
    return result


def main_func_with_2param_and_args(name: str, grade: int, *scores: int, func: Callable[[str, int, P.args], int]):
    print(f"姓名：{name},年级：{grade}")
    print("以下是回调函数的信息")
    print("──分割线───────────────────────────────────")
    result = func(name, grade, *scores)
    print("──分割线───────────────────────────────────")
    print(f"回调函数执行完毕,其返回值为：{result}")


def called_func_with_2param_and_args(name: str, grade: int, *scores: int) -> int:
    result = reduce(lambda x, y: x + y, scores)
    print(f"{grade}年级的学生{name} 总成绩：{result}")
    return result


def main_func_with_2param_and_args_kwargs(name: str, grade: int, *scores: int, func: Callable[[str, int, P.args, P.kwargs], int],
                                          **history_scores: int):
    """
    特别说明：
    即便回调函数的参数只有*args位置参数，那么不使用 P.args,而是直接使用P也是可以的。
    :param grade:
    :param name:
    :param scores:
    :param func:
    :return:
    """
    print(f"姓名：{name}")
    print("以下是回调函数的信息")
    print("──分割线───────────────────────────────────")
    result = func(name, grade, *scores, **history_scores)
    print("──分割线───────────────────────────────────")
    print(f"回调函数执行完毕,其返回值为：{result}")


pass


def main_func_with_2param_and_args_kwargs_general(name: str, grade: int, *scores: int, func: Callable[[str, int, P], int],
                                                  **history_scores: int):
    """
    特别说明：
    类型参数P，可以表示回调函数的参数:1.位置参数*args，那么不使用 P.args,而是直接使用P也是可以的。2.关键字参数**kwargs
    :param grade:
    :param name:
    :param scores:
    :param func:
    :return:
    """
    print(f"姓名：{name}")
    print("以下是回调函数的信息")
    print("──分割线───────────────────────────────────")
    result = func(name, grade, *scores, **history_scores)
    print("──分割线───────────────────────────────────")
    print(f"回调函数执行完毕,其返回值为：{result}")


pass


def called_func_with_2param_and_args_kwargs(name: str, grade: int, *scores: int, **history_scores: int) -> int:
    result = reduce(lambda x, y: x + y, scores)
    print(f"{grade}年级的学生{name} 本学期总成绩：{result}")
    print("以下是历史成绩：")
    pprint(history_scores)
    return result


if __name__ == '__main__':
    main_func_with_1param_and_args("张三", 77, 69, 80, func=called_func_with_1param_and_args)
    print("======")
    main_func_with_1param_and_args_general("张三", 77, 69, 80, func=called_func_with_1param_and_args)
    print("======")
    main_func_with_2param_and_args("李四", 3, 40, 69, 80, func=called_func_with_2param_and_args)
    print("======")

    _history_scores = {"第一学期总分": 30, "第二学期总分": 40}
    main_func_with_2param_and_args_kwargs("王五", 3, 40, 69, 80, func=called_func_with_2param_and_args_kwargs,
                                          **_history_scores)
    print("======")
