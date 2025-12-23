import importlib
import subprocess
import sys
import pyttsx3
import PyPDF2


def ensure_dependencies():
    missing = []
    for pkg, module in [("pyttsx3", "pyttsx3"), ("PyPDF2", "PyPDF2")]:
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
book = open('readmypdf.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()