import csv
# from datetime import datetime
# you should pip install iso8601 before
from iso8601 import parse_date


def read_csv(file_obj):

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
    """Декоратор @benchmark для обчислення часу виконання функції f.

    """
    import time
    import functools

    @functools.wraps(f)
    def _benchmark(*args, **kw):  # функція _benchmark містить код, що виконується
        # перед та після виклику f
        t = time.clock()  # вимірюємо час перед викликом функції
        rez = f(*args, **kw)  # викликаємо f
        t = time.clock() - t  # вимірюємо різницю у часі після виклику функції
        print('{0} time elapsed {1:.8f}'.format(f.__name__, t))
        return rez

    return _benchmark


if __name__ == '__main__':
    t1 = time_fs('2018-02-25 10:51:21.433')
    print(t1)
    t1 = t1.astimezone()
    print(t1)
    # t2 = time_fs('2018-02-01T12:19:39.6337006Z')
    # print(t2 - t1)
    print(id_to_lower('A2C4B1AD-CE00-469F-9DDE-89AA2A56014B'))
    pass
