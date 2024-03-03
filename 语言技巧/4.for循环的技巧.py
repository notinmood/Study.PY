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

# --output---
# a
# b
# c

print("─────────────────────────────────────")
for i in range(len(list_data)):
    print(i)
    item = list_data[i]
    print(item)

# --output---
# 0
# a
# 1
# b
# 2

print("─────────────────────────────────────")
for k, v in enumerate(list_data):
    print(k, v)

# --output---
# 0 a
# 1 b
# 2 c


