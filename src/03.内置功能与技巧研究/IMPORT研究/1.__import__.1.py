"""
 * @file   : 1.__import__.1.py
 * @time   : 17:11
 * @date   : 2021/12/26
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

package_path = "IMPORT研究.archives.routine"
package = __import__(name=package_path)
print("返回值为：")
print(package)

# 以下语句会出现错误，因为当前package为"IMPORT研究"这个级别
# package.say_hello()

# --output--
# in archives using __init__
# in routine
# 返回值为：
# <module 'IMPORT研究' (<_frozen_importlib_external._NamespaceLoader object at 0x000001481491C370>)>

"""
说明
只给__import__指定name参数的时候：
1. 会加载name指定路径上所有的逻辑；
2. 但__import__的返回值是'IMPORT研究'这个顶级的模块
3. 但如果在这个返回的模块上调用routine内的功能say_hello(),系统会报错
"""

