import csv

# you should 'pip install iso8601' before
from iso8601 import parse_date


def read_csv(file_obj):
    """
    Read info from file that contains information in csv-format.
    Returns the list of <OrderDict> objects.
    :param file_obj: file object
    :return: <list>
    """
    reader = csv.DictReader(file_obj)
    return list(reader)


def time_fs(str_time):
    """
    Converting date and time from str_time to datetime.
    :param str_time: <class 'str'>. date and time in format '2018-02-21 20:26:37.073'
    :return: <class 'datetime'>.
    """
    return parse_date(str_time)


def id_to_lower(_id):
    """
    Format id to lowercase.
    :param _id: <class 'str'>. Uppercase id. (e.g. 74D2A8C0-5531-4FC0-8478-F9CE11825F09)
    :return: <class 'str'>. Lowercase id. (e.g. 74d2a8c0-5531-4fc0-8478-f9ce11825f09)
    """
    _tmp = list(_id)
    _tmp = list(map(lambda x: x.lower() if x.isalpha() else x, _tmp))
    return ''.join(_tmp)


def benchmark(f):
    """
    Decorator for calculating function f working time.
    """
    import time
    import functools

    @functools.wraps(f)
    def _benchmark(*args, **kw):
        t = time.clock()  # time before
        rez = f(*args, **kw)
        t = time.clock() - t  # time difference
        print('{0} time elapsed {1:.8f}'.format(f.__name__, t))
        return rez

    return _benchmark


def calc_efficiency(apps):
    """
    Calculates efficiency for each app in 'apps'
    :param apps: list of apps
    :return: None
    """
    for app in apps.values():
        app.calc_eff()


if __name__ == '__main__':
    pass
