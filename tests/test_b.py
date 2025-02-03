"""
 * @file   : test_a.py
 * @time   : 13:28
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import pytest

"""
1. 缺省的方法setup和teardown,不需要为其指定@pytest.fixture;(如果指定了@pytest.fixture 就不能自动加载了。)
2. 缺省的方法setup和teardown的scope是函数级别的。
3. 同时，在被测试的业务逻辑方法上也不用连接setup和teardown,被测试方法会自动加载setup和teardown
"""


@pytest.fixture(scope='function')
def setup_function():
    print('my_function called.')


def setup():
    print('')
    print('setup called.')


def teardown():
    print("teardown called.")


def test_foo():
    print()
    print("i am in test_foo")


def test_bar():
    print()
    print("i am in test_bar")
