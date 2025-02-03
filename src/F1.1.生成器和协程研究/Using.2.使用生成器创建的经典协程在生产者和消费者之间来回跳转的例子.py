"""
 * @file   : Using.1.使用生成器创建的经典协程在生产者和消费者之间来回跳转的例子.py
 * @time   : 9:24
 * @date   : 2024/2/21
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


def producer():
    print("[P] 厂家上线")
    r = 'OK...'
    while True:
        n = yield r  # 第一次send（None）的时候，会激活generator，并返回 yield r 的值；但不会将None赋值给n
        print(f"[P] 厂家生成和发货: {n}")
        r = n


def consumer(p: producer):
    print("[C] 消费者上线")

    ## 消费者联系厂家（启动generator）
    # start_value = next(p)
    start_value = p.send(None)
    print(f"[C/P]双方建立联系 {start_value}")
    print("──分割线───────────────────────────────────")

    n = 0
    while n < 3:
        n += 1
        print(f"[C] 消费者下单: {n}")
        r = p.send(n)
        print(f"[C] 消费者收货: {r}")
        print("──分割线───────────────────────────────────")
    pass

    # 关闭generator
    p.close()


if __name__ == '__main__':
    my_producer = producer()
    consumer(my_producer)
pass
