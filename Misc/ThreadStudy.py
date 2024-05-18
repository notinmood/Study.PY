from threading import Thread


def sub_thread():
    print("in sub thread...")


def main_thread():
    t = Thread(target=sub_thread)
    t.start()
    print("in main thread...")


if __name__ == '__main__':
    main_thread()
