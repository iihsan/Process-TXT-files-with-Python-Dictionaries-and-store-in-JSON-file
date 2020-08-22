import os           # os is used to read files and directories
import json         # json is used to store data in format

path=os.getcwd()            # reading current working directory
dir = os.listdir(path)      # reading all directories of current path

data = {}
data['python'] = []             #data list to store in json file

for i in dir:                                   # iterating through directories
    if i.endswith('.txt'):                      # read only that files having extension .txt
        with open(i, 'r') as file:              # opening and reading files
            data['python'].append({
                'title': file.readline(),       # 1st line is of title
                'module': file.readline(),      # 2nd line is of module names
                'description': file.readline()  # 3rd line is of description
            })

with open('data.json', 'w') as out:
    json.dump(data, out)            # writing to json file

with open('data.json') as json_file:
    data = json.load(json_file)     # reading from json file
    for p in data['python']:
        print('Title: ' + str(p['title']), end='')
        print('Modules: ' + str(p['module']), end='')
        print('Description: ' + str(p['description']))
        print('')