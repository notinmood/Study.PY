"""
 * @file   : index.py
 * @time   : 18:30
 * @date   : 2024/1/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import subprocess

import os

# TODO:xiedali@2024/01/10 其他几种跟系统交互的方式可以继续探讨

if __name__ == '__main__':
    # 将当前目录切换到指定目录
    os.chdir(r"z:\我们的目录")
    print(os.path.abspath(os.curdir))

    # 使用os.system()在指定目录下执行pandoc等命令
    input_file_path = r'00.README.md'
    out_file_path = r'我的word文件.docx'
    os.system('pandoc ' + '"' + input_file_path + '"' + ' -o ' + out_file_path)
