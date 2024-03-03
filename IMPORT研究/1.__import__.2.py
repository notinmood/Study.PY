"""
 * @file   : 1.__import__.2.py
 * @time   : 17:11
 * @date   : 2021/12/26
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

package_path = "IMPORT研究.archives.routine"
fromlist = ["say_hello"]
package = __import__(name=package_path, fromlist=fromlist)
print("返回值为：")
print(package)
print("通过返回的模块信息，继续操作模块内的功能")
package.say_hello()
package.say_bye()

# --output--
# in archives using __init__
# in routine
# 返回值为：
# <module 'IMPORT研究.archives.routine' from 'E:\\myworkspace\\MyStudy\\Python\\IMPORT研究\\archives\\routine.py'>
# 通过返回的模块信息，继续操作模块内的功能
# in routine say hello

"""
说明
给__import__指定name参数和fromlist参数的时候：
1. 会加载name指定路径上所有的逻辑；
2. 并且__import__的返回值是'IMPORT研究.archives.routine' 这个最低成的模块
3. 可以通过返回的模块，继续操作 fromlist 内的功能(比如此处的say_hello功能)
4. 没有在 fromlist 内的功能指定的功能(比如此处的 say_bye，居然也加载成功了，奇怪！！！)
"""
