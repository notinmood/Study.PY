"""
 * @file   : bar.py
 * @time   : 19:17
 * @date   : 2024/12/22
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

## 如下使用了相对导入，在IDE中显示没有问题， 但是在命令行运行时会报错，提示找不到模块
# from .. packageA.foo import Foo
# from tao import Tao

## 正确的导入方式是使用绝对导入，如下：
from 模块的相对导入与绝对导入.packageA.foo import Foo
from 模块的相对导入与绝对导入.packageB.tao import Tao

class Bar(object):
    @staticmethod
    def fb(arg_name: str = "default_name"):
        Foo.fa()
        Tao.ta()

        print("This is a static method in packageB")
        return f"This is a function in packageB, arg_name is {arg_name}"

    pass


pass
