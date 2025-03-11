# 说明：

一、本程序是使用Python语言编写的，需要安装Python环境。

二、本程序需要使用FFmpeg，所以需要安装FFmpeg。
1. 官方网站下载FFMPEG
2. 解压后，复制bin目录的，假定为“D:\ffmpeg\bin”（文件目录一定不能出现中文字符）
3. 配置系统环境变量，在Path中新增系统变量“D:\ffmpeg\bin”    
4. 测试是否配置成功：在CMD中输入命令：ffmpeg -version，如果出现版本信息，则配置成功。

三、安装FFmpeg-Python（这是一个架设Python和FFmpeg之间的桥梁）:`pip install ffmpeg-python`

# 参考链接：
1. https://blog.csdn.net/qq_38499109/article
