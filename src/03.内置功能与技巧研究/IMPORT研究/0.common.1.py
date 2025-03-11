"""
 * @file   : 0.common.1.py
 * @time   : 17:55
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from IMPORT研究.archives.routine import say_hello

say_hello()
print("i am in 0.common.1.py")
# 以下为本py运行结果：
# in archives using __init__
# in routine
# in routine say hello
# i am in 0.common.1.py

"""
从上面的结构可以得出结论：
使用from import导入模块和功能的时候会：
1. 先加载包内的逻辑(如果有可以自动执行的逻辑，就直接执行,比如本例中的 print('in archives using __init__'))
2. 再加载模块内的逻辑(如果有可以自动执行的逻辑，就直接执行,比如本例中的 print('in routine'))
3. 最后执行指定的方法等逻辑(比如本例方法调用 say_hello() 和本地代码执行 print("i am in 0.common.1.py"))
"""

