"""
 * @file   : foo.py
 * @time   : 19:17
 * @date   : 2024/12/22
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class Too(object):
    @staticmethod
    def ma(arg_name: str = "default_arg_name"):
        print("This is a static method in moduleA")
        return f"This is a function in moduleA, arg_name is {arg_name}"

    pass


pass
