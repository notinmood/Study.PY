"""
 * @file   : 50.asyncio的使用流程.py
 * @time   : 9:29
 * @date   : 2024/10/17
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import asyncio


# 1.定义处理具体问题的协程函数
async def handle_request(request_data):
    # 处理请求
    print(f"Handling request {request_data}")
    # 模拟耗时操作
    await asyncio.sleep(1)
    # 返回结果
    return f"Result for request {request_data}"


# 2.创建任务
async def main():
    ## 方式1：使用create_task语法手动创建任务

    # task1 = asyncio.create_task(handle_request(1))
    # task2 = asyncio.create_task(handle_request(2))
    # task3 = asyncio.create_task(handle_request(3))
    #
    # await task1
    # await task2
    # await task3
    #
    # # 获取结果
    # print(f"Task 1 returned result {task1.result()}")
    # print(f"Task 2 returned result {task2.result()}")
    # print(f"Task 3 returned result {task3.result()}")

    # 方式2.1：使用asyncio.gather语法自动创建任务（各个结果统一等待）
    results = await asyncio.gather(handle_request(1), handle_request(2), handle_request(3))
    print(f"Results: {results}")

    # 方式2.2：使用asyncio.as_completed语法自动创建任务（各个结果分别等待）
    results = asyncio.as_completed([handle_request(1), handle_request(2), handle_request(3)])
    for result in results:
        print(f"Result: {await result}")
    pass


if __name__ == '__main__':
    # 3.创建和运行事件循环
    asyncio.run(main())
