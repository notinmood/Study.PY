说明：

特别说明：
//TODO:xiedali@2023-12-08 是否JetBrains本是就支持mypy？

使用mypy进行静态类型检测。

安装：`pip install mypy`



使用方法：


在项目根目录下创建`mypy.ini`文件，内容如下：

```ini
[mypy]
# 开启类型检查
check_untyped_defs = True
# 开启类型提示
show_error_context = True
# 开启类型提示
show_error_codes = True
# 开启类型提示
show_column_numbers = True
# 开启类型提示
ignore_missing_imports = True
# 开启类型提示
disallow_untyped_calls = True
```
