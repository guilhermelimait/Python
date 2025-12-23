# ⚡ Spam Text - Automated Text Typing Tool

Automate text input from a file using PyAutoGUI for testing and automation purposes.

## 📝 Description

A Python automation script that reads text from a file and automatically types it using keyboard simulation. Useful for testing, repetitive data entry, or automation tasks.

## ✨ Features

- **File-Based Input**: Read text from any text file
- **Automated Typing**: Simulates keyboard input
- **Line-by-Line Processing**: Types each line with Enter key
- **Configurable Delay**: Built-in delay before execution
- **Simple Interface**: Easy to use and modify

## 📋 Prerequisites

- Python 3.8+
- `words.txt` file with content to type

## 📦 Installation

```bash
# Install required package
pip install pyautogui
```

## 🚀 Usage

### Basic Usage

1. Create or edit `words.txt` with your content:
```
Line 1 of text
Line 2 of text
Line 3 of text
```

2. Run the script:
```bash
python spam.py
```

3. **Quickly switch** to your target window/application within 5 seconds
4. The script will automatically type each line

## ⚠️ Important Notes

- **5-Second Delay**: You have 5 seconds after running to position your cursor
- **Each Line = Enter**: Script presses Enter after each line
- **Stop Execution**: Move mouse to corner of screen to trigger failsafe
- **Test Safely**: Always test in a safe environment first

## 🔧 Configuration

### Modify Delay Time

```python
from time import sleep

sleep(10)  # Change to 10 seconds delay
```

### Change Input File

```python
f = open("myfile.txt", 'r')  # Use different file
```

### Add Delay Between Lines

```python
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    sleep(0.5)  # Add 0.5 second delay between lines
```

### Type Without Enter Key

```python
import pyautogui

# Read entire file and type as one block
with open("words.txt", 'r') as f:
    text = f.read()
    pyautogui.typewrite(text, interval=0.05)  # 0.05s between characters
```

## 💡 Use Cases

- **Form Testing**: Automated form filling for QA
- **Data Entry**: Repetitive data input automation
- **Chat Testing**: Test chat applications with automated messages
- **Demo Scripts**: Create automated demonstrations
- **Stress Testing**: Test input handling of applications

## 🎯 Advanced Examples

### Type with Random Delays

```python
import pyautogui
import random
from time import sleep

sleep(5)

with open("words.txt", 'r') as f:
    for line in f:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
        sleep(random.uniform(0.5, 2.0))  # Random delay 0.5-2s
```

### Type Specific Number of Times

```python
import pyautogui
from time import sleep

sleep(5)

with open("words.txt", 'r') as f:
    content = f.readlines()

# Repeat 10 times
for i in range(10):
    for line in content:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
```

### Type with Keyboard Shortcuts

```python
import pyautogui
from time import sleep

sleep(5)

with open("words.txt", 'r') as f:
    for line in f:
        pyautogui.typewrite(line)
        pyautogui.hotkey('ctrl', 'enter')  # Ctrl+Enter instead of Enter
```

### Safe Mode with Confirmation

```python
import pyautogui
from time import sleep

print("Starting in 5 seconds...")
print("Move mouse to top-left corner to abort!")
sleep(5)

try:
    with open("words.txt", 'r') as f:
        for line in f:
            pyautogui.typewrite(line)
            pyautogui.press("enter")
except pyautogui.FailSafeException:
    print("Aborted by user!")
```

## 🛡️ Safety Features

### PyAutoGUI Failsafe

Move your mouse to the **top-left corner** of the screen to stop execution immediately.

### Disable Failsafe (Not Recommended)

```python
pyautogui.FAILSAFE = False  # Use with caution!
```

### Add Pause Between Actions

```python
pyautogui.PAUSE = 0.5  # 0.5 second pause between all PyAutoGUI calls
```

## 📚 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| pyautogui | Latest | GUI automation and keyboard control |

## 🐛 Troubleshooting

**Issue**: Script types too fast
- Add delays: `sleep(0.5)` between lines
- Use `interval` parameter: `pyautogui.typewrite(text, interval=0.1)`

**Issue**: Cannot stop script
- Move mouse to top-left corner (failsafe)
- Use Ctrl+C in terminal

**Issue**: Wrong window/application
- Increase initial delay time
- Add window focus code before typing

**Issue**: Special characters not typing
- Use `pyautogui.write()` instead of `typewrite()` for Unicode support

## 🎮 Additional PyAutoGUI Functions

```python
# Click at position
pyautogui.click(100, 100)

# Move mouse
pyautogui.moveTo(500, 500)

# Press key combinations
pyautogui.hotkey('ctrl', 'c')  # Copy
pyautogui.hotkey('ctrl', 'v')  # Paste

# Get screen size
width, height = pyautogui.size()

# Screenshot
pyautogui.screenshot('screenshot.png')
```

## ⚠️ Ethical Usage Warning

This tool should only be used:
- On your own systems
- For legitimate testing and automation
- With proper authorization

**DO NOT use for:**
- Spamming messages
- Unauthorized access
- Malicious purposes
- Violating terms of service

## 📄 License

MIT License - Feel free to use and modify for your projects.

---

**Part of the [Python Projects Collection](../README.md)**
