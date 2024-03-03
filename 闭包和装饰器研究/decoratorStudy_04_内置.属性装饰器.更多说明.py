class PropertyDemo(object):
    def __init__(self, name, age, sex):
        """

        :param str name:姓名
        :param int age:年龄
        :parameter sex:性别
        """
        self.sex = sex
        self.name = name
        self.age = age

    @property
    def my_name(self):
        return 5555

    @my_name.getter
    def my_name(self):
        return self.name

    @my_name.setter
    def my_name(self, value):
        self.name = value


if __name__ == '__main__':
    pd = PropertyDemo("张三", 20, '男')
    print('以下展示的是通过__init__内初始化的属性')
    print(pd.name)
    print(pd.sex)

    print('以下展示的是通过@property装饰器访问属性的值')
    print(pd.my_name)

    print('以下展示的是通过@property.setter装饰器设置属性的值')
    pd.my_name = '李四'
    print(pd.my_name)
