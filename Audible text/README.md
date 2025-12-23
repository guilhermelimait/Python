# 🔊 Audible Text - Text-to-Speech Utilities

Convert text and PDF documents to speech using Python's text-to-speech capabilities.

## 📝 Description

A collection of text-to-speech utilities that enable you to convert written text and PDF documents into audible speech using the pyttsx3 engine.

## ✨ Features

- **Text-to-Speech**: Convert any text string to speech
- **PDF Reader**: Read PDF documents aloud
- **Offline Processing**: No internet connection required
- **Multiple Voice Options**: Choose from available system voices
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📋 Prerequisites

- Python 3.8+
- System audio output

## 📦 Installation

```bash
# Install required packages
pip install pyttsx3 PyPDF2
```

## 🚀 Usage

### Basic Text-to-Speech

```bash
python audible1.py
```

**Script functionality:**
```python
import pyttsx3
texttospeach = pyttsx3.init()
texttospeach.say("That is awesome!")
texttospeach.runAndWait()
```

### PDF Reader

```bash
python audiblepdf.py
```

This script will:
1. Open a specified PDF file
2. Extract text from pages
3. Read the content aloud

## 🔧 Configuration

### Customize Voice Settings

```python
import pyttsx3

engine = pyttsx3.init()

# Set speech rate (default is 200)
engine.setProperty('rate', 150)

# Set volume (0.0 to 1.0)
engine.setProperty('volume', 0.9)

# Change voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index for different voices
```

## 📚 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| pyttsx3 | Latest | Text-to-speech conversion |
| PyPDF2 | Latest | PDF text extraction |

## 💡 Use Cases

- **Accessibility**: Help visually impaired users access text content
- **Multitasking**: Listen to documents while doing other tasks
- **Learning**: Audio learning from written materials
- **Testing**: Test voice interfaces and audio outputs

## 🐛 Troubleshooting

**Issue**: No audio output
- Check system volume settings
- Verify audio drivers are installed
- Try different voice engines

**Issue**: PDF not reading correctly
- Ensure PDF is not image-based (scanned)
- Check PDF is not password-protected
- Verify file path is correct

## 📄 License

MIT License - Feel free to use and modify for your projects.

---

**Part of the [Python Projects Collection](../README.md)**
