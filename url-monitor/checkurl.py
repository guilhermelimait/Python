import requests
import win10toast
from clear_screen import clear

t = win10toast.ToastNotifier()

response = requests.get("https://nullaostalavoro.dlci.interno.it/Ministero/Index2", verify=False) 
response2 = requests.get("https://nullaostalavoro.dlci.interno.it/Ministero/", verify=False)
clear()
result = response.status_code     # To print http response code  
result2 = response2.status_code     # To print http response code  

print (response.status_code)
print (response2.status.code)

if result == 200: t.show_toast ("Alert","SITE ONLINE\nIndex2 está disponível","icon.ico",10) 
if result == 406: t.show_toast ("Alert","SITE FORA DO AR\nIndex2 está indisponível","icon.ico",10)



