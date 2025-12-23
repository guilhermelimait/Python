# 📊 JSON User Data Management

Advanced examples for managing user data with JSON files in Python.

## 📝 Description

Complete examples demonstrating how to create, read, modify, and save JSON files with user data. Perfect for understanding JSON-based data management systems.

## ✨ Features

- **Create JSON Files**: Generate structured JSON data
- **Read User Data**: Parse and display JSON information
- **Modify Attributes**: Update specific JSON fields
- **Save Changes**: Persist modifications back to files
- **User Management**: Handle multiple user records

## 📋 Prerequisites

- Python 3.8+
- No external dependencies (uses standard library)

## 🚀 Usage

### Read User Data

```bash
python readjson.py
```

Reads user information from `users.json` and displays it on screen.

### Write/Modify User Data

```bash
python writejson.py
```

Creates or modifies user data and saves it to `users.json`.

## 📂 Example Data Structure

### users.json
```json
{
    "users": [
        {
            "username": "john_doe",
            "password": "secure123",
            "email": "john@example.com",
            "created": "2020-11-19"
        },
        {
            "username": "jane_smith",
            "password": "password456",
            "email": "jane@example.com",
            "created": "2020-11-19"
        }
    ]
}
```

## 💡 Common Operations

### Read All Users

```python
import json

with open('users.json', 'r') as f:
    data = json.load(f)
    for user in data['users']:
        print(f"Username: {user['username']}")
        print(f"Email: {user['email']}")
```

### Add New User

```python
import json

# Read existing data
with open('users.json', 'r') as f:
    data = json.load(f)

# Add new user
new_user = {
    "username": "new_user",
    "password": "newpass123",
    "email": "newuser@example.com"
}
data['users'].append(new_user)

# Save
with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)
```

### Update User

```python
import json

with open('users.json', 'r') as f:
    data = json.load(f)

# Find and update user
for user in data['users']:
    if user['username'] == 'john_doe':
        user['email'] = 'newemail@example.com'
        break

# Save changes
with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)
```

### Delete User

```python
import json

with open('users.json', 'r') as f:
    data = json.load(f)

# Remove user
data['users'] = [u for u in data['users'] if u['username'] != 'john_doe']

# Save
with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)
```

## 🎯 Advanced Examples

### User Authentication System

```python
import json
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password, email):
    with open('users.json', 'r') as f:
        data = json.load(f)
    
    new_user = {
        "username": username,
        "password": hash_password(password),
        "email": email
    }
    
    data['users'].append(new_user)
    
    with open('users.json', 'w') as f:
        json.dump(data, f, indent=4)

def verify_user(username, password):
    with open('users.json', 'r') as f:
        data = json.load(f)
    
    for user in data['users']:
        if user['username'] == username:
            return user['password'] == hash_password(password)
    return False
```

### Search Users

```python
import json

def search_users(query):
    with open('users.json', 'r') as f:
        data = json.load(f)
    
    results = []
    for user in data['users']:
        if query.lower() in user['username'].lower() or \
           query.lower() in user['email'].lower():
            results.append(user)
    
    return results

# Usage
matches = search_users('john')
for user in matches:
    print(user['username'])
```

### User Statistics

```python
import json
from datetime import datetime

def get_user_stats():
    with open('users.json', 'r') as f:
        data = json.load(f)
    
    stats = {
        'total_users': len(data['users']),
        'usernames': [u['username'] for u in data['users']],
        'domains': {}
    }
    
    # Count email domains
    for user in data['users']:
        domain = user['email'].split('@')[1]
        stats['domains'][domain] = stats['domains'].get(domain, 0) + 1
    
    return stats
```

## 📚 Project Completion Checklist

- ✅ Create a JSON file with username and password (2020-11-19)
- ✅ Create a script to read JSON and print to screen (2020-11-19)
- ✅ Create a script to modify JSON attributes (2020-11-19)
- ✅ Save the modified file (2020-11-19)

## 💡 Use Cases

- **User Management Systems**: Store and manage user accounts
- **Authentication**: Simple login systems
- **Profile Management**: User profile data storage
- **Settings Storage**: Application user preferences
- **Data Collection**: Collect and organize user information

## 🔒 Security Notes

⚠️ **Important**: These examples are for learning purposes only!

For production systems:
- **Never store plain text passwords**
- Use proper password hashing (bcrypt, argon2)
- Implement proper authentication libraries
- Use databases instead of JSON files
- Add input validation and sanitization
- Implement access controls

### Better Password Handling

```python
import bcrypt
import json

def create_user_secure(username, password, email):
    # Hash password with bcrypt
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    
    user = {
        "username": username,
        "password": hashed.decode(),  # Store as string
        "email": email
    }
    # Save to JSON...
```

## 🐛 Troubleshooting

**Issue**: File not found
- Ensure `users.json` exists
- Run `writejson.py` first to create the file

**Issue**: JSON decode error
- Validate JSON syntax
- Check for missing commas or brackets

**Issue**: Permission denied
- Check file permissions
- Run with appropriate privileges

## 📄 License

MIT License - Feel free to use and modify for your learning.

---

**Part of the [Python Projects Collection](../README.md)**
