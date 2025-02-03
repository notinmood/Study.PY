"""
 * @file   : index.py
 * @time   : 19:15
 * @date   : 2024/12/22
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from 模块的相对导入与绝对导入.packageB.bar import Bar
from 模块的相对导入与绝对导入.moduleB.boo import Boo

if __name__ == '__main__':
    Bar.fb()
    Boo.fb()
