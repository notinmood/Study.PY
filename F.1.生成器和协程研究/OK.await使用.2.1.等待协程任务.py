"""
 * @file   : OK.T.1.py
 * @time   : 9:12
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

    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # +--------------------------------------------------------------------------
    # |::::TIPS::::| 本代码的使用说明
    # ---------------------------------------------------------------------------
    # 此时，事件循环中已经有3个任务了，因此EventLoop只能在Task-main和task-1、task-2之间反复查询和执行
    # +--------------------------------------------------------------------------

    await task1
    # 虽然EventLoop里面在task1运行的时候，task2也在运行。
    # 但此处print(f"middle-1 at {time.strftime('%X')}")是不运行的，直到task1结束
    print(f"middle-1 at {time.strftime('%X')}")
    await task2
    print(f"middle-2 at {time.strftime('%X')}")

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main())  # 时间跨度2秒
pass
