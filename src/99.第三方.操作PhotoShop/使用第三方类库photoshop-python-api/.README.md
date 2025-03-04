说明：

1. 使用第三方类库： https://github.com/loonghao/photoshop_python_api.git
2. 安装此类库： `pip install photoshop_python_api`
3. 此类库的使用示例：https://loonghao.github.io/photoshop-python-api/examples/

- Q:非常奇怪，无法实现导出或者另存为。可能是PhotoShop的版本太新？
- A:请使用Ps2023版本及其之前的版本（因为photoshop_python_api的0.22.3版本尚未匹配ps2024）

- Q:如何修改图层的文字内容而图层的名字不变？
- A:同时设置图层的name和textItem.contents可以使二者分别展示不同信息
  ```shell
  wechat_layer.name = ">公众号：文句之美"
  wechat_layer.textItem.contents = ">>百家号：故事里的人生智慧"
  ```
  

