import json

import sys

from os.path import isfile


def load_json_from_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)


def json_pprint(json_data):
    print(json.dumps(json_data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = ""

    while not isfile(file_path):
        print("Неверный путь к файлу")
        file_path = input("Введите путь к файлу: ")

    json_pprint(load_json_from_file(file_path))
