def display_name():
    # print(f"我是在moduleA中执行的代码，我的__name__为:{__name__}")
    print("__name__:{0}".format(__name__))
    print("__package__:{0}".format(__package__))
    print("__file__:{0}".format(__file__))
    # print("__path__:{0}".format(__path__))


if __name__ == '__main__':
    display_name()

# output
# __name__:__main__
# __package__:None
# __file__:D:\HOME\MySpace\Study.PY\src\02.内置功能研究\01.常用的魔术方法研究\biz.py
