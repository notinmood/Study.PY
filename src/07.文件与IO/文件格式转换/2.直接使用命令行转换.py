"""
 * @file   : 2.直接使用命令行转换.py
 * @time   : 21:40
 * @date   : 2024/1/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os

if __name__ == '__main__':
    print("Hello, world!")
    here = os.path.abspath(os.path.dirname(__file__))
    source_file_full_name = os.path.join(here, 'res.README.md')
    output_file_full_name = os.path.join(here, 'out.README.docx')
    os.system("pandoc " + source_file_full_name + " -o " + output_file_full_name)
