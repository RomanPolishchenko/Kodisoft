from functions import *
import datetime


def input_data():
    file_path = 'input/apps.csv'
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        _apps = read_csv(file)

    file_path = 'input/link_data.csv'
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        _link_data = read_csv(file)

    file_path = 'input/orders.csv'
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        _orders = read_csv(file)
    return _apps, _link_data, _orders


if __name__ == '__main__':
    CURRENT_TIME = datetime.datetime.utcnow().astimezone()
    apps, link_data, orders = input_data()
