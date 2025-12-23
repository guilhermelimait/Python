# 🔐 Password Generator - Secure Password Creator

Generate strong, random passwords with customizable complexity using Python.

## 📝 Description

A simple yet effective password generator that creates secure random passwords using uppercase letters, lowercase letters, digits, and special characters.

## ✨ Features

- **Cryptographically Random**: Uses Python's random module for unpredictability
- **Customizable Length**: Configure password length to meet requirements
- **Multiple Character Types**: Includes letters, digits, and special characters
- **Easy to Use**: Simple command-line interface
- **Secure Generation**: Meets most password complexity requirements

## 📋 Prerequisites

- Python 3.8+
- No external dependencies (uses standard library)

## 📦 Installation

No installation required! Uses Python standard library.

```bash
# Just run the script
python gerasenha.py
```

## 🚀 Usage

### Basic Usage

```bash
python gerasenha.py
```

The script will generate a 10-character password by default.

### Example Output

```
p7K@mN9!zQ
```

## 🔧 Configuration

### Customize Password Length

Edit the `tamanho` variable in the script:

```python
tamanho = 16  # Change to desired length
```

### Character Set Customization

Choose which character types to include:

```python
import string

# All lowercase letters
string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz

# All uppercase letters
string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

# All letters (upper + lower)
string.ascii_letters    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

# All digits
string.digits           # 0123456789

# Special characters
string.punctuation      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Combine for password
valores = string.ascii_letters + string.digits + string.punctuation
```

## 📊 Password Strength

| Length | Possible Combinations | Strength |
|--------|----------------------|----------|
| 8 | 94^8 ≈ 6 quadrillion | Basic |
| 10 | 94^10 ≈ 54 quintillion | Good |
| 12 | 94^12 ≈ 48 septillion | Strong |
| 16 | 94^16 ≈ 3.8 × 10^31 | Very Strong |

## 💡 Use Cases

- **Account Creation**: Generate passwords for new accounts
- **Password Rotation**: Create new passwords for security updates
- **Testing**: Generate test credentials for development
- **Bulk Generation**: Create multiple passwords for user provisioning

## 🔒 Security Best Practices

1. **Never reuse passwords** across different services
2. **Use a password manager** to store generated passwords
3. **Enable 2FA** when available
4. **Regular rotation** for sensitive accounts
5. **Minimum 12 characters** for strong security

## 🎯 Advanced Example

### Generate Multiple Passwords

```python
from random import choice
import string

def generate_password(length=12):
    valores = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(choice(valores) for _ in range(length))
    return senha

# Generate 5 passwords
for i in range(5):
    print(f"Password {i+1}: {generate_password(16)}")
```

### Generate Password Without Special Characters

```python
# Only letters and numbers
valores = string.ascii_letters + string.digits
```

### Ensure Minimum Requirements

```python
import random
import string

def generate_secure_password(length=12):
    # Ensure at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill remaining length
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += [random.choice(all_chars) for _ in range(length - 4)]
    
    # Shuffle to avoid predictable pattern
    random.shuffle(password)
    return ''.join(password)
```

## 📚 Dependencies

None - uses Python standard library only:
- `random`: For random selection
- `string`: For character sets

## 🐛 Troubleshooting

**Issue**: Password too short
- Increase the `tamanho` variable value

**Issue**: Special characters not supported
- Remove `string.punctuation` from the character set

## 📄 License

MIT License - Feel free to use and modify for your projects.

---

**Part of the [Python Projects Collection](../README.md)**
