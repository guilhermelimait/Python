# 📊 JSON File Examples - Read & Write JSON Data

Learn how to read, write, and manipulate JSON data in Python.

## 📝 Description

A collection of examples demonstrating JSON file operations in Python, including reading data, writing data, and modifying JSON structures.

## ✨ Features

- **Read JSON Files**: Parse JSON data from files
- **Write JSON Files**: Save Python data as JSON
- **Modify Data**: Update JSON attributes
- **Pretty Printing**: Format JSON for readability
- **Error Handling**: Handle invalid JSON

## 📋 Prerequisites

- Python 3.8+
- No external dependencies (uses standard library)

## 📦 Installation

No installation needed! Uses Python's built-in `json` module.

```bash
# Just run the scripts
python readjson.py
```

## 🚀 Usage

### Read JSON File

```bash
python readjson.py
```

This script reads data from `jsonfile.json` and displays it.

### Additional Examples

Check the `2nd example/` folder for more advanced operations:

```bash
cd "2nd example"
python readjson.py    # Read JSON data
python writejson.py   # Write JSON data
```

## 📂 File Structure

```
read json file/
├── jsonfile.json          # Sample JSON data
├── readjson.py           # Read JSON example
└── 2nd example/
    ├── data.txt          # Data file
    ├── readjson.py       # Read operations
    └── writejson.py      # Write operations
```

## 💡 Common Operations

### Read JSON

```python
import json

# Read from file
with open('jsonfile.json', 'r') as f:
    data = json.load(f)
    print(data)
```

### Write JSON

```python
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Write to file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)
```

### Modify JSON

```python
import json

# Read
with open('data.json', 'r') as f:
    data = json.load(f)

# Modify
data['age'] = 31
data['email'] = 'john@example.com'

# Write back
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
```

### Parse JSON String

```python
import json

json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)
print(data['name'])  # Output: Alice
```

### Convert to JSON String

```python
import json

data = {"name": "Bob", "age": 35}
json_string = json.dumps(data, indent=2)
print(json_string)
```

## 🎯 Advanced Examples

### Pretty Print JSON

```python
import json

with open('data.json', 'r') as f:
    data = json.load(f)
    print(json.dumps(data, indent=4, sort_keys=True))
```

### Handle Nested JSON

```python
import json

data = {
    "users": [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]
}

# Access nested data
for user in data['users']:
    print(f"{user['name']} is {user['age']} years old")
```

### Merge JSON Files

```python
import json

# Read multiple JSON files
with open('file1.json', 'r') as f1:
    data1 = json.load(f1)

with open('file2.json', 'r') as f2:
    data2 = json.load(f2)

# Merge
merged = {**data1, **data2}

# Save
with open('merged.json', 'w') as f:
    json.dump(merged, f, indent=4)
```

### Error Handling

```python
import json

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found!")
except json.JSONDecodeError:
    print("Invalid JSON format!")
```

### Filter JSON Data

```python
import json

with open('users.json', 'r') as f:
    users = json.load(f)

# Filter users over 25
adults = [user for user in users if user['age'] > 25]

print(json.dumps(adults, indent=2))
```

## 📊 JSON Data Types

| Python Type | JSON Type |
|-------------|-----------|
| dict | object |
| list, tuple | array |
| str | string |
| int, float | number |
| True | true |
| False | false |
| None | null |

## 🔧 Common Patterns

### Configuration Files

```python
import json

# Load config
with open('config.json', 'r') as f:
    config = json.load(f)

# Use settings
api_key = config.get('api_key')
timeout = config.get('timeout', 30)  # Default 30
```

### User Data Management

```python
import json

def save_user(username, data):
    users = {}
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        pass
    
    users[username] = data
    
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

def get_user(username):
    with open('users.json', 'r') as f:
        users = json.load(f)
    return users.get(username)
```

### API Response Handling

```python
import json
import requests

response = requests.get('https://api.example.com/data')
data = response.json()  # Parse JSON response

# Save to file
with open('api_response.json', 'w') as f:
    json.dump(data, f, indent=4)
```

## 💡 Use Cases

- **Configuration Files**: Store application settings
- **Data Storage**: Simple database alternative
- **API Communication**: Exchange data with web services
- **Data Export**: Export data in portable format
- **Settings Management**: User preferences and options

## 🐛 Troubleshooting

**Issue**: JSONDecodeError
- Check JSON syntax (commas, brackets, quotes)
- Use online JSON validator
- Check for trailing commas

**Issue**: File not found
- Verify file path
- Use absolute paths if needed
- Check current working directory

**Issue**: Unicode errors
- Specify encoding: `open('file.json', 'r', encoding='utf-8')`

## 📚 Dependencies

None - uses Python standard library:
- `json`: Built-in JSON module

## 🎓 Learning Objectives

After completing these examples, you'll understand:
- ✅ Reading JSON files
- ✅ Writing JSON files
- ✅ Modifying JSON data
- ✅ Parsing JSON strings
- ✅ Error handling
- ✅ Working with nested structures
- ✅ Real-world JSON applications

## 📄 License

MIT License - Feel free to use and modify for your learning.

---

**Part of the [Python Projects Collection](../README.md)**
