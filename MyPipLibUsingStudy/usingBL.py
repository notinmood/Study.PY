"""
 * @file   : index.py
 * @time   : 14:12
 * @date   : 2021/11/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from BasicLibrary.data.stringHelper import *

if __name__ == '__main__':
    # 1. 使用index占位符的形式
    original = "My name is {0},my age is {1}."
    result = StringHelper.format(original, "zhangsan", 20)
    print(result)

    # 2. 使用具名占位符的形式
    original = "My name is {name},my age is {age}."
    result = StringHelper.format(original, name="zhangsan", age=20)
    print(result)
