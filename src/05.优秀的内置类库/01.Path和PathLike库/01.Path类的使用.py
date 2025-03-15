"""
 * @file   : 01.Path类.py
 * @time   : 下午2:16
 * @date   : 2024/4/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from pathlib import Path

# 创建Path对象
if __name__ == '__main__':
    here = Path(__file__).resolve()

    print("当前文件路径:")
    print(here)  # 当前文件路径

    print("当前文件父目录路径")
    print(here.parent)  # 当前文件父目录路径

    print("当前文件名")
    print(here.name)  # 当前文件名

    print("当前文件名（不含扩展名）")
    print(here.stem)  # 当前文件名（不含扩展名）

    print("当前文件扩展名")
    print(here.suffix)  # 当前文件扩展名

    print("当前文件路径的各个部分")
    print(here.parts)  # 当前文件路径的各个部分

    print("当前文件路径的根目录")
    print(here.anchor)  # 当前文件路径的根目录

    print("当前文件路径的驱动器")
    print(here.drive)  # 当前文件路径的驱动器

    print("当前文件路径的根目录")
    print(here.root)  # 当前文件路径的根目录

    print("当前文件父目录路径 (等价于 parent)")
    print(here.parents[0])  # 当前文件父目录路径 (等价于 parent)

    print("当前文件父目录的父目录路径")
    print(here.parents[1])  # 当前文件父目录的父目录路径

    print("当前文件父目录的父目录的父目录路径")
    print(here.parents[2])  # 当前文件父目录的父目录的父目录路径
