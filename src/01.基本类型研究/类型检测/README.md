说明：

特别说明：

PyCharm本身支持mypy，但需要安装插件，具体方法请参考官方文档：https://www.jetbrains.com/help/pycharm/type-hinting-in-pycharm.html#mypy-type-checker
另外PyCharm本身就提供了类型提示，不需要安装mypy，也能进行静态类型校验。
如果对PyCharm本身提供的类型提示，或者mypy的类型提示不满意，可以尝试使用其他的静态类型检测工具，比如pylint、pyright等。
-> 现在推荐使用pylint


使用mypy进行静态类型检测。

安装：`pip install mypy`或者 `poetry add mypy`



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
