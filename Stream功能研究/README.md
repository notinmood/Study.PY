# 说明：
▌参考资料：https://zhuanlan.zhihu.com/p/688235805

## 介绍

使用过Java的stream流处理后，真觉得这种管道形式的链式调用是贼爽，再也不用一层层的嵌套for循环和if条件再组装。

再到Python开发中，要么老老实实的for循环嵌套，要么高阶函数层层套娃，其中可能还夹杂着lamda函数、列表生成式。一段时间后自己阅读起来都感觉困难重重。

然后，网上找到了如下的第三方库：SuperStream，官网地址：https://shimada666.github.io/super-stream/

特点和使用的API官网都有详细介绍，此处大致罗列下API和具体实践。

## 安装

```shell
poetry add superstream
```

## 使用

### 1. 基本使用

```python
from superstream import Stream

# 1. 创建Stream对象
s = Stream([1, 2, 3, 4, 5])

# 2. 筛选
s.filter(lambda x: x % 2 == 0).map(lambda x: x ** 2).to_list()  # [4, 16]

# 3. 排序
s.sorted().to_list()  # [1, 2, 3, 4, 5]

# 4. 去重
s.distinct().to_list()  # [1, 2, 3, 4, 5]

# 5. 切片
s.slice(1, 3).to_list()  # [2, 3]

# 6. 映射
s.map(lambda x: x ** 2).to_list()  # [1, 4, 9, 16, 25]

# 7. 聚合
s.reduce(lambda x, y: x + y)  # 15

# 8. 遍历
s.foreach(lambda x: print(x))  # 1 2 3 4 5
```

### 2. 多级流

```python
from superstream import Stream

# 1. 创建Stream对象
s1 = Stream([1, 2, 3])
s2 = Stream([4, 5, 6])

# 2. 多级流
s = s1.zip(s2).map(lambda x: x[0] + x[1]).to_list()  # [5, 7, 9]
```

### 3. 并行流

```python
from superstream import Stream
import concurrent.futures

# 1. 创建Stream对象
s = Stream([1, 2, 3, 4, 5])

# 2. 并行流
with concurrent.futures.ProcessPoolExecutor() as executor:
    result = s.map(lambda x: x ** 2, executor=executor).to_list()  # [1, 4, 9, 16, 25]
```

## 总结

SuperStream库提供了丰富的API，可以让我们在Python中使用流式处理，提高代码的可读性和可维护性。
