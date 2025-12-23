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

sleep(3)

pyautogui.rightClick(10, 10)

pyautogui.alert('This displays some text with an OK button.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')
a = pyautogui.prompt('This lets the user type in a string and press OK.')
print(a)
pyautogui.alert(a)