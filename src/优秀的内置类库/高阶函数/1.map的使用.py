"""
 * @file   : 1.map的使用.py
 * @time   : 10:08
 * @date   : 2024/1/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

if __name__ == '__main__':
    my_arr = [1, 2, 3, 4, 5]
    result = map(lambda x: x * x, my_arr)

    print(result)  # 可以看到map方法返回的是一个迭代器
    for _index, _item in enumerate(result):
        print(f"第{_index}个元素为：{_item}")
    pass
