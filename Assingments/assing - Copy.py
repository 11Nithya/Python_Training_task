import json
f = open('data.json')
d = json.load(f)
# print(d)
# print(type(json_obj))
for key,values in d.items():
    if isinstance(values,list):
        for item in values:
            if 'name' in item:
                print('name: ',item['name'])
            if 'work' in item:
                print('work: ', item['work'])
                print('---------')