"""
 * @file   : 从kwargs内提前参数.py
 * @time   : 11:51
 * @date   : 2023/7/19
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# +--------------------------------------------------------------------------
# |::::TIPS::::| 定义函数和调用函数时，**表示不同的意思（一个表示接受剩余参数，一个用来表示解包）
# ---------------------------------------------------------------------------
# 1. 定义函数时使用的关键字参数中的两个星号（**），表示用来接受所有关键字参数（即字典类型的剩余参数）的意思。
# 2. 调用函数时：a.可以分别给关键字参数来传递数据，例如：get_data(query='AAPL', query_type='stock')。
#     b.也可以使用一部字典来一次性传递所有关键字参数，例如：get_data(**{'query': 'AAPL', query_type='stock'}),
#       但这个时候，必须在字典的前面加上一个**符号，这里的**表示解包的意思（就是将字典解包成各个独立的元素分别传入）。
# +--------------------------------------------------------------------------

def get_data(**kwargs):
    retry = kwargs.get('retry', 10)
    sleep = kwargs.get('sleep', 0)
    question = kwargs.get('query')
    log = kwargs.get('log', False)
    query_type = kwargs.get('query_type', 'stock')
    cookie = kwargs.get('cookie', None)
    request_params = kwargs.get('request_params', {})

    print("获取到的信息为：")

    print(retry)
    print(cookie)
    print(sleep)
    print(question)
    print(log)
    print(query_type)
    print(request_params)


pass

if __name__ == '__main__':
    # 1. 字典参数，各个字典元素可以分别传入。
    get_data(retry=8, sleep=0, query='股票户', log=False, query_type='stock', cookie=None, request_params={})

    print("──分割线───────────────────────────────────")

    # 2. 如果统一成字典，再传入，则需要使用 两个星号（**）的方式进行解包（就是将字典解包成各个独立的元素分别传入）。
    my_kwargs = {'retry': 8, 'sleep': 0, 'query': '股票户', 'log': False, 'query_type': 'stock', 'cookie': None,
                 'request_params': {}}
    get_data(**my_kwargs)
pass
