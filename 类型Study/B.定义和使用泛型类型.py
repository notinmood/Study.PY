"""
 * @file   : A.定义和使用泛型类型.py
 * @time   : 22:05
 * @date   : 2024/1/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from dataclasses import dataclass
from typing import TypeVar, Generic

# +--------------------------------------------------------------------------
# |::::TIPS::::| 定义泛型类型的注意事项
# ---------------------------------------------------------------------------
# 定义泛型类型的目的是控制对象实例中的某些属性的类型为泛型。定义泛型类型的时候：
#   1. 需要从typing模块导入TypeVar，然后使用TypeVar来声明一个名称为T的泛型类型
#   2. 泛型类型需要从Generic[T]派生；或者直接在方法名称后面通过方括号[U, V]指定泛型参数
# +--------------------------------------------------------------------------

T = TypeVar("T")
# 如果类型参数有多个，可以类似格式继续定义
U = TypeVar("U")
V = TypeVar("V")


# 1.1 定义泛型类型的方式1：从Generic[T]派生(带1个类型参数)
@dataclass
class ReturnResult(Generic[T]):
    """
    返回结果
    """
    status: bool = True
    message: str = ""
    data: T = None


# 1.2 定义泛型类型的方式1：从Generic[T]派生(带多个类型参数)
@dataclass
class ReturnResultPro(Generic[U, V]):
    """
    返回结果
    """
    status: bool = True
    message: str = ""
    data: U = None
    addon: V = None


# 2. 定义泛型类型的方式2：直接在方法名称后面通过方括号[S, K]指定泛型参数
# 此种方式使用的泛型类型可直接使用，不需要使用类似U = TypeVar("U")的方式提前声明
@dataclass
class ReturnResultExt[S, K]:
    """
    返回结果
    """
    status: bool = True
    message: str = ""
    data: S = None
    extra: K = None


if __name__ == '__main__':
    print("Hello, world!")

    # 使用泛型类型
    result_str = ReturnResult[str](status=True, message="成功", data="Hello World")
    result_int = ReturnResult[int](status=True, message="成功", data=123)
    result_dict = ReturnResult[dict](status=True, message="成功", data={"name": "张三", "age": 30})

    print(result_str)
    print(result_int)
    print(result_dict)

    print(result_str.data)
    print(result_int.data)
    print(result_dict.data)
    print(result_dict.data["name"])

    print("──分割线───────────────────────────────────")
    # 使用泛型类型
    result_ext_a = ReturnResultExt[str, list](status=True, message="成功", data="Hello World", extra=[1, 2, 3])
    print(result_ext_a.extra)
    result_ext_b = ReturnResultExt[str, str](status=True, message="成功", data="Hello World", extra="山东解大劦")
    print(result_ext_b.extra)
