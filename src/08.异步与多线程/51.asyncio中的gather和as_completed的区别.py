"""
 * @file   : 51.asyncio中的gather和as_completed的区别.py
 * @time   : 10:16
 * @date   : 2024/10/17
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

# +--------------------------------------------------------------------------
# |::::TIPS::::| 本代码的使用说明
# ---------------------------------------------------------------------------
# 1. gather和as_completed都是用来处理asyncio.Future的工具函数。
# 2. gather将多个任务合并在一起处理，当所有任务都完成时，才使用tuple的方式返回结果。因此需要再gather上进行await等待。
# 3. as_completed是将多个任务分别处理，分别返回结果：当某个任务完成时，返回该任务的结果。因此await不在as_completed上使用,而在for循环的某个结果的等待上使用。
# +--------------------------------------------------------------------------
import asyncio


async def task1():
    await asyncio.sleep(1)
    return 1


async def task2():
    await asyncio.sleep(2)
    return 2


async def task3():
    await asyncio.sleep(3)
    return 3


async def main():
    tasks = [task1(), task2(), task3()]
    # # 1.使用gather将多个任务合并在一起处理和返回结果（直接在gather上使用await等待）
    # results = await asyncio.gather(*tasks)
    # print(results)

    ##  2.使用as_completed将多个任务分别处理，分别返回结果（在具体某个结果上使用await等待）
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)
    pass


if __name__ == '__main__':
    asyncio.run(main())
