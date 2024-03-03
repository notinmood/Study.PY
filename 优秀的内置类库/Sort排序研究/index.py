"""
 * @file   : index.py
 * @time   : 16:47
 * @date   : 2022/3/17
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# 返回 'year' 值的函数：
def my_func(e):
    return e['year']


if __name__ == '__main__':
    """
    1. 由简单元素组成的数组，直接用不带参数的sort就可以。
    """
    my_list = [5, 8, 3, 6, 1, 10, 2]
    my_list.sort()
    print(my_list)

    """
    2. 由复杂元素组成的数组，可以给sort传递一个 命名参数为key 的函数
        ~ 这个函数接收一个参数（这个参数就是数组的复杂元素），
        ~ 返回值是这个复杂元素的属性名称（就是用这个属性作为key对数组进行排序）。
    """
    cars = [
        {'car': 'Porsche', 'year': 1963},
        {'car': 'Audi', 'year': 2010},
        {'car': 'BMW', 'year': 2019},
        {'car': 'Volvo', 'year': 2013}
    ]

    # cars.sort(key=my_func)
    cars.sort(key=lambda item: item["year"])
    print(cars)
