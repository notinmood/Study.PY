import numpy as np
import pandas as pd

from hiland.data import PandasHelper as ph


def _get_max_value(item, result_4_loops):
    # print(item)
    # print('------------')
    target = item['C']
    if result_4_loops is None:
        result_4_loops = target
    else:
        if result_4_loops < target:
            result_4_loops = target

    return result_4_loops


def pandas_helper_loop():
    _df = create_df_use_dict(True)
    max_value = ph.loop_data_frame(_df, _get_max_value)
    print(max_value)


def read_rows(data_frame):
    print('按行读取数据，内容如下')
    print(11111111111111111111111)
    for index, row in data_frame.iterrows():
        print("索引号为：", index)
        # print(row)
        print("目标值为：", row['A'])
        print('////////////////////////')


def create_df_use_list():
    """
    用列表创建dataframe就是按照行的方式创建，列表的每个元素就是df的一行（列表的每个元素依然是列表）
    :return:
    """
    _df = pd.DataFrame([['Snow', 'M', 22], ['Tyrion', 'M', 32], ['Sansa', 'F', 18], ['Arya', 'F', 14]],
                       columns=['name', 'gender', 'age'], index=['a', 'b', 'c', 'd'])
    return _df


def create_df_use_dict(custom_index=False):
    """
    用字典创建dataframe就是按照列的方式创建，字典的每一个Key就是df的column（字典的每个value依然是列表）
    :return:
    """
    data = {"A": [12, 4, 5, 44, 1],
            "B": [5, 2, 54, 3, 2],
            "C": [20, 16, 7, 3, 8],
            "D": [14, 3, 17, 2, 6]}

    index = list("abcde")

    _df = None

    if custom_index:
        _df = pd.DataFrame(data, index)
    else:
        _df = pd.DataFrame(data)

    return _df


def merge_demo():
    df1 = pd.DataFrame({'key': ['one', 'two', 'two'],
                        'data1': np.arange(3)})
    df2 = pd.DataFrame({'key': ['one', 'three', 'three'],
                        'data2': np.arange(3)})

    df3 = pd.merge(df1, df2)
    print(df1)
    print("-" * 10)
    print(df2)
    print("-" * 10)
    print(df3)
    print("-" * 10)

    df4 = pd.merge(df1, df2, how='left')
    print(df4)
    print("-" * 10)

    df5 = pd.merge(df1, df2, how='right')
    print(df5)
    print("-" * 10)

    df6 = pd.merge(df1, df2, how='inner')
    print(df6)
    print("-" * 10)

    df7 = pd.merge(df1, df2, how='outer')
    print(df7)
    print("-" * 10)

    dfa = pd.DataFrame({'key': ['one', 'two', 'two'],
                        'value': ['a', 'b', 'c'],
                        'data1': np.arange(3)})
    dfb = pd.DataFrame({'key': ['one', 'two', 'three'],
                        'value': ['a', 'c', 'c'],
                        'data2': np.arange(3)})

    df9 = pd.merge(dfa, dfb)
    df10 = pd.merge(dfa, dfb, on=['key', 'value'], how='outer')
    print(dfa)
    print(dfb)
    df11 = pd.merge(dfa, dfb, on=['value'], how='right')
    print(df11)
    print(df9)
    print(df10)
    print("+" * 10)


def rolling_demo():
    data = [[1, 10], [2, 12], [3, 14], [4, 16], [5, 18], [6, 20], [7, 22], [8, 24], [9, 26],
            [10, 28], [11, 30],
            [12, 32]]
    _df = pd.DataFrame(data, columns=["Ca", "Cb"])
    _mean = _df.rolling(3).mean()
    print(_mean)
    _mean = _df.rolling(5).mean()
    print(_mean)
    _mean = _df.rolling(10).mean()
    print(_mean)
    print(type(_mean))
    print('===============================')
    _aa = _df.rolling(3)
    print(type(_aa))
    print(_aa)
    print('===============================')
    __df = _df['Ca'] + _df['Cb']
    print(type(__df))

    __mean = __df.rolling(3).mean()
    print(__mean)


def get_element_demo():
    _df = create_df_use_list()
    print(_df)

    _element = ph.get_element(_df, 1, 0)
    print(_element)

    _element = ph.get_element(_df, 1, "name")
    print(_element)

    _element = ph.get_element(_df, 'a', "name")
    print(_element)

    _c = _df["name"]
    print(_c)

    _c = _df[1:2]
    print(_c)


def __get_chinese_weight(weight, unit="jin"):
    return str(weight * 2) + unit


def map_demo():
    # df = create_df_use_list()
    boolean = [True, False]
    gender = ["男", "女"]
    color = ["white", "black", "yellow"]
    row_count = 10
    my_dataframe = pd.DataFrame({
        "height": np.random.randint(150, 190, row_count),
        "weight": np.random.randint(40, 90, row_count),
        "smoker": [boolean[x] for x in np.random.randint(0, 2, row_count)],
        "gender": [gender[x] for x in np.random.randint(0, 2, row_count)],
        "age": np.random.randint(15, 90, row_count),
        "color": [color[x] for x in np.random.randint(0, len(color), row_count)]
    })

    print(my_dataframe)
    my_dataframe = my_dataframe[["height", "weight", "age"]]

    print(my_dataframe)
    print(my_dataframe["weight"].map(__get_chinese_weight))
    _cc = my_dataframe.apply(np.sum, axis=0)
    print(type(_cc))
    print(_cc)

    _cc = my_dataframe.apply(np.log, axis=0)
    print(type(_cc))
    print(_cc)
    # print(type(my_dataframe["weight"]))
    # print(11111111111111111111111111111)
    #
    # _series = my_dataframe["weight"]
    #
    # _new_df = my_dataframe[["weight", "height"]]
    #
    # _filtered_df = my_dataframe[my_dataframe["weight"] > 70]
    #
    # _temp = my_dataframe[["weight", "weight"]]
    #
    # _temp = my_dataframe[my_dataframe.weight > 70]
    # print(type(_temp))
    # print(_temp)
    # print(55555555555555555555555555)
    #
    # _filtered_df = my_dataframe[my_dataframe["weight"] > 70]
    #
    # _filtered_sr = my_dataframe["weight"] > 70
    #
    # print(type(_filtered_sr))
    # print(_filtered_sr)
    # # print(my_dataframe["weight"]).apply(__get_chinese_weight, args="斤")


def column_exist_demo():
    _pp = create_df_use_list()
    oo = ph.is_exist_column(_pp, "name2")
    print(oo)


if __name__ == '__main__':
    column_exist_demo()
    # map_demo()
# get_element_demo()

# rolling_demo()
# merge_demo()
# df = create_df_use_list()
# print(df)
#
# _t = df["name"]
# _t = df.name
# print(type(_t))
# print(_t)
#
# _m = df[df.age > 20]
# print(_m)

# pandas_helper_loop()
# df = create_df_use_dict()
# read_rows(df)
