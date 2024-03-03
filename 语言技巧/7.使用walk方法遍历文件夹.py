"""
 * @file   : 7.使用walk方法遍历文件夹.py
 * @time   : 21:52
 * @date   : 2023/12/16
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os

from BasicLibrary.projectHelper import ProjectHelper

if __name__ == '__main__':
    """
    以下代码演示了，如果使用os模块的walk方法，来遍历文件夹。
    其中本段代码已经做成了snippet，输入“walk”，1秒后再点击回车，可以直接将以下代码插入到编辑器中。
    """
    project_root = ProjectHelper.get_root_physical_path()

    for dir_path, dir_names, file_names in os.walk(project_root):
        for filename in file_names:
            print(filename)
            print(dir_path + '\\' + filename)
            print("-------------------------------------------------------")
        pass
    pass
