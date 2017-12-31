import json

import sys
from pprint import pprint


def pprint_from_file(filepath):
	with open(filepath, encoding='utf-8') as f:
		pprint(json.load(f))


if __name__ == '__main__':
	if len(sys.argv) > 1:
		file_path = sys.argv[1]
		pprint_from_file(file_path)
	else:
		assert AttributeError('Отсутсвует путь к файлу')
