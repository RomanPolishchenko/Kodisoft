from functions import *
import datetime
from collections import namedtuple


App = namedtuple('App', ['name', 'time', 'revenue', 'efficiency'])


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


# @benchmark
def parse_apps(app_list):
    _seen = []
    _apps = []
    for info in app_list:
        if info['AppId'] not in _seen:
            _apps.append(App(info['AppId'], datetime.timedelta(0, 0, 0), 0, 0))
            _seen.append(info['AppId'])
    return _apps


# @benchmark
def orders_walkthrough(orders_list):
    global CURRENT_TIME, HOUR

    for order in orders_list:
        # print(order)
        order_time = time_fs(order['Time'])
        time_delta = order_time - CURRENT_TIME
        print(time_delta)
        if time_delta.seconds <= HOUR.seconds:
            print('1 hour')
        elif HOUR.seconds < time_delta.seconds <= 2 * HOUR.seconds:
            print('2 hours')
        else:
            print('1 day')


if __name__ == '__main__':
    CURRENT_TIME = datetime.datetime.utcnow().astimezone()
    HOUR = datetime.timedelta(0, 3600)
    apps, link_data, orders = input_data()

    # look for all unique apps
    unique_apps = parse_apps(apps)
    # add them all to top-list
    top_apps_h = unique_apps.copy()
    top_apps_2h = unique_apps.copy()
    top_apps_d = unique_apps.copy()

    # orders_walkthrough(orders)
