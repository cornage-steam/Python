import os


def show_stat(folder_path):
    stat = get_stat(folder_path)
    keys = list(stat)
    keys.sort()
    for key in keys:
        print(f'{key}: {stat(key)}')


def get_stat(folder_path):
    stat = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            size = os.stat(os.path.join(root, file)).st_size
            key = get_key(size)
            if key not in stat:
                stat[key] = 0
            stat[key] += 1
    if not stat:
        raise Exception('Отсутствуют файлы в директории')
    return stat


def get_key(size):
    num_digits = 1
    while True:
        if size // 10:
            num_digits += 1
        else:
            break
        size //= 10
    return 10 ** num_digits


if __name__ == '__main__':
    try:
        my_folder_path = './'
        show_stat(my_folder_path)
    except Exception as e:
        print(e)
