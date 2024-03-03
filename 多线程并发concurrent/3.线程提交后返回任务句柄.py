"""
 * @file   : 3.线程提交后返回任务句柄.py
 * @time   : 8:24
 * @date   : 2023/6/22
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from concurrent.futures import ThreadPoolExecutor
import time


# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)

# 通过submit函数提交执行的功能（用方法形式表示的功能）到线程池中，submit函数立即返回任务句柄，不阻塞
task1 = executor.submit(get_html, 3)
task2 = executor.submit(get_html, 2)

# done方法用于判定某个任务是否完成
print(task1.done())  # False,因为task1内有延时操作，此时立即判断的话肯定是未完成
print(task2.done())  # False,因为task2内有延时操作，此时立即判断的话肯定是未完成

# cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功
print(task2.cancel())  # False,因为task2差收入程序中，此时立即not in the thread pool，取消失败

# 4s 后打印task1是否完成
time.sleep(4)
print(task1.done())  # True,因为task1内的延时操作时间已到，此时Task1已经完成

# result方法可以获取task的执行结果
print(task1.result())

# 执行结果
# False  # 表明task1未执行完成
# False  # 表明task2取消失败，因为已经放入了线程池中
# get page 2s finished
# get page 3s finished
# True  # 由于在get page 3s finished之后才打印，所以此时task1必然完成了
# 3     # 得到task1的任务返回值
