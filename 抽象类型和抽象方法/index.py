"""
 * @file   : using.py
 * @time   : 下午6:25
 * @date   : 2024/4/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from defineData import *

if __name__ == '__main__':
    # 1. 实例化抽象类对象
    # 一个类型即便声明为抽象类，也依然可以实例化
    shape = Shape()
    city = City()

    # 2. 不能实例化带有抽象方法的类型
    # 无论类型中是否对抽象方法进行了实现，都不能实例化
    # animal = Animal() # 报错，
    # country = Country() # 报错，即便已经为抽象方法进行了默认实现
