"""
 * @file   : 4.使用as_completed查询任务完成情况.py
 * @time   : 21:55
 * @date   : 2023/6/22
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("in subroutine: get page {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 6, 5, 4]  # 并不是真的url
all_task = [executor.submit(get_html, url) for url in urls]

# print("get page {}s finished".format(all_task[0].result()))
print("all_task: ", all_task, type(all_task))

for future in as_completed(all_task):
    data = future.result()
    print("in main: get page {}s success".format(data))

# max_workers 很小的时候，会按照任务的加入线程池得到先后顺序进行执行
# 以下是max_workers=2时候的结果：
# in subroutine: get page 2s finished
# in main: get page 2s success
# in subroutine: get page 3s finished
# in main: get page 3s success
# in subroutine: get page 6s finished
# in subroutine: get page 5s finished
# in main: get page 5s success
# in main: get page 6s success
# in subroutine: get page 4s finished
# in main: get page 4s success









# 2. max_workers 足够大了的时候，会并行执行。以下是 max_workers =10的结果：

# 执行结果
# in subroutine: get page 2s finished
# in main: get page 2s success
# in subroutine: get page 3s finished
# in main: get page 3s success
# in subroutine: get page 4s finished
# in main: get page 4s success
# in subroutine: get page 5s finished
# in main: get page 5s success
# in subroutine: get page 6s finished
# in main: get page 6s success
