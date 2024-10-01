"""
 * @file   : 1.使用Thread进行基础的子线程开启.py
 * @time   : 15:12
 * @date   : 2023/12/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from threading import Thread, current_thread


# join()方法。等待join的线程执行完毕后再继续执行下面的代码（包括主线程和其他子线程）或者结束程序

def worker(name: str, num: int) -> None:
    for i in range(num):
        print(f"我在线程【{name}】中执行,第{i}次；但我真正的名字是:【{current_thread().name}】")
    pass


def no_join():
    t1 = Thread(target=worker, args=('T1', 30,), name='线程t1')
    t2 = Thread(target=worker, args=('T2', 30,))
    t1.start()
    t2.start()
    worker('main', 3)
    # 可以看到，主线程和各个子线程是交替执行的


def using_join():
    t1 = Thread(target=worker, args=('T1', 30,), name='线程t1')
    t2 = Thread(target=worker, args=('T2', 30,))
    t1.start()
    t1.join()  # 等待t1线程执行完毕后再执行t2线程
    t2.start()
    t2.join()  # 等待t2线程执行完毕后再结束程序
    worker('main', 3)
    # 可以看到，主线程和各个子线程是顺序执行的


if __name__ == '__main__':
    no_join()
    print("──分割线───────────────────────────────────")
    using_join()
