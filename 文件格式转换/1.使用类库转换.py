"""
 * @file   : index.py
 * @time   : 19:36
 * @date   : 2024/1/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os

import pypandoc

if __name__ == '__main__':
    print("Hello, world!")
    print(pypandoc.__version__)

    # # 1. 转换跟本文件同目录下的markdown文件到word
    # here = os.path.abspath(os.path.dirname(__file__))

    # # 2. 转换其他目录下的MarkDown文件
    # here = os.path.abspath(os.path.dirname(__file__))
    # here = os.path.join(here, "_res")
    #
    # source_file_full_name = os.path.join(here, 'res.README.md')
    # output_file_full_name = os.path.join(here, 'out.README.docx')

    # 3. 转换其他目录下的MarkDown文件
    source_file_full_name = r'Z:\mm\res.README.md'
    output_file_full_name = r'Z:\mm\res.README.docx'

    # 执行逻辑
    pypandoc.convert_file(source_file=source_file_full_name, to='docx', outputfile=output_file_full_name)
