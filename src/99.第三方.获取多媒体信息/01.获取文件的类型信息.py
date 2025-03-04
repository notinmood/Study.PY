import filetype


def determine(file_path: str):
    kind = filetype.guess(file_path)
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)
    if kind.mime.startswith('image/'):
        print('这是一张图片')

    print('---------')


def is_image(file_path: str):
    kind = filetype.guess(file_path)
    if kind is None:
        return False
    pass

    return kind.mime.startswith('image/')


pass

if __name__ == '__main__':
    determine('res/my.jpg')
    determine('res/my.png')
    determine('res/my.txt')
    determine('res/my.psd')

    print(is_image('res/my.jpg'))
    print(is_image('res/my.png'))
    print(is_image('res/my.txt'))
    print(is_image('res/my.psd'))
