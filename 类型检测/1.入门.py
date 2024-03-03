"""
 * @file   : 1.入门.py
 * @time   : 9:12
 * @date   : 2023/12/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


def greeting(name: str) -> str:  # 这里提示有问题
    print(f'Hello {name}')


x: str = 'xxx'
y: int = "yyy"  # 这里应该提示有问题
greeting(x)
greeting(y)  # 这里应该提示有问题
