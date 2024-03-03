"""
 * @file   : 1.__import__.3.py
 * @time   : 17:11
 * @date   : 2021/12/26
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

package_path = "IMPORT研究.archives.sub_arch"
fromlist = ["say_hello"]
package = __import__(name=package_path, fromlist=fromlist)
print("返回值为：")
print(package)
print("通过返回的模块信息，继续操作模块内的功能")
package.say_hello()


# --output--
# in archives using __init__
# in sub_arch using __init__
# 返回值为：
# <module 'IMPORT研究.archives.sub_arch' from 'E:\\myworkspace\\MyStudy\\Python\\IMPORT研究\\archives\\sub_arch\\__init__.py'>
# 通过返回的模块信息，继续操作模块内的功能
# in sub_arch say hello

"""
说明
给__import__指定name参数和fromlist参数的时候：
name属性加载到子包"IMPORT研究.archives.sub_arch"上，实际是加载子包的初始化文件__init__.py文件
接下来的事情，跟 1.__import__.2.py 内的逻辑相同。
"""
