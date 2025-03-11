"""
 * @file   : 从空数组内读取元素.py
 * @time   : 19:51
 * @date   : 2022/3/17
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from BasicLibrary.data.listHelper import ListHelper

my_list = []

# 1. 使用[]的方式进行索引读取的时候，指定的元素不存在就会抛出异常
# print(my_list[0])
# item0 = my_list.__getitem__(0)
# print(item0)

# 2. 使用ListHelper.get()方法进行索引读取的时候，指定的元素不存在就会返回None
item0 = ListHelper.get(my_list, 0)
print(item0)
