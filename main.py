import csv


def read_csv(file_obj):
    reader = csv.DictReader(file_obj)
    return reader


if __name__ == '__main__':
    file_path = 'input/apps.csv'
    with open(file_path, 'r') as file:
        read_csv(file)
