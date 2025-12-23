# 📁 Folder Structure & Naming Convention

## 🎨 Visual Overview

```
python-projects/
│
├── 🎭 facial-emotion-recognition/
│   │   Real-time AI emotion detection with MediaPipe
│   ├── emotion_detector.py
│   ├── emotion_trainer.py
│   ├── face_puppeteer.py
│   └── requirements.txt
│
├── 📝 wordpress-to-github/
│   │   Export WordPress posts to Markdown
│   ├── ExportWordpressToGithub.py
│   └── readme.md
│
├── 📄 pdf-joiner/
│   │   Merge multiple PDFs into one
│   ├── pdfjoiner.py
│   └── README.md
│
├── 🌡️ weather-api/
│   │   Real-time weather data via OpenWeatherMap
│   ├── getcitytemp.py
│   ├── tempexample.json
│   └── README.md
│
├── 🔊 text-to-speech/
│   │   Convert text and PDFs to audio
│   ├── audible1.py
│   ├── audiblepdf.py
│   └── README.md
│
├── 🔐 password-generator/
│   │   Generate secure random passwords
│   ├── gerasenha.py
│   └── README.md
│
├── 🔍 url-monitor/
│   │   Monitor website status with notifications
│   ├── checkurl.py
│   └── README.md
│
├── ⚡ text-automation/
│   │   Automate keyboard typing from files
│   ├── spam.py
│   ├── words.txt
│   └── README.md
│
├── 📚 learning-examples/
│   │   Beginner-friendly Python tutorials
│   ├── helloworld.py
│   ├── guessthenumber.py
│   ├── hangman.py
│   ├── [15+ more examples]
│   └── README.md
│
├── 📊 json-basics/
│   │   JSON read/write fundamentals
│   ├── readjson.py
│   ├── jsonfile.json
│   └── README.md
│
└── 📊 json-user-management/
    │   Advanced JSON operations with user data
    ├── readjson.py
    ├── writejson.py
    ├── users.json
    └── readme.md
```

---

## 🏷️ Naming Convention: kebab-case

All folders follow **kebab-case** (lowercase with hyphens) for consistency:

### ✅ Benefits

| Feature | Description |
|---------|-------------|
| 🌐 **GitHub Friendly** | No encoding issues in URLs |
| 🔗 **URL Safe** | Direct use in web addresses |
| 👁️ **Readable** | Easy to scan and understand |
| 💻 **Cross-Platform** | Works on Windows, Mac, Linux |
| 📱 **Mobile Friendly** | No case sensitivity issues |
| 🤝 **Industry Standard** | Matches modern best practices |

### 📝 Naming Rules

1. **All lowercase**: `password-generator` not `PasswordGenerator`
2. **Hyphens for spaces**: `text-to-speech` not `text_to_speech`
3. **Descriptive names**: `weather-api` not `gettemp`
4. **English only**: `password-generator` not `geradorsenhas`
5. **Purpose-driven**: `json-user-management` not `json-file-2`

---

## 🔄 Migration Reference

| ❌ Old Name | ✅ New Name | 🏷️ Category |
|------------|-------------|-------------|
| `Audible text` | `text-to-speech` | Utility |
| `check url` | `url-monitor` | Utility |
| `Export-Wordpress-Posts-To-Github` | `wordpress-to-github` | Featured |
| `geradorsenhas` | `password-generator` | Utility |
| `get city temp` | `weather-api` | Utility |
| `PDFJoiner` | `pdf-joiner` | Utility |
| `random examples` | `learning-examples` | Education |
| `read json file` | `json-basics` | Education |
| `read json file 2` | `json-user-management` | Education |
| `spam text` | `text-automation` | Utility |

---

## 📂 Category Structure

### 🌟 Featured Projects (2)
Advanced, production-ready applications
- `facial-emotion-recognition/` - AI/ML emotion detection
- `wordpress-to-github/` - Content management tool

### 🔧 Utility Scripts (6)
Practical tools for everyday tasks
- `pdf-joiner/` - Document management
- `weather-api/` - Data fetching
- `text-to-speech/` - Audio conversion
- `password-generator/` - Security tool
- `url-monitor/` - System monitoring
- `text-automation/` - Task automation

### 📚 Learning Resources (3)
Educational materials for Python beginners
- `learning-examples/` - Basic concepts
- `json-basics/` - Data handling intro
- `json-user-management/` - Advanced patterns

---

## 🎯 Quick Navigation

### By Technology
- **Computer Vision**: `facial-emotion-recognition/`
- **Web Scraping**: `wordpress-to-github/`
- **API Integration**: `weather-api/`
- **File Processing**: `pdf-joiner/`, `text-to-speech/`
- **Automation**: `text-automation/`, `url-monitor/`
- **Security**: `password-generator/`
- **Data Handling**: `json-basics/`, `json-user-management/`

### By Skill Level
- **Beginner**: `learning-examples/`, `json-basics/`
- **Intermediate**: `password-generator/`, `weather-api/`, `pdf-joiner/`
- **Advanced**: `facial-emotion-recognition/`, `wordpress-to-github/`

### By Use Case
- **Learning Python**: `learning-examples/`
- **Data Science/ML**: `facial-emotion-recognition/`
- **Content Creation**: `wordpress-to-github/`, `text-to-speech/`
- **DevOps/Automation**: `url-monitor/`, `text-automation/`
- **Everyday Tools**: `password-generator/`, `weather-api/`, `pdf-joiner/`

---

## 📊 Repository Statistics

| Metric | Count |
|--------|-------|
| Total Projects | 11 |
| Featured Projects | 2 |
| Utility Scripts | 6 |
| Learning Examples | 3 |
| README Files | 12 |
| Python Files | 50+ |

---

## 🔍 Finding Projects

### By Command
```bash
# List all projects
ls -la

# Filter by type
ls *-api/        # API-related
ls *-generator/  # Generator tools
ls json-*/       # JSON-related
```

### By README
Each folder contains a comprehensive README with:
- ✅ Description and features
- ✅ Installation instructions
- ✅ Usage examples
- ✅ Dependencies
- ✅ Troubleshooting
- ✅ Advanced examples

---

<div align="center">

**Organized, Professional, GitHub-Ready** 🚀

[← Back to Main README](../README.md)

</div>
