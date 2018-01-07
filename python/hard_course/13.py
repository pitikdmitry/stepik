#не работает так как нужно
import json


def create_dict(data: []) -> dict:
    result = dict()

    for obj in data:
        key = obj['name']
        val = obj['parents']
        result[key] = val
    return result


def count_children_in_list(data: dict, result_dict: dict, current_name: str, depth: int):
    if depth > result_dict[current_name]:
        result_dict[current_name] = depth
    else:
        result_dict[current_name] += depth
    for name in data[current_name]:
        count_children_in_list(data, result_dict, name, result_dict[current_name] + 1)


def count_children(data: dict, result_dict: dict):
    for key, list_names in data.items():
        count_children_in_list(data, result_dict, key, result_dict[key])


data = json.loads(input())
data_dict = create_dict(data)

result_dict = dict()
for key in data_dict:
    result_dict[key] = 1

for key, value in data_dict.items():
    print(key + ": " + str(value))

count_children(data_dict, result_dict)

for key, value in result_dict.items():
    print(key + " : " + str(value))
