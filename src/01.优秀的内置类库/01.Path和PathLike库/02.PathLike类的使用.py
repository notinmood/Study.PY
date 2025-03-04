import os
from os import PathLike
from pathlib import Path

from BasicLibrary.projectHelper import ProjectHelper


# 定义一个使用PathLike的函数
def process_path(path: PathLike) -> None:
    # 将PathLike转换为Path对象
    path = Path(path)
    # 处理Path对象
    print(path.name)


# 测试可以给PathLike对象传递：字符串、Path对象、os.path.join()结果
if __name__ == '__main__':
    root_path = ProjectHelper.get_root_physical_path()
    file_path = root_path + r'src/_res/00.人民日报.Cover.jpg'
    process_path(file_path)  # 输出：file.txt
    process_path(Path(file_path))  # 输出：file.txt
    process_path(os.path.join(root_path, file_path))  # 输出：file.txt
