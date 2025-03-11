# 说明：

安装xpinyin库：

```
pip install xpinyin
# or
poetry add xpinyin
```

使用方法：

```
from xpinyin import Pinyin

p = Pinyin()

text = "你好，世界！"

pinyin = p.get_pinyin(text)

print(pinyin)
```

输出：

```
ni3 hao3, shi4 jie4!
