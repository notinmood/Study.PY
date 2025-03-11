"""
 * @file   : 8.使用两个星号进行解包操作.py
 * @time   : 21:58
 * @date   : 2023/12/16
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

"""
解包操作：
    1. 基本解包：
        1. 基本解包是指将一个可迭代对象中的元素，按照位置顺序，依次赋值给多个变量（元素的数量和变量的数量必选相等）。
        2. 基本解包的语法格式：
            变量1, 变量2, 变量3, ... = （包含元素的）可迭代对象
        3. 基本解包的示例：
            fruits = ['apple', 'banana', 'orange']
            fruit1, fruit2, fruit3 = fruits
            print(fruit1)
            print(fruit2)
            print(fruit3)
    2. 扩展解包：
        1. 扩展解包是指将一个可迭代对象中的元素，按照位置顺序，依次赋值给多个变量（变量的数量要小于等于元素的个数，其中某个变量要以*开头）。
        2. 扩展解包的语法格式：
            变量1, 变量2, *变量3, ... = （包含元素的）可迭代对象
        3. 扩展解包的示例：
            fruits = ['apple', 'banana', 'orange','pear']
            fruit1, *fruit2, fruit3 = fruits
            # 或者 fruit1, fruit2, *fruit3 = fruits
            print(fruit1)
            print(fruit2)
            print(fruit3)
▌注意：
    1. 基本解包的语法格式中：可迭代对象中的可迭代元素的数量，必须与变量数量相等。
    2. 扩展解包的语法格式中：可迭代对象中的可迭代元素的数量，可以等于或者多于变量数量。
    3. 扩展解包的语法格式中：以*开头的变量，可以接收任意数量的可迭代的普通元素。
    4. 扩展解包的语法格式中：以**开头的变量，可以接收任意数量的可迭代的字典元素。 
    5. 定义方法时，*args和**kwargs是可变参数，它们的作用是接收任意数量的位置参数和关键字参数，他们就是这种解包语法的最常见表现形式。
    

▌参考资料：https://zhuanlan.zhihu.com/p/664917461


另外zip除了可以缝合，也可以解包
    zip(iterable_a,iterable_b) 函数用于将两组（或多组）可迭代的对象作为参数，将对象中对应的元素一一对照分别打包成一个个元组，然后返回由这些元组列表
    zip(*tuple_zipped)给参数使用*，可以对缝合的zip进行解包，具体参看：`优秀的内置类库/高阶函数/4.zip的使用研究.py`
"""

if __name__ == '__main__':
    # 1. 基本解包示例
    print("# 1. 基本解包示例")

    fruits = ['apple', 'banana', 'orange']
    fruit1, fruit2, fruit3 = fruits
    print(fruit1)
    print(fruit2)
    print(fruit3)

    print('------------------------------------------')

    # 2. 解包嵌套结构
    print("# 2. 解包嵌套结构")

    person = ('John', 'Doe', 30, ('New York', 'USA'))
    first_name, last_name, age, (city, country) = person

    print(first_name)  # 输出: 'John'
    print(last_name)  # 输出: 'Doe'
    print(age)  # 输出: 30
    print(city)  # 输出: 'New York'
    print(country)  # 输出: 'USA'

    print('------------------------------------------')

    # 3. 解包函数返回值
    print("# 3. 解包函数返回值")


    def get_name():
        return 'John', 'Doe'


    first_name, last_name = get_name()

    print(first_name)  # 输出: 'John'
    print(last_name)  # 输出: 'Doe'
    print('------------------------------------------')

    # 4. 解包可变长度的可迭代对象
    print("# 4. 解包可变长度的可迭代对象")

    numbers = [1, 2, 3, 4, 5]
    a, b, *rest = numbers
    print(a, b)  # 输出: 1 2
    print(rest)  # 输出: [3, 4, 5]

    # # 如果长度小于变量数量，会引发 ValueError 异常
    # a, b, c, d, e, f = numbers  # ValueError: not enough values to unpack (expected 6, got 5)
    print('------------------------------------------')

    # 5. 使用“**”（两个星号）解包字典
    print("#  5. 使用“**”（两个星号）解包字典")

    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # 5.1 定义函数时候，使用“**”解包字典的键值对，并将其分别作为参数传递进入函数中
    def my_function(**_dict):
        print(_dict)


    # 5.2 调用函数时，使用“**”解包字典(即：将字典的键值对解包后分别作为函数参数传递到函数中)
    my_function(**my_dict, **{'d': 4, 'e': 5})
