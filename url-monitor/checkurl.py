import requests
import urllib3
try:
    import win10toast
    t = win10toast.ToastNotifier()
    TOAST_AVAILABLE = True
except ImportError:
    TOAST_AVAILABLE = False
    print("win10toast not installed. Install with: pip install win10toast")

try:
    from clear_screen import clear
    clear()
except ImportError:
    import os
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()

# Disable SSL warnings for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URLs = [
    ("Index2", "https://nullaostalavoro.dlci.interno.it/Ministero/Index2"),
    ("Main", "https://nullaostalavoro.dlci.interno.it/Ministero/")
]

print("Checking website status...\n")

for name, url in URLs:
    try:
        response = requests.get(url, verify=False, timeout=10)
        status_code = response.status_code
        
        print(f"Status {name}: {status_code}")
        
        if TOAST_AVAILABLE:
            if status_code == 200:
                t.show_toast("Site Online", f"{name} está disponível", "icon.ico", 10)
            else:
                t.show_toast("Site Offline", f"{name} está indisponível (Code: {status_code})", "icon.ico", 10)
        else:
            if status_code == 200:
                print(f"{name} is ONLINE")
            else:
                print(f"{name} is OFFLINE (Status: {status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error checking {name}: {e}")
        if TOAST_AVAILABLE:
            t.show_toast("Connection Error", f"Cannot reach {name}", "icon.ico", 10)

print("\nCheck complete.")



