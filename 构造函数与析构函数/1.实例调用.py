"""
 * @file   : using.实例调用.py
 * @time   : 8:18
 * @date   : 2021/12/26
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from 构造函数与析构函数.person import Person

"""
调用类型的实例方法，会触发其构造函数和析构函数
"""
p = Person()
p.eat()

## --output---------------------------
# 我出生了
# 吃饭
