"""
 * @file   : 05.数字类型与非数字nan.py
 * @time   : 10:25
 * @date   : 2025/3/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: Less is more.Simple is best!
"""
import math

# 1. 非数字的数字类型nan的表示
nan = float('nan')  # nan表示Not a Number
print(nan)  # nan

# 2. nan的判断
print(type(nan))  # <class 'float'> # nan的类型是float
print(isinstance(nan, float))  # True
print(isinstance(nan, int))  # False
print(math.isnan(nan))  # True
print(nan == float('nan'))  # False # 所有的nan都不相等（TypeScript，PHP等语言也一样）
