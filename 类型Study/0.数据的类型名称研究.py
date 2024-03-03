import types
from builtins import *


def my_function(arg_name: str):
    return arg_name


pass

if __name__ == '__main__':
    print("──使用types枚举查看数据的类型信息───────────────────────────────────")
    # 1. 使用types枚举查看数据类型
    print(types.BuiltinFunctionType)
    print(types.FunctionType)

    print(types.BuiltinMethodType)
    print(types.MethodType)

    # 内置的BuiltinMethodType和BuiltinFunctionType是一样的。
    if types.BuiltinMethodType == types.BuiltinFunctionType:
        print("YYY,types.BuiltinMethodType== types.BuiltinFunctionType")
    else:
        print("NNN,types.BuiltinMethodType!= types.BuiltinFunctionType")
    pass

    print("──使用type函数获取数据的类型信息───────────────────────────────────")
    # 2. 使用type函数获取数据类型
    print(type(1))
    print(type(my_function))

    # 3. 使用isinstance函数判断数据类型
    if isinstance(1, int):
        print("YYY,1 是int类型")
    else:
        print("NNN,1不是int类型")
    pass

    if isinstance(my_function, types.FunctionType):
        print("YYY,my_function 是函数类型")
    else:
        print("NNN,my_function不是函数类型")
    pass

    if isinstance(my_function, types.BuiltinFunctionType):
        print("YYY,my_function 是内置的函数类型")
    else:
        print("NNN,my_function不是内置的函数类型")
    pass
