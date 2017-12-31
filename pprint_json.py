import json

import sys
from pprint import pprint


def load_data(filepath):
	with open(filepath, encoding='utf-8') as f:
		pprint(json.load(f))


if __name__ == '__main__':
	if len(sys.argv) > 1:
		file_path = sys.argv[1]
		load_data(file_path)
	else:
		assert AttributeError('Отсутсвует путь к файлу')
