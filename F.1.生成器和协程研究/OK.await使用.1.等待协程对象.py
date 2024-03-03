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
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    print(f"middle at {time.strftime('%X')}")
    # +--------------------------------------------------------------------------
    # |::::TIPS::::| 本代码的使用说明
    # ---------------------------------------------------------------------------
    # 此时，事件循环中还没有task-2这个任务，因此EventLoop只能在Task-main和task-1之间反复查询和执行
    # +--------------------------------------------------------------------------
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    # 1： 创建事件循环，传入入口点main()协程对象,此时生成一个对应的task
    asyncio.run(main())  # 时间跨度3秒
pass
