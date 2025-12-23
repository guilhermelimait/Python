import importlib
import subprocess
import sys
import pyautogui
from time import sleep


def ensure_dependencies():
    missing = []
    try:
        importlib.import_module("pyautogui")
    except ImportError:
        missing.append("pyautogui")

    if missing:
        print(f"Installing missing packages: {', '.join(missing)}")
        result = subprocess.run([sys.executable, "-m", "pip", "install", *missing])
        if result.returncode != 0:
            print("Package installation failed. Please install manually and retry.")
            sys.exit(1)


ensure_dependencies()

sleep(5)
f = open("words.txt",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")


