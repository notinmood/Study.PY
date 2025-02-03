"""
 * @file   : OK.await使用.3.等待协程任务简化.py
 * @time   : 12:22
 * @date   : 2024/2/19
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import asyncio
import time


async def say_after(delay, what):
    """

    :param delay:
    :param what:
    :return:
    """
    await asyncio.sleep(delay)
    print(what)


async def main():
    """

    :return:
    """

    print(f"started at {time.strftime('%X')}")

    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    # 使用asyncio.wait的方式对放入EventLoop中的协程进行分别等待
    await asyncio.wait([task1, task2])

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())  # 时间跨度2秒
pass
