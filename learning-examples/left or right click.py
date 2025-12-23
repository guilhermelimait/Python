import pyautogui
from time import sleep

sleep(3)

pyautogui.rightClick(10, 10)

pyautogui.alert('This displays some text with an OK button.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')
a = pyautogui.prompt('This lets the user type in a string and press OK.')
print(a)
pyautogui.alert(a)