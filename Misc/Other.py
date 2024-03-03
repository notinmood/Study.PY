from builtins import *

from crawl import TushareRequest as tr

_date = tr.get_last_trade_date()
print(_date)

# _list = ['beijing', 'shanghai', 'qingdao', 'guangzhou', "ss"]
# _list.insert(0, 'shenzhen')
# print(_list)


# def get_daily_data2(ts_code, start_date=None, end_date=None):
#     _client_daily = mm.Client("stock_daily")
#     condition = dict()
#     condition["ts_code"] = ts_code
#     if start_date is None:
#         start_date = DateTimeHelper.get_compact_string()
#
#     if end_date is None:
#         end_date = DateTimeHelper.get_compact_string()
#
#     condition["trade_date"] = {"$gte": start_date, "$lte": end_date}
#
#     cursor = _client_daily.find_all(condition)
#
#     _daily_data = ph.convert_cursor_to_dataframe(cursor)
#
#     if _daily_data.empty:
#         print("空的dataframe")
#     else:
#         print(_daily_data.columns)
#         print(list(_daily_data))
#         print(_daily_data.columns.tolist())
#         print("]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
#         print(ph.get_column_names(_daily_data))
#         print(ph.get_column_count(_daily_data))
#         print(ph.get_row_count(_daily_data))
#         print("0000000000000000000000000")
#         print(_daily_data)
#         print("======0000000000000000000")
#         first_date = ph.get_element(_daily_data, 0, 2)
#         last_date = ph.get_element(_daily_data, 7, 2)
#         row_count = ph.get_row_count(_daily_data)
#         last_factor_in_period = ph.get_element(_daily_data, row_count - 1, "adj_factor")
#         print(first_date, last_date, last_factor_in_period)
#         _hfq_close = _daily_data["close"] * _daily_data["adj_factor"]
#         _qfq_close = _hfq_close / last_factor_in_period
#         _hfq_ma = _hfq_close.rolling(3).mean()
#         _qfq_ma = _qfq_close.rolling(3).mean()
#         print("收盘数据为：")
#         print(_daily_data["close"])
#         print("后复权数据为：")
#         print(_hfq_ma)
#         print("前复权数据为：")
#         print(_qfq_ma)
#         # print(_ma.items)
#         # data = cursor.fetchall()
#         # columnDes = cursor.description  # 获取连接对象的描述信息
#         # columnNames = [columnDes[i][0] for i in range(len(columnDes))]
#         # df = pd.DataFrame([list(i) for i in data], columns=columnNames)
#         #
#         # print(df)
