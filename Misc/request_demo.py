from builtins import *
from functools import cmp_to_key

from hiland.data import ListHelper as lh
from hiland.io import IOHelper
from hiland.web import RequestHelper as rh


def comp(x, y):
    x = str(x)
    y = str(y)
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


def get_jinan():
    url = "http://www.gshubao.xyz/78_78611/"
    selector = "#list > dl > dd > a"
    detail_items = rh.get_items(url, selector)
    detail_items = lh.remove_duplication_item(detail_items)
    print("共有{0}篇内容".format(len(detail_items)))
    # map(get_jinan_detail, detail_items)

    detail_items.sort(key=cmp_to_key(comp))
    for item in detail_items:
        get_jinan_detail(item)


def get_jinan_detail(item):
    url = "http://www.gshubao.xyz" + item['href']
    title = item.get_text()
    print(title)
    # file_name = "c:\\ab\\bb\\{0}.txt".format(title);
    file_name = "c:\\ab\\bb\\{0}.txt".format("jinan")

    selector = "#content"
    content = rh.get_items(url, selector)
    if len(content) > 0:
        content = str(content[0])
        content = content.replace("<br/>", "\r\n")
        IOHelper.store_file(file_name, content)
        # print(content)


# def get_money_support():
#     url = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%5D&k1=1615430189613&h=1"
#     content = rh.get_items(url, "")
#     print(content)


if __name__ == '__main__':
    # get_money_support()
    get_jinan()
