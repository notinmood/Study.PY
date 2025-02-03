"""
自由变量（在某个作用域x（本例为my_func）外定义的，但在作用域内调用的变量），
不能改变其对象的指向信息（即系统内部对象的id信息，或者称为内存的地址不可以改变）：
=> 对int，string这样的简单类型来说，不能改变其值（因为要通过重新赋值的方式改变其值）。
=> 对list，dict（元组除外）等复杂类型来说，在不改变系统内部id的情况下，
可以修改其成员元素的值；但是不能直接给对象赋值改变。
"""

x = 10
y = 20
li = ['1', 2, 3]
di = dict()
di['a'] = "A"


def my_func():
    print("x,y的值为{},{}".format(x, y))
    # 输出结果：x,y的值为10,20

    # 以下代码无法通过
    # x = 15
    # print("x的值为{}".format(x))

    print(li)
    li.append('4')
    print(li)

    print(di)
    # di = dict()
    # print(di)


if __name__ == '__main__':
    my_func()
