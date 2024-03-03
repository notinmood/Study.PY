"""
 * @file   : base64模块内的方法3.b64encode和b64decode.py
 * @time   : 11:03
 * @date   : 2024/1/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import base64

# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 1. base64.b64encode(bytes)->bytes 接收一个普通字节串（比如二进制图片信息），返回base64编码后的字节串。方法中的b表示byte。
# 2. base64.b64decode(bytes)->bytes 接收一个经过base64编码的字节串，返回解码后的普通字节串
#
# ** 注意：**
# b64encode/b64decode方法只能处理bytes类型的数据，其主要的应用场景之一是处理图片文件的base64编码和解码。
# +--------------------------------------------------------------------------

if __name__ == '__main__':
    print("──1.1. 对纯英文字符串，可以使用b关键字快速转字节串，然后进行base64编码解码───────────────────────────────────")
    my_bytes = b"Hello, world!"
    my_base64_bytes = base64.b64encode(my_bytes)

    print(type(my_base64_bytes))
    print(my_base64_bytes)

    my_bytes = base64.b64decode(my_base64_bytes)
    print(type(my_bytes))
    print(my_bytes)

    print("──分割线───────────────────────────────────")

    print("──1.2. 对纯英文字符串，也可以使用明确的方法转字节串，然后进行base64编码解码───────────────────")
    my_str = "Hello, world!"
    my_bytes = my_str.encode(encoding="utf-8")
    my_base64_bytes = base64.b64encode(my_bytes)

    print(type(my_base64_bytes))
    print(my_base64_bytes)

    my_bytes = base64.b64decode(my_base64_bytes)
    print(type(my_bytes))
    print(my_bytes)

    my_str = my_bytes.decode(encoding="utf-8")
    print(type(my_str))
    print(my_str)

    print("──分割线───────────────────────────────────")

    print("──2. 对中文字符串需要先明确转成字节串，再进行base64编码解码───────────────────────────────────")
    my_str = "你好，世界！"
    my_bytes = my_str.encode("utf-8")
    my_base64_bytes = base64.b64encode(my_bytes)
    print(type(my_base64_bytes))
    print(my_base64_bytes)

    my_bytes = base64.b64decode(my_base64_bytes)
    print(type(my_bytes))
    print(my_bytes)

    my_str = my_bytes.decode("utf-8")
    print(type(my_str))
    print(my_str)


# TODO:xiedali@2024/01/21 写一个读取图片文件，然后进行base64编码解码的代码。
