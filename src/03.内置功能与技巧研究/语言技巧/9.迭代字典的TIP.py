"""
 * @file   : 9.迭代字典的TIP.py
 * @time   : 8:05
 * @date   : 2023/12/30
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
if __name__ == '__main__':
    my_dict = {"A": "a",
               "B": "b",
               "C": "c"}
    # 1. 如果对字典直接进行迭代，则迭代得到的是键（key）
    for _item in my_dict:
        print(_item, my_dict[_item])
    pass
    ## --output---------------------------
    # A a
    # B b
    # C c

    print("──分割线───────────────────────────────────")

    # 2. 如果要同时迭代键和对应的值，可以使用 items() 方法
    for key, value in my_dict.items():
        print(key, value)
    pass
    ## --output---------------------------
    # A a
    # B b
    # C c
