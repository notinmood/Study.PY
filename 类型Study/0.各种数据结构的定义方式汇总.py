"""
 * @file   : 0.各种数据结构的定义方式汇总.py
 * @time   : 下午5:55
 * @date   : 2024/4/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from dataclasses import dataclass
from enum import Enum


# 1. 定义枚举类型（内部有赋值操作）
# 枚举类型本质上是使用类型的静态属性来表达信息的方式。
# 基本上可以理解为一个具体的对象（只是这个对象的属性是固定的））
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# 2. 定义结构体类型（内部没有赋值操作）
# 定义结构体类型本质上是在定义类的结构信息，结构体类型可以包含多个属性，每个属性都有自己的类型。
# 然后在其他地方实例化这个类为具体的对象后再使用。
@dataclass
class Point:
    x: float
    y: float
