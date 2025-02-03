"""
 * @file   : 6.列表list和集合set内元素的有序无序问题.py
 * @time   : 11:07
 * @date   : 2023/6/21
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

if __name__ == '__main__':
    # 1. list 列表内元素是有序排放的
    my_list = [_item for _item in "qingdao city"]
    print(my_list)  # ["q", "i", "n", "g", "d", "a", "o", " ", "c", "i", "t", "y"]

    # 2. set 集合内元素是无序排放的
    chars = {_item for _item in "Qingdao City"}
    print(chars)  # {'o', ..., 'y', 'a'} 因为set的特性，具体的元素顺序每次不一样

pass
