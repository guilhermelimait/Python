import json
with open('jsonfile.json') as json_file:
    data = json.load(json_file)
    for value in data.Name():
        print(value)
    

""" 
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
"""


"""
person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)
print( person_dict)

print (person_dict['name'], person_dict['languages'])
"""