"""
 * @file   : 字符串分割.py
 * @time   : 上午9:11
 * @date   : 2024/4/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.listHelper import ListHelper

if __name__ == '__main__':
    s = "hello\nworld"
    print(s)
    print(s.split('\n'))

    print("──分割线───────────────────────────────────")
    s = "hello,world\n"
    print(s)

    result = s.split('\n')
    print(result)

    fixed = ListHelper.remove_item(result, '')
    print(fixed)

    print("──分割线───────────────────────────────────")
    s = "hello world"
    print(s)
    print(s.split('\n'))
