# Audible Text - Text-to-Speech Utilities

Convert text (and PDFs) to speech using Python's text-to-speech capabilities.

## Description

Utilities that read text aloud with `pyttsx3`. `audible1.py` now accepts text from the command line, exposes rate/volume settings, and includes basic error handling. `audiblepdf.py` reads PDF files aloud.

## Features

- Text-to-speech with configurable rate and volume
- CLI text input: `python audible1.py "Hello world"`
- Offline processing (no network required)
- PDF-to-speech helper (`audiblepdf.py`)

## Prerequisites

- Python 3.8+
- System audio output

## Installation

```bash
pip install pyttsx3 PyPDF2
```

## Usage

### Text-to-speech

```bash
# Default text
python audible1.py

# Custom text
python audible1.py "This is a test"
```

Key snippet:

```python
def speak(text, rate=150, volume=1.0):
	engine = pyttsx3.init()
	engine.setProperty('rate', rate)
	engine.setProperty('volume', volume)
	engine.say(text)
	engine.runAndWait()
```

### PDF reader

```bash
python audiblepdf.py
```

## Dependencies

| Package | Purpose                 |
|---------|-------------------------|
| pyttsx3 | Text-to-speech engine   |
| PyPDF2  | PDF text extraction     |

## Notes

- Audio output depends on OS voices installed.
- For scanned/image PDFs, use OCR before reading.

---

Part of the [Python Projects Collection](../README.md)
