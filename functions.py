import csv
# from datetime import datetime
# you should pip install iso8601 before
from iso8601 import parse_date


def read_csv(file_obj):

    reader = csv.DictReader(file_obj)
    return reader


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


if __name__ == '__main__':
    t1 = time_fs('2018-02-25 10:51:21.433')
    print(t1)
    t1 = t1.astimezone()
    print(t1)
    # t2 = time_fs('2018-02-01T12:19:39.6337006Z')
    # print(t2 - t1)
    # print(id_to_lower('74D2A8C0-5531-4FC0-8478-F9CE11825F09'))

    pass
