"""
 * @file   : abc.py
 * @time   : 下午9:24
 * @date   : 2024/5/1
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class MyAbc(object):
    def __init__(self, arg: str):
        self.arg = arg

    pass

    def func_name(self, arg_name: str):
        _arg_name = arg_name
        _handler = self


if __name__ == '__main__':
    pass
