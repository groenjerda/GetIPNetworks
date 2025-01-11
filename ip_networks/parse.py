import json
import re


data = {}

with open('items.jsonl') as json_file:
    json_list = list(json_file)

for json_str in json_list:
    result = json.loads(json_str)
    data.setdefault(result['provider'], []).append(result['network'])

for provider, networks in data.items():
    with open('data\\Datagroup.txt', 'a') as file:
        file.write('\n'.join(set(networks)) + '\n')
