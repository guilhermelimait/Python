# 🐍 Python Projects Collection

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)](https://github.com/yourusername)

A comprehensive collection of practical Python projects ranging from AI/ML applications to automation utilities. This repository showcases real-world implementations that developers can use, learn from, and contribute to.

---

## 📋 Table of Contents

- [Featured Projects](#-featured-projects)
- [Utility Scripts](#-utility-scripts)
- [Learning Examples](#-learning-examples)
- [Installation](#-installation)
- [Dependencies](#-dependencies)
- [Quick Start](#-quick-start)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Featured Projects

### 1. **Facial Emotion Recognition Suite** 🎭
**Location:** `facial-emotion-recognition/`

A real-time facial emotion detection system with advanced features:
- **7 Emotion Detection**: Happy, Sad, Surprised, Angry, Disgusted, Sleepy, Neutral
- **468 Facial Landmarks**: Using MediaPipe for precise tracking
- **Personalized Calibration**: Train the system to your specific facial features
- **Face Puppeteer**: Animate photos with your facial expressions
- **Real-time Processing**: Instant emotion analysis with confidence scoring

**Technologies:** OpenCV, MediaPipe, NumPy, Computer Vision

**Quick Start:**
```bash
cd facial-emotion-recognition
pip install -r requirements.txt
python emotion_detector.py
```

[📖 Full Documentation](facial-emotion-recognition/README.md)

---

### 2. **WordPress to GitHub Exporter** 📝
**Location:** `wordpress-to-github/`

Export WordPress posts to categorized Markdown files perfect for static sites:
- **Time Period Selection**: Last 24h, 7 days, 30 days, or all posts
- **Automatic Organization**: Posts sorted by categories
- **Image Downloads**: Automatically downloads and organizes post images
- **Markdown Conversion**: Clean conversion with metadata preservation
- **Multiple Site Support**: Works with any WordPress site with public API

**Technologies:** Requests, BeautifulSoup4, Markdown Processing

**Quick Start:**
```bash
cd wordpress-to-github
pip install requests beautifulsoup4
python ExportWordpressToGithub.py
```

[📖 Full Documentation](wordpress-to-github/readme.md)

---

## 🔧 Utility Scripts

### 📄 PDF Management
**Location:** `pdf-joiner/`
- **pdfjoiner.py**: Merge multiple PDF files into a single document
- **Dependencies:** PyPDF2 or pyPdf

```bash
cd pdf-joiner
python pdfjoiner.py file1.pdf file2.pdf output.pdf
```

### 🌡️ Weather Information
**Location:** `weather-api/`
- **getcitytemp.py**: Get real-time weather data for any city
- **Features:** Temperature, feels like, min/max, weather conditions
- **API:** OpenWeatherMap integration

```bash
cd weather-api
python getcitytemp.py
```

### 🔊 Text-to-Speech
**Location:** `text-to-speech/`
- **audible1.py**: Convert text to speech
- **audiblepdf.py**: Read PDF files aloud
- **Dependencies:** pyttsx3, PyPDF2

```bash
cd text-to-speech
python audible1.py
```

### 🔐 Password Generator
**Location:** `password-generator/`
- **gerasenha.py**: Generate secure random passwords
- **Features:** Configurable length, uppercase, lowercase, digits, special characters

```bash
cd password-generator
python gerasenha.py
```

### 🔍 URL Monitor
**Location:** `url-monitor/`
- **checkurl.py**: Monitor website status and get desktop notifications
- **Features:** HTTP status checking, Windows toast notifications
- **Dependencies:** requests, win10toast

```bash
cd url-monitor
python checkurl.py
```

### ⚡ Text Automation
**Location:** `text-automation/`
- **spam.py**: Automate text typing from file (for testing)
- **Dependencies:** pyautogui

```bash
cd text-automation
python spam.py
```

---

## 📚 Learning Examples

**Location:** `learning-examples/`

Perfect for beginners learning Python! Includes:

| Script | Description | Concepts |
|--------|-------------|----------|
| `helloworld.py` | Classic first program | Print statements |
| `variaveis.py` | Variable usage | Data types |
| `condicionais.py` | Conditional logic | if/else statements |
| `loop.py`, `loopfor.py` | Loop examples | Iteration, control flow |
| `listas.py` | List operations | Data structures |
| `metodos.py` | Method examples | Functions |
| `guessthenumber.py` | Number guessing game | Random, user input, loops |
| `hangman.py` | Classic hangman game | String manipulation, game logic |
| `dice.py` | Dice rolling simulator | Random numbers |
| `getcurrency.py` | Currency converter | API calls, JSON parsing |
| `passwordgenerator.py` | Password generator | Random, string operations |
| `colorprint.py` | Colored console output | Terminal formatting |
| `batteryindicatorheadset.py` | Battery monitoring | System information |
| `notify2.py` | Desktop notifications | Windows integration |

---

## 📂 Data Handling Examples

### 📊 JSON Operations
**Location:** `json-basics/` and `json-user-management/`

Examples of working with JSON data:
- Reading JSON files
- Writing JSON files
- Modifying JSON attributes
- User data management

```bash
# Basic JSON operations
cd json-basics
python readjson.py

# Advanced user management
cd json-user-management
python readjson.py
python writejson.py
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning)

### Clone Repository
```bash
git clone https://github.com/yourusername/python-projects.git
cd python-projects
```

---

## 📦 Dependencies

### Global Dependencies
```bash
# Core utilities (used across multiple projects)
pip install requests psutil pyautogui
```

### Project-Specific Dependencies

#### Facial Emotion Recognition
```bash
pip install opencv-python mediapipe numpy
```

#### WordPress Exporter
```bash
pip install requests beautifulsoup4
```

#### PDF Tools
```bash
pip install PyPDF2
```

#### Text-to-Speech
```bash
pip install pyttsx3 PyPDF2
```

#### Windows Notifications
```bash
pip install win10toast
```

---

## ⚡ Quick Start

1. **Choose a project** from the directory structure
2. **Navigate to the folder**:
   ```bash
   cd project-name
   ```
3. **Install dependencies** (if requirements.txt exists):
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the script**:
   ```bash
   python script_name.py
   ```

---

## 📁 Repository Structure

```
python-projects/
│
├── 🎭 facial-emotion-recognition/    # AI-powered emotion detection suite
│   ├── emotion_detector.py          # Real-time emotion detection
│   ├── emotion_trainer.py           # Personalized calibration
│   ├── face_puppeteer.py            # Animate photos with expressions
│   └── requirements.txt             # Project dependencies
│
├── 📝 wordpress-to-github/           # WordPress content exporter
│   ├── ExportWordpressToGithub.py   # Main export script
│   └── readme.md                    # Documentation
│
├── 🔧 Utility Scripts
│   ├── 📄 pdf-joiner/               # Merge PDF files
│   ├── 🌡️  weather-api/             # Real-time weather data
│   ├── 🔊 text-to-speech/           # Text and PDF to audio
│   ├── 🔐 password-generator/       # Secure password creation
│   ├── 🔍 url-monitor/              # Website status monitoring
│   └── ⚡ text-automation/          # Automated text typing
│
├── 📚 learning-examples/            # Beginner-friendly tutorials
│   ├── helloworld.py                # Your first program
│   ├── guessthenumber.py            # Interactive game
│   ├── hangman.py                   # Classic word game
│   └── [15+ more examples]          # Full learning path
│
└── 📊 Data Handling
    ├── json-basics/                 # JSON read/write fundamentals
    └── json-user-management/        # Advanced JSON operations
```

---

## 🛠️ Technologies Used

| Technology | Projects | Purpose |
|------------|----------|---------|
| **OpenCV** | Facial Emotion Recognition | Computer vision and image processing |
| **MediaPipe** | Facial Emotion Recognition | Face mesh and landmark detection |
| **NumPy** | Facial Emotion Recognition | Mathematical operations |
| **BeautifulSoup4** | WordPress Exporter | HTML parsing |
| **Requests** | Multiple projects | HTTP requests and API calls |
| **PyPDF2** | PDF tools | PDF manipulation |
| **pyttsx3** | Text-to-Speech | Voice synthesis |
| **pyautogui** | Automation | GUI automation |
| **win10toast** | Notifications | Windows notifications |

---

## 💡 Use Cases

### For Developers
- **Learn Python**: Start with examples in `learning-examples/`
- **API Integration**: See real-world examples with OpenWeatherMap, WordPress API
- **Computer Vision**: Explore MediaPipe and OpenCV in emotion recognition
- **Automation**: Study pyautogui implementations

### For Content Creators
- **WordPress Migration**: Export your blog to Markdown
- **PDF Processing**: Merge documents programmatically
- **Text-to-Speech**: Convert articles to audio

### For Researchers
- **Emotion Detection**: Real-time facial analysis
- **Calibration Systems**: Personalized ML model training
- **Data Collection**: JSON handling and storage examples

---

<div align="center">

**Made with ❤️ and Python**

[⬆ Back to Top](#-python-projects-collection)

</div>

