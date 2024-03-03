
Base64模块真正用得上的方法只有8个，分别是：
* A. encode, decode为一组, 专门用来编码和解码文件的, 也可以对StringIO里的数据做编解码；
* B. encodestring, decodestring为一组，专门用来编码和解码字符串（3.9之后就没有这个方法了）
* C. b64encode, b64decode为一组, 用来编码和解码字节串（将普通字节串和base64字节串之间进行转换）
* D. urlsafe_b64decode, urlsafe_b64encode为一组，这个就是用来专门对url进行Base64编解码的，实际上也是调用的前一组函数。

原文链接：https://blog.csdn.net/weixin_44799217/article/details/125949538
