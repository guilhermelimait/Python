import json
users = {}

with open ('users.json') as f:
    users = json.load(f)
    print("Username: "+ users['username'])
    print("Password: "+ users['password'])



