"""
 * @file   : 12.元组的使用技巧.py
 * @time   : 9:27
 * @date   : 2024/3/19
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
if __name__ == '__main__':
    # 1. 创建仅有一个元素的元组对象
    t1 = ("qingdao",)
    print(t1)

    # 2. 给某对象赋多个值的时候，其自动创建元组
    t2 = "qingdao", "beijing", "shanghai"
    print(t2)
