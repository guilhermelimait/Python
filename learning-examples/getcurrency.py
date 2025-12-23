import importlib
import subprocess
import sys
import requests 
import urllib, json


def ensure_dependencies():
	missing = []
	try:
		importlib.import_module("requests")
	except ImportError:
		missing.append("requests")

	if missing:
		print(f"Installing missing packages: {', '.join(missing)}")
		result = subprocess.run([sys.executable, "-m", "pip", "install", *missing])
		if result.returncode != 0:
			print("Package installation failed. Please install manually and retry.")
			sys.exit(1)


ensure_dependencies()

r = requests.get('https://api.exchangeratesapi.io/history?start_at=2020-10-30&end_at=2020-11-06&symbols=BRL')
print (r.text)
