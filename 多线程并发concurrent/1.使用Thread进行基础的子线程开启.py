"""
 * @file   : 1.使用Thread进行基础的子线程开启.py
 * @time   : 15:12
 * @date   : 2023/12/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from threading import Thread, current_thread


# TODO:xiedali@2023/12/13 研究Thread.join()方法的使用

def worker(name: str, num: int) -> None:
    for i in range(num):
        print(f"我在线程【{name}】中执行,第{i}次；但我真正的名字是:【{current_thread().name}】")
    pass


if __name__ == '__main__':
    t1 = Thread(target=worker, args=('T1', 30,), name='线程t1')
    t2 = Thread(target=worker, args=('T2', 30,))
    t1.start()
    t2.start()
    worker('main', 30)
    # 可以看到，主线程和各个子线程是交替执行的
