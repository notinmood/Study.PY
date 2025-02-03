"""
 * @file   : ui.py
 * @time   : 13:24
 * @date   : 2023/12/6
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from typing import TypedDict

# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 1. 创建强类型字典的两种方式：
#    1.1. 使用类型TypedDict的构造函数，创建一个有名字的字典类型，并定义它的键的名称和值的数据类型
#    1.2. 创建派生于TypedDict的类型，并为此类型定义键的名称和值的数据类型
# 2. 创建强类型字典实例的两种方式：
#    2.1. 使用新类型MyClass的构造函数，创建一个字典实例，并传入命名的键值对
#    2.2. 直接用{}创建一个传入键值对的字典实例，并将其赋值给新类型MyClass的变量
#
# 注意：字典中的key名称和value的类型，必须与强类型字典的键的名称和值的数据类型一致，否则会报错
# +--------------------------------------------------------------------------

# 1. 步骤一、创建强类型
# 1.1.  使用类型TypedDict的构造函数，创建一个有名字的字典类型，并定义它的键的名称和值的数据类型
Movie = TypedDict("Movie", {"name": str, "year": int})


# 1.2. 创建派生于TypedDict的类型，并为此类型定义键的名称和值的数据类型
class Video(TypedDict):
    name: str
    year: int
    directors: list[str]


pass

# 2. 步骤二、再创建命名字典的对象实例
# 2.1 创建对象实例方式1
movie1: Movie = {
    "name": "Blade Runner",
    "year": 1982,
    ## 如果加入了下面这样未定义的属性，那么会出现warning：TypedDict 'Movie' 的额外键 'budget'
    # "budget": 1300000,
}

video1: Video = {
    "name": "Blade Runner",
    "year": 1982,
    "directors": ["Riley Scott"],
}

# 2.2 创建对象实例方式2
movie2 = Movie(
    name="Blade Runner",
    year=1982,
    ## 加入以下为定义的属性，也会出现warning：意外实参
    # budget=3000000,
)

video2: Video = Video(name="Blade Runner", year=1982, directors=["Riley Scott"])


# 3. 调用实例和实例的属性

print(movie1)
print(video1)

## 以下代码会出现warning：“TypedDict 'Movie' 没有属性 'budget'”
# print(movie1["budget"])

