import json
users = {}
with open ('users.json') as f:
    users = json.load(f)
    users['password'] = 'NONONON'
with open('users.json','w') as f:
    json.dump(users,f)
print("Username: "+ users['username'])
print("New password is: " + users['password'])