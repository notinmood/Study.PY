"""
 * @file   : www.py
 * @time   : 20:35
 * @date   : 2022/3/24
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

list_data = ["a", "b", "c"]
for key in list_data:
    print(key)
pass

# --output---
# a
# b
# c

print("─────────────────────────────────────")
for i in range(len(list_data)):
    print(i)
    item = list_data[i]
    print(item)
pass

# --output---
# 0
# a
# 1
# b
# 2

print("─────────────────────────────────────")

# 对list使用enumerate方法后，就可以得到每个元素的索引号和元素的值
for k, v in enumerate(list_data):
    print(k, v)
pass

# --output---
# 0 a
# 1 b
# 2 c
