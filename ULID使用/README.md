# 说明：

本文档是关于ULID的介绍，主要介绍ULID的概念、特性、优点、以及如何使用ULID。

## ULID是什么？

ULID（Universally Unique Lexicographically Sortable Identifier）是一种基于时间戳、随机数、机器ID和序号的UUID（Universally
Unique Identifier）的变种。

## ULID有什么优点？

- 全局唯一：ULID保证了在任意时刻生成的ID都是唯一的，不会重复。
- 时间戳：ULID使用48位时间戳，可以保证生成的ID在任意时刻都是唯一的。
- 随机数：ULID使用80位随机数，可以保证生成的ID在任意时刻都是唯一的。
- 序号：ULID使用16位序号，可以保证生成的ID在同一时间戳下是唯一的。
- 易读性：ULID使用32位、8位、2位、2位、10位、6位的编码，可以方便地阅读和记忆。

## ULID安装

ULID可以使用pip安装：

```
pip install ulid-py
```
或者poetry安装：

```
poetry add ulid-py
```

## ULID如何使用？

ULID的使用非常简单，只需要生成一个ULID，就可以使用它。

```python
import ulid

ulid.new()
```

生成的ULID是一个字符串，可以直接使用。

```python
ulid.new()
'01BX5ZZKBKACTAV9WEVGEMMVRY'
```

## 参考资料

- [ULID: A Universally Unique Lexicographically Sortable Identifier](https://github.com/ulid/spec)
- [ULID in Python](https://github.com/ahawker/ulid)

