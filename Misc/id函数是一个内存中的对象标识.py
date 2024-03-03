# id表示内存中的对象标识(可以认为对象在内存中的地址)

# 相同的对象，在内存中是同一个地址。
# 不同的对象，在内存的地址不同。

if __name__ == '__main__':
    myName1 = "zhangsan"
    myName2 = "zhangsan"

    yourName = "lisi"

    # 以下打印的结果是相同的
    print(id(myName1))
    print(id(myName2))

    print(id(yourName))
