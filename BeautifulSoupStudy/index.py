# http://www.javashuo.com/article/p-vwduxehq-cw.html
from builtins import *

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# soup_html = BeautifulSoup(html, features='html.parser')
print(type(soup))  # <class 'bs4.BeautifulSoup'>
print(soup.title)  # <title>The Dormouse's story</title>
print(soup)  # 整片文章
print(11111111111111111111111)
tt = soup.select("p a")
print(type(tt))  # <class 'bs4.element.ResultSet'>
print(tt)  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print('2' * 20)
for item in tt:
    print(item)
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
print('3' * 20)

my_tag = tt[0]
print(type(my_tag))  # <class 'bs4.element.Tag'>
print(my_tag)  # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print(my_tag.name)  # a
print(my_tag.attrs)  # {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
print(my_tag.attrs['href'])  # http://example.com/elsie
my_tag['href'] = 'http://www.sina.com.cn'
print(my_tag.attrs['href'])  # http://www.sina.com.cn
print(my_tag.string)  # Elsie
print(my_tag.get_text()) #如果有嵌套标签，my_tag.string获取不到内容，但my_tag.get_text()可以
