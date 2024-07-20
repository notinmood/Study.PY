"""
 * @file   : 16.匿名函数和lambda表达式.py
 * @time   : 下午3:53
 * @date   : 2024/7/20
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
# Python中不支持普通的匿名函数，只有lambda表达式是其唯一支持的匿名函数

my_arr = [1, 2, 3, 4, 5]
result = map(lambda x: x * x, my_arr)
