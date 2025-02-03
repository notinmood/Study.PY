"""
 * @file   : bar.py
 * @time   : 19:17
 * @date   : 2024/12/22
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

# from  .. moduleA.too import Too
from 模块的相对导入与绝对导入.moduleA.too import Too


class Boo(object):
    @staticmethod
    def fb(arg_name: str = "default_name"):
        Too.ma()

        print("This is a static method in moduleB")
        return f"This is a function in moduleB, arg_name is {arg_name}"

    pass


pass
