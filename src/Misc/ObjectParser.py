# import json
#
# import pandas
#
# from hiland.data import StringHelper
# from hiland.io import IOHelper as ioh
#
#
# def __get_node_index__money_support(all_nodes, code_value):
#     all_nodes = enumerate(all_nodes)
#     for index, node in all_nodes:
#         if node["code"] == code_value:
#             return index
#
#     return None
#
#
# def deal_money_support():
#     content = ioh.load_file("C:\\ab\\money.txt")
#     json_object = json.loads(content)
#     all_nodes = json_object["returndata"]["datanodes"]
#
#     # # print(type(all_nodes))
#     # # # _index = __get_node_index__money_support(all_nodes, "zb.A0D0105_sj.202012")
#     # _index = __get_node_index__money_support(all_nodes, 'zb.A0D0105_sj.200005')
#     #
#     # print(_index)
#     # print(all_nodes[_index])
#     # val = all_nodes[_index]['data']['data']
#     # print(val)
#
#     prefix = "zb.A0D01{0}_sj."
#     prefix_m0_quantity = prefix.format("05")
#     prefix_m0_rate = prefix.format("06")
#     prefix_m1_quantity = prefix.format("03")
#     prefix_m1_rate = prefix.format("04")
#     prefix_m2_quantity = prefix.format("01")
#     prefix_m2_rate = prefix.format("02")
#
#     money_supports = []
#
#     for year in range(2000, 2022):
#         for month in range(1, 13):
#             month = StringHelper.set_padding(month, 2)
#             period = "{0}{1}".format(year, month)
#
#             m0_q_code = prefix_m0_quantity + period
#             m0_q_value = __get_mx_value(m0_q_code, all_nodes)
#             m0_r_code = prefix_m0_rate + period
#             m0_r_value = __get_mx_value(m0_r_code, all_nodes)
#
#             m1_q_code = prefix_m1_quantity + period
#             m1_q_value = __get_mx_value(m1_q_code, all_nodes)
#             m1_r_code = prefix_m1_rate + period
#             m1_r_value = __get_mx_value(m1_r_code, all_nodes)
#
#             m2_q_code = prefix_m2_quantity + period
#             m2_q_value = __get_mx_value(m2_q_code, all_nodes)
#             m2_r_code = prefix_m2_rate + period
#             m2_r_value = __get_mx_value(m2_r_code, all_nodes)
#
#             print(period)
#
#             print(m0_q_value)
#             print(m0_r_value)
#
#             print(m1_q_value)
#             print(m1_r_value)
#
#             print(m2_q_value)
#             print(m2_r_value)
#             print('----------------------------')
#             money_supports.append([period, m0_r_value, m0_q_value, m1_r_value, m1_q_value, m2_r_value, m2_q_value])
#
#     df = pandas.DataFrame(money_supports,
#                           columns=["period", "m0_quantity", "m0_rate", "m1_quantity", "m1_rate", "m2_quantity",
#                                    "m2_rate"])
#     df.to_excel("C:\\ab\\money.csv")
#     print(df)
#
#
# def __get_mx_value(code, all_nodes):
#     _index = __get_node_index__money_support(all_nodes, code)
#     if _index:
#         _value = all_nodes[_index]['data']['data']
#     else:
#         _value = None
#
#     return _value
#
#
# if __name__ == '__main__':
#     deal_money_support()
