"""
 * @file   : OK.Callable类型使用.py
 * @time   : 10:36
 * @date   : 2024/1/13
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from collections.abc import Callable


# +--------------------------------------------------------------------------
# |::::TIPS::::| 通过Callable类型可以指明要调用的函数必须符合某种签名形式（参数和返回值信息）
# ---------------------------------------------------------------------------
# 1. Callable类型来源于Python的collections.abc模块（别名typing.Callable）
# 2. Callable后面跟的[[T],U]形式的类型参数。外层中括号内有两个类型参数：分别表示函数的参数类型和
# 返回值类型，其中参数类型可以是一个或多个类型（但必选放在内层中括号内），返回值类型只能是一个类型。
# ────────────────────────
# 比如：a. 明确回调函数的类型，该函数接受一个字符串作为参数，并以一个int作为返回值。其表述为：
# Callable[[str], int]
#      b. 明确回调函数的类型，该函数接受int和list作为两个参数，并以一个字符串作为返回值。其表述为：
# Callable[[int, list], str]
# +--------------------------------------------------------------------------

def hello(name: str, func: Callable[[str], int]):
    print(f"传入的参数为{name}")
    print("以下是回调函数的信息")
    print("──分割线───────────────────────────────────")
    result = func(name)
    print("──分割线───────────────────────────────────")
    print(f"回调函数执行完毕,其返回值为：{result}")


def display_info(info: str) -> int:
    print(f"我是一个显示函数，我接收到的参数为:{info}")
    return len(info)


pass

if __name__ == '__main__':
    hello("张三", display_info)
