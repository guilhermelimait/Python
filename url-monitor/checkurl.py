import importlib
import subprocess
import sys
import requests
import urllib3


def ensure_dependencies():
    missing = []
    for pkg, module in [("requests", "requests"), ("win10toast", "win10toast"), ("urllib3", "urllib3")]:
        try:
            importlib.import_module(module)
        except ImportError:
            missing.append(pkg)

    if missing:
        print(f"Installing missing packages: {', '.join(missing)}")
        result = subprocess.run([sys.executable, "-m", "pip", "install", *missing])
        if result.returncode != 0:
            print("Package installation failed. Please install manually and retry.")
            sys.exit(1)


ensure_dependencies()
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



