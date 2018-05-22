from functions import *
from classes import *
import datetime
from copy import deepcopy
import os


def input_apps(file_path):
    """
    Input app list of OrderDict objects from file at 'file_path' .
    :return: <list>
    """
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        _apps = read_csv(file)
        return _apps


def input_links(file_path):
    """
    Input links from file and converting them to dict {key=ApplicationID: value=SessionID}.
    :return: <dict>
    """
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        _link_out = {}
        _link_data = read_csv(file)
        for _link in _link_data:
            _link_out[id_to_lower(_link['ApplicationID'])] = id_to_lower(_link['SessionID'])
        return _link_out


def input_orders(file_path):
    """
    Input orders from file and converting them to dict:
            key = SessionId
            value = list of 'Order' namedtuples
    :return: <list>
    """
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        _orders_out = {}
        _orders = read_csv(file)
        for _order in _orders:
            if _order['SessionId'] in _orders_out:
                _orders_out[_order['SessionId']].append(Order(float(_order['Revenue']), time_fs(_order['Time'])))
            else:
                _orders_out[_order['SessionId']] = [Order(float(_order['Revenue']), time_fs(_order['Time']))]
        return _orders_out


def input_time():
    """
    Input and format time or use current time.
    :return: <datetime>
    """
    _time = input('Enter time in format "yyyy-mm-dd hh:mm:ss.ms" or 0 if you want to use current time: ')
    if _time is '0':
        _time = datetime.datetime.utcnow().astimezone()
    else:
        _time = time_fs(_time)
    return _time


# @benchmark
def parse_apps(app_list):
    """
    Parsing and looking for unique apps.
    Takes list of all apps. Returns dict {key=AppName: value: App object} of unique apps.
    :param app_list: <list>
    :return: <dict>
    """
    _seen = []
    _apps = {}
    for _app in app_list:
        if _app['AppId'] not in _seen:
            _apps[_app['AppId']] = App(_app['AppId'], datetime.timedelta(0, 0, 0), 0)
            _seen.append(_app['AppId'])
    return _apps


def closest_h(_time):
    """
    Checks if _time is in the closest hour from CURRENT_TIME.
    :param _time: <datetime>
    :return: <bool>
    """
    global HOUR, CURRENT_TIME
    return HOUR.seconds * 1/6 <= (_time - CURRENT_TIME).seconds <= HOUR.seconds


def closest_2h(_time):
    """
    Checks if _time is in the closest 2 hours from CURRENT_TIME.
    :param _time: <datetime>
    :return: <bool>
    """
    global HOUR, CURRENT_TIME
    return HOUR.seconds < (_time - CURRENT_TIME).seconds <= 2 * HOUR.seconds


def analise_order(_order):
    """
    Analise order within the time and account its duration and revenue.
    :param _order: <Order>
    :return: None
    """
    global top_apps_h, top_apps_2h, top_apps_d
    current_revenue = _order.revenue  # add its revenue

    if closest_h(_order.time):  # if the order is made in closest hour
        top_apps_h[app_name].total_time += app_duration
        top_apps_h[app_name].total_revenue += current_revenue
        # then it's made in closest two hours too
        top_apps_2h[app_name].total_time += app_duration
        top_apps_2h[app_name].total_revenue += current_revenue
    elif closest_2h(_order.time):  # if the order is made in 2 closest hours
        top_apps_2h[app_name].total_time += app_duration
        top_apps_2h[app_name].total_revenue += current_revenue
    top_apps_d[app_name].total_time += app_duration  # anyway it is made in closest day
    top_apps_d[app_name].total_revenue += current_revenue


def output_result(file_name):
    """
    Write the result to the file file_name
    :param file_name: <str>
    :return: None
    """
    global top_apps_h, top_apps_2h, top_apps_d, N, CURRENT_TIME

    # converting dict to list and sort it by efficiency
    out_apps_h = sorted([item for item in top_apps_h.values()], key=lambda x: x.efficiency)[:-(N + 1):-1]
    out_apps_2h = sorted([item for item in top_apps_2h.values()], key=lambda x: x.efficiency)[:-(N + 1):-1]
    out_apps_d = sorted([item for item in top_apps_d.values()], key=lambda x: x.efficiency)[:-(N + 1):-1]

    with open(file_name, 'w', encoding='utf-8') as f:
        # print('Prediction for {}\n'.format(CURRENT_TIME.strftime('%A, %H:%M')), file=f)
        print('Prediction for {}\n'.format(CURRENT_TIME.now().strftime('%A, %H:%M')), file=f)

        print('Most relevant {} apps in the next hour:'.format(N), file=f)
        for num, _app in enumerate(out_apps_h):
            print('{}. {}'.format(num + 1, _app.name), file=f)
        print('\n', file=f)

        print('Most relevant {} apps in the next 2 hours:'.format(N), file=f)
        for num, _app in enumerate(out_apps_2h):
            print('{}. {}'.format(num + 1, _app.name), file=f)
        print('\n', file=f)

        print('Most relevant {} apps in the next day:'.format(N), file=f)
        for num, _app in enumerate(out_apps_d):
            print('{}. {}'.format(num + 1, _app.name), file=f)

    print("Result was also printed to the file 'output.txt' in current directory.")


