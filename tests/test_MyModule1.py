"""
 * @file   : test_MyModule1.py
 * @time   : 12:36
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import pytest

"""
本文件的目的是演示"固定设置"fixture 的作用范围，其共有：
function：每个test都运行，默认是function的scope
class：每个class的所有test只运行一次
module：每个module的所有test只运行一次
session：每个session只运行一次(本文件没有演示session)

作者：红薯爱帅
链接：https://www.jianshu.com/p/a754e3d47671
"""


# 通过scope="function"(或者默认不指定具体值) 定义每个function都会使用的"固定设置"
@pytest.fixture()
def setup_function():
    print("I am in setup_function")


# 通过scope="class" 定义在同一个class内，仅仅会调用一次的"固定设置"
@pytest.fixture(scope="class")
def setup_class():
    print("I am in setup_class")


@pytest.fixture(scope="module")
def setup_module():
    print("I am in setup_module")


class TestMyClass:
    """
    以下两个方法 test_f_foo 和 test_f_bar，测试的时候分别调用setup_function
    通过结果，可以发现setup_function确实执行了两次
    """

    def test_f_foo(self, setup_function):
        print("I am in test_f_foo")

    def test_f_bar(self, setup_function):
        print("I am in test_f_bar")

    """
    以下两个方法 test_c_foo 和 test_c_bar，测试的时候分别调用 setup_class
    通过结果，可以发现 setup_class 仅在第一次被调用的时候执行了执行了一次。
    """

    def test_c_foo(self, setup_class):
        print("I am in test_c_foo")

    def test_c_bar(self, setup_class):
        print("I am in test_c_bar")

    """
    以下代码(test_m_foo)连同 TestYourClass 内的 test_m_bar 演示同一个模块(同一个模块就是同一个文件)内分别调用 setup_module
    通过结果，可以发现 setup_module，仅执行了一次(同一个模块的其他类型(方法)再次调用 setup_module 时，没有被再次执行).
    """

    def test_m_foo(self, setup_module):
        print("I am in {0} {1}".format(__class__, __name__))

    """
    以下代码演示，一个被测方法(test_c_bar)可以调用多个"固定设置"(setup_class, setup_function)
    """

    def test_c_bar(self, setup_class, setup_function):
        print("I am in test_c_bar")


class TestYourClass:
    """
    本方法(test_m_bar)是配合 TestMyClass.test_m_foo，演示 setup_module 的使用.
    结论：只要在同一个模块内(即便是夸Class),多次调用 setup_module,但只有第一次调用的时候才会被执行
    """

    def test_m_bar(self, setup_module):
        print("I am in {0} {1}".format(__class__, __name__))
