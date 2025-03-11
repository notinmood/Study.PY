"""
 * @file   : 05.数字类型与非数字nan.py
 * @time   : 10:25
 * @date   : 2025/3/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: Less is more.Simple is best!
"""
import math


# 数字类型判断变量的类型判断
def display(value):
    print(value, "的类型是：", type(value))
    print(value, "是float类型？", isinstance(value, float))
    print(value, "是int类型？", isinstance(value, int))
    print(value, "是复数类型？", isinstance(value, complex))

    if not isinstance(value, complex):
        print(value, "是nan结果？", math.isnan(value))
        print(value, "是inf结果？", math.isinf(value))
    pass

    print("-----------------------")


# 数字类型
aa = 123;
display(aa)
# 123 的类型是： <class 'int'>
# 123 是float类型？ False
# 123 是int类型？ True
# 123 是复数类型？ False
# 123 是nan结果？ False
# 123 是inf结果？ False

bb = 3.14;
display(bb)
# 3.14 的类型是： <class 'float'>
# 3.14 是float类型？ True
# 3.14 是int类型？ False
# 3.14 是复数类型？ False
# 3.14 是nan结果？ False
# 3.14 是inf结果？ False

cc = 1 + 2J;  # 复数部分必须使用j或J表示
display(cc)
# (1+2j) 的类型是： <class 'complex'>
# (1+2j) 是float类型？ False
# (1+2j) 是int类型？ False
# (1+2j) 是复数类型？ True

# 非数字的数字类型nan的表示
nan = float('nan')  # nan表示Not a Number
display(nan)
# nan 的类型是： <class 'float'>
# nan 是float类型？ True
# nan 是int类型？ False
# nan 是复数类型？ False
# nan 是nan结果？ True
# nan 是inf结果？ False

inf = float('inf')  # inf表示正无穷大
display(inf)
# inf 的类型是： <class 'float'>
# inf 是float类型？ True
# inf 是int类型？ False
# inf 是复数类型？ False
# inf 是nan结果？ False
# inf 是inf结果？ True

inf_neg = float('-inf')  # -inf表示负无穷大
display(inf_neg)
# -inf 的类型是： <class 'float'>
# -inf 是float类型？ True
# -inf 是int类型？ False
# -inf 是复数类型？ False
# -inf 是nan结果？ False
# -inf 是inf结果？ True