def print_result():
    global top_apps_h, top_apps_2h, top_apps_d, N, CURRENT_TIME

    # converting dict to list and sort it by efficiency
    out_apps_h = sorted([item for item in top_apps_h.values()], key=lambda x: x.efficiency)[:-(N + 1):-1]
    out_apps_2h = sorted([item for item in top_apps_2h.values()], key=lambda x: x.efficiency)[:-(N + 1):-1]
    out_apps_d = sorted([item for item in top_apps_d.values()], key=lambda x: x.efficiency)[:-(N + 1):-1]

    print('Prediction for {}\n'.format(CURRENT_TIME.now().strftime('%A, %H:%M')))

    print('Most relevant {} apps in the next hour:'.format(N))
    for num, _app in enumerate(out_apps_h):
        print('{}. {}'.format(num + 1, _app.name))
    print('\n')

    print('Most relevant {} apps in the next 2 hours:'.format(N))
    for num, _app in enumerate(out_apps_2h):
        print('{}. {}'.format(num + 1, _app.name))
    print('\n')

    print('Most relevant {} apps in the next day:'.format(N))
    for num, _app in enumerate(out_apps_d):
        print('{}. {}'.format(num + 1, _app.name))


if __name__ == '__main__':
    # some constants
    CURRENT_TIME = input_time()  # current time or set by user
    HOUR = datetime.timedelta(0, 3600)  # one hour to compare with
    SECONDS_BEFORE = 25  # probable time for order be made before app launching
    SECONDS_AFTER = 20  # probable time for order be made after app launching
    N = int(input('Count of top apps: N = '))  # count of top apps

    # files paths
    apps_path = os.path.join(os.path.dirname(__file__), '.', 'input', 'apps.csv')
    links_path = os.path.join(os.path.dirname(__file__), '.', 'input', 'link_data.csv')
    orders_path = os.path.join(os.path.dirname(__file__), '.', 'input', 'orders.csv')

    # input info from files and format it
    apps = input_apps(apps_path)
    links = input_links(links_path)
    orders = input_orders(orders_path)

    # look for all unique apps
    unique_apps = parse_apps(apps)
    # add them all to top-list
    top_apps_h = deepcopy(unique_apps)
    top_apps_2h = deepcopy(unique_apps)
    top_apps_d = deepcopy(unique_apps)

    for app in apps:
        # current app info
        app_name = app['AppId']
        app_id = app['Id']
        start_time = time_fs(app['StartTime'])
        end_time = time_fs(app['EndTime'])
        app_duration = end_time - start_time

        # if weekday of launching doesn't correspond to current weekday
        if start_time.isoweekday() != CURRENT_TIME.isoweekday():
            continue  # ignoring this launching

        app_session = links.get(app_id)  # get session id in which the order was made

        # if there is no information about session or about order
        if app_session is None or orders.get(app_session) is None:
            continue  # just ignoring this app launching

        for order in orders.get(app_session):
            # if the order was made in this app
            if start_time <= order.time <= end_time:
                analise_order(order)  # than it's probably Restaurant

            # if the order was made just before or just after some app
            if (start_time - order.time).seconds < SECONDS_BEFORE or\
                    (order.time - end_time).seconds < SECONDS_AFTER:
                analise_order(order)  # than it's probably an entertaining app

    # calculate their efficiency
    calc_efficiency(top_apps_h)
    calc_efficiency(top_apps_2h)
    calc_efficiency(top_apps_d)

    # printing results into the file
    open('output.txt', 'w', encoding='utf-8').close()
    output_path = os.path.join(os.path.dirname(__file__), 'output.txt')
    print_result()
    output_result(output_path)
