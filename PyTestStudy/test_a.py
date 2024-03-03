"""
 * @file   : test_a.py
 * @time   : 13:28
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import pytest


@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print("teardown_function called.")

    request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
    print('setup_function called.')


def test_foo(setup_function):
    print("i am in test_foo")
