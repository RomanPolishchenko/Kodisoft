import csv


def read_csv(file_obj):
    reader = csv.DictReader(file_obj)
    return reader


if __name__ == '__main__':
    file_path = 'input/apps.csv'
    with open(file_path, 'r') as file:
        apps = read_csv(file)

    file_path = 'input/link_data.csv'
    with open(file_path, 'r') as file:
        link_data = read_csv(file)

    file_path = 'input/orders.csv'
    with open(file_path, 'r') as file:
        orders = read_csv(file)
