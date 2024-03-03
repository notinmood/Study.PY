print('in myClass.py')


def __index__():
    print('in myClass index')


def say_hello(self):
    print('in myClass.py say hello')


class MyClass(object):
    """

    """

    # 以下是为了消除ide的警告而做的cheating
    # noinspection all
    def say_hello(self):
        print('in myClass say hello')
