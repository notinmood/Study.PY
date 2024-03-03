"""
 * @file   : zip的使用研究.py
 * @time   : 11:04
 * @date   : 2024/2/20
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


if __name__ == '__main__':
    man_list = ['黄晓明', '刘恺威', '贾乃亮']
    woman_list = ['杨颖', '杨幂', '李小璐']
    # 1.1 zip缝合两个或多个等长的列表
    couple= zip(man_list, woman_list)
    couple_list= list(couple)
    print(couple)
    print(couple_list)

    # 1.2  zip缝合两个或多个不等长的列表
    has_child = [True,True]
    family_list = list(zip(man_list, woman_list, has_child))
    print(family_list) # 可以发现结果中只有两个家庭，这是因为zip虽然可以处理任意多的序列，但最终元素的个数取决于最短的序列。

    # 2. 遍历
    for man, woman in couple_list:
        print(f'{man} 和 {woman} 结婚')
    pass

    # 3. 解封
    man, woman = zip(*couple_list) # 将夫妻列表解封为男女两个列表
    print(man)
    print(woman)


pass
