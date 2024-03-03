"""
 * @file   : 0.common.2.py
 * @time   : 17:55
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from IMPORT研究.archives.sub_dir.bar import say_hello

say_hello()
print("i am in 0.common.3.py")

# 以下为本py运行结果：
# in archives using __init__
# in bar.py
# in sub_dir/bar say hello
# i am in 0.common.3.py

"""
从上面的结构可以得出结论：
使用from import导入模块和功能的时候在0.common.1.py的基础上：
1. 先执行最外层的软件包内的逻辑(本例中的 in archives using __init__)
2. 但内层是一个子目录，不是子包，因此本例没有2例中出现的"in sub_arch using __init__"
"""

