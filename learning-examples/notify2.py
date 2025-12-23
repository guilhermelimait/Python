import importlib
import subprocess
import sys
import win10toast


def ensure_dependencies():
	missing = []
	try:
		importlib.import_module("win10toast")
	except ImportError:
		missing.append("win10toast")

	if missing:
		print(f"Installing missing packages: {', '.join(missing)}")
		result = subprocess.run([sys.executable, "-m", "pip", "install", *missing])
		if result.returncode != 0:
			print("Package installation failed. Please install manually and retry.")
			sys.exit(1)


ensure_dependencies()

t = win10toast.ToastNotifier()
t.show_toast("Alert", "Hello beautiful! \nThis is an alert", "icon.ico", 10)