"""
 * @file   : 1.默认情形下type是class的元类.py
 * @time   : 下午6:39
 * @date   : 2024/6/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# | 元类是用来创建类的。本代码展示了默认情形下type是class的元类。
# +--------------------------------------------------------------------------

class MyClass(object):
    def foo(self):
        _self = self
        print("foo")

    pass


pass

if __name__ == '__main__':
    obj = MyClass()

    print(type(obj))  # <class '__main__.MyClass'>
    print(type(MyClass))  # <class 'type'>
