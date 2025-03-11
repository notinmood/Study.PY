"""
 * @file   : 00.类型声明.py
 * @time   : 13:44
 * @date   : 2025/3/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: Less is more.Simple is best!
"""

# 1. 变量的类型声明

a: int = 10  # 整数
b: float = 3.14  # 浮点数
c: bool = True  # 布尔值
d: str = "hello, world"  # 字符串
e: list = [1, 2, 3]  # 列表
f: tuple = (1, 2, 3)  # 元组
g: dict = {"name": "Alice", "age": 25}  # 字典
h: set = {1, 2, 3}  # 集合


# 2. 函数的类型注解

def add(aa: int, bb: int) -> int:
    return aa + bb


pass
