"""
 * @file   : base64模块内的方法2.encodestring和decodestring.py
 * @time   : 10:22
 * @date   : 2024/1/21
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import base64

# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# python3.9之后，base64模块内的方法encodestring和decodestring已经被移除了。
# 可以通过手动实现的方式，思路如下：
# 1. 先将字符串encode为普通字节串
# 2. 然后将普通字节串使用base64.b64encode进行编码为base64字节串
# +--------------------------------------------------------------------------

if __name__ == '__main__':
    my_str = "你好，世界！"

    print("──1. 编码过程───────────────────────────────────")
    my_common_bytes = my_str.encode("utf-8")  # 可以采用的编码方式有多种，最常用的为 utf-8
    print(f"普通字节码为：{my_common_bytes}")
    my_base64_bytes = base64.b64encode(my_common_bytes)
    print(f"base64字节码为：{my_base64_bytes}")

    print("──解码过程───────────────────────────────────")
    my_common_bytes = base64.b64decode(my_base64_bytes)
    print(f"普通字节码为：{my_common_bytes}")
    my_str = my_common_bytes.decode("utf-8")
    print(f"普通字符串为：{my_str}")
