"""
 * @file   : 3.filter的使用.py
 * @time   : 10:12
 * @date   : 2024/1/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 1. Python2.7 返回列表，Python3.x 返回迭代器对象（迭代器需要进一步调用才能获取到内部的元素）。
# 2. filter，顾名思义，就是一个过滤器。其作用是从列表（或其他序列类型）中筛选出满足条件的子列表，filter是python的内置函数，无须import即可直接使用。
# +--------------------------------------------------------------------------
if __name__ == '__main__':
    result = filter(lambda x: x > 0, [1, -2, 3, -4, 5, -6])
    print(result)  # <filter object at 0x...>
    print(list(result))  # [1, 3, 5]

