"""
 * @file   : index.py
 * @time   : 12:11
 * @date   : 2021/12/16
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from random import Random

if __name__ == '__main__':
    """
    1、获取随机数
    """
    r = Random()
    print("1-10之间随机数：{}".format(r.randint(a=1, b=10)))

    """
    2、从集合中获取随机元素
    """
    my_cities = ["qingdao", "beijing", "shanghai"]
    print("随机选中的list元素为：{}".format(r.choice(my_cities)))
