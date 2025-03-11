"""
生成器的研究与使用
"""


# 1. 生成器的标准定义方法
def standard_generator():
    """
    生成器标准定义方法
    :return:
    """
    for _i in range(3):
        yield _i * _i
    pass


# 2. 生成器的快速定义方法
# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 注意定义快速生成器和定义推导式语法非常相似。
# 具体参见：文件“语言技巧/3.推导式研究.py”
# +--------------------------------------------------------------------------
def rappid_generator():
    """
    生成器快速定义方法
    :return:
    """
    return (_i * _i for _i in range(3))


if __name__ == '__main__':
    my_generator = standard_generator()

    print('1. my_generator type为:')
    print(type(my_generator))
    print('2. my_generator 对象为:')
    print(my_generator)

    print('3. my_generator 内容为:')
    print('3.1 使用基础的方式： next() 函数调用 获取下一个值')
    print(next(my_generator))
    print(next(my_generator))
    print(next(my_generator))
    # # 由于 my_generator 对象 已经没有值了，所以再次调用 next() 函数 就会报错
    # print(next(my_generator))

    print('3.2 使用 for 循环调用 获取下一个值')
    my_generator = rappid_generator()
    print(my_generator)
    for i in my_generator:
        print(i)
    pass

    print('4. 使用list、tuple等构造函数快速调用生成器以获取生成器对象的所有值')
    my_generator = rappid_generator()
    my_list = list(my_generator)
    print(my_list)
    my_generator = rappid_generator()
    my_tuple = tuple(my_generator)
    print(my_tuple)
    my_generator = rappid_generator()
    my_set = set(my_generator)
    print(my_set)
