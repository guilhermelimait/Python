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
**Location:** `Export-Wordpress-Posts-To-Github/`

Export WordPress posts to categorized Markdown files perfect for static sites:
- **Time Period Selection**: Last 24h, 7 days, 30 days, or all posts
- **Automatic Organization**: Posts sorted by categories
- **Image Downloads**: Automatically downloads and organizes post images
- **Markdown Conversion**: Clean conversion with metadata preservation
- **Multiple Site Support**: Works with any WordPress site with public API

**Technologies:** Requests, BeautifulSoup4, Markdown Processing

**Quick Start:**
```bash
cd Export-Wordpress-Posts-To-Github
pip install requests beautifulsoup4
python ExportWordpressToGithub.py
```

[📖 Full Documentation](Export-Wordpress-Posts-To-Github/readme.md)

---

## 🔧 Utility Scripts

### PDF Management
**Location:** `PDFJoiner/`
- **pdfjoiner.py**: Merge multiple PDF files into a single document
- **Dependencies:** PyPDF2 or pyPdf

```bash
python pdfjoiner.py file1.pdf file2.pdf output.pdf
```

### Weather Information
**Location:** `get city temp/`
- **getcitytemp.py**: Get real-time weather data for any city
- **Features:** Temperature, feels like, min/max, weather conditions
- **API:** OpenWeatherMap integration

```bash
python getcitytemp.py
```

### Text-to-Speech
**Location:** `Audible text/`
- **audible1.py**: Convert text to speech
- **audiblepdf.py**: Read PDF files aloud
- **Dependencies:** pyttsx3, PyPDF2

```bash
python audible1.py
```

### Password Generator
**Location:** `geradorsenhas/`
- **gerasenha.py**: Generate secure random passwords
- **Features:** Configurable length, uppercase, lowercase, digits, special characters

```bash
python gerasenha.py
```

### URL Monitor
**Location:** `check url/`
- **checkurl.py**: Monitor website status and get desktop notifications
- **Features:** HTTP status checking, Windows toast notifications
- **Dependencies:** requests, win10toast

```bash
python checkurl.py
```

### Automation Tools
**Location:** `spam text/`
- **spam.py**: Automate text typing from file (for testing)
- **Dependencies:** pyautogui

```bash
python spam.py
```

---

## 📚 Learning Examples

**Location:** `random examples/`

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

### JSON Operations
**Location:** `read json file/` and `read json file 2/`

Examples of working with JSON data:
- Reading JSON files
- Writing JSON files
- Modifying JSON attributes
- User data management

```bash
cd "read json file 2"
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
Python/
├── 🎭 facial-emotion-recognition/    # AI-powered emotion detection suite
├── 📝 Export-Wordpress-Posts-To-Github/  # WordPress content exporter
├── 📄 PDFJoiner/                     # PDF manipulation tools
├── 🌡️  get city temp/                 # Weather information API
├── 🔊 Audible text/                  # Text-to-speech utilities
├── 🔐 geradorsenhas/                 # Password generation
├── 🔍 check url/                     # URL monitoring and notifications
├── ⚡ spam text/                     # Automation scripts
├── 📚 random examples/               # Learning examples for beginners
├── 📊 read json file/                # JSON handling examples
└── 📊 read json file 2/              # Advanced JSON operations
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
- **Learn Python**: Start with examples in `random examples/`
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

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute
1. 🐛 **Report Bugs**: Open an issue with details
2. 💡 **Suggest Features**: Share your ideas
3. 📝 **Improve Documentation**: Fix typos, add examples
4. 🔧 **Submit Pull Requests**: Add new features or fix bugs

### Development Setup
```bash
# Fork the repository
git clone https://github.com/yourusername/python-projects.git
cd python-projects

# Create a new branch
git checkout -b feature/your-feature-name

# Make your changes and commit
git add .
git commit -m "Add: your feature description"

# Push to your fork
git push origin feature/your-feature-name

# Open a Pull Request
```

### Code Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Include docstrings for functions
- Update README if adding new projects
- Test your code before submitting

---

## 📝 Project Roadmap

### In Progress
- [ ] Add unit tests for core utilities
- [ ] Create requirements.txt for each project
- [ ] Docker containers for major projects
- [ ] CI/CD pipeline integration

### Planned Features
- [ ] Web interface for emotion detection
- [ ] REST API for WordPress exporter
- [ ] Cross-platform notification system
- [ ] GUI applications for CLI tools
- [ ] More ML/AI examples

### Future Projects
- [ ] Natural Language Processing examples
- [ ] Web scraping utilities
- [ ] Database integration examples
- [ ] Discord/Telegram bots
- [ ] Data visualization tools

---

## 🎓 Learning Path

### Beginner Track
1. Start with `random examples/helloworld.py`
2. Learn variables with `variaveis.py`
3. Practice conditionals with `condicionais.py`
4. Master loops with `loop.py` and `loopfor.py`
5. Play with `guessthenumber.py` and `hangman.py`

### Intermediate Track
1. JSON operations in `read json file/`
2. API calls with `getcitytemp.py`
3. File operations with `PDFJoiner/`
4. Automation with `spam text/`

### Advanced Track
1. Computer vision with `facial-emotion-recognition/`
2. Web scraping with `Export-Wordpress-Posts-To-Github/`
3. Build your own ML models

---

## 🔒 Security Notes

- **API Keys**: Never commit API keys to the repository
- **Sensitive Data**: Use environment variables for credentials
- **Dependencies**: Keep packages updated for security patches
- **Validation**: Always validate user input

Example for API keys:
```python
import os
API_KEY = os.getenv('OPENWEATHER_API_KEY')
```

---

## 🐛 Known Issues

- **check url/checkurl.py**: Windows-specific (uses win10toast)
- **Audible text**: Some voices may not work on all systems
- **facial-emotion-recognition**: Requires webcam access
- **getcitytemp.py**: Requires OpenWeatherMap API key

---

## 📊 Project Statistics

- **Total Projects**: 11+ complete applications
- **Learning Examples**: 15+ beginner-friendly scripts
- **Lines of Code**: 5000+
- **Dependencies**: 10+ popular Python libraries
- **Categories**: AI/ML, Automation, Utilities, Learning

---

## 📖 Additional Resources

### Documentation
- [Python Official Docs](https://docs.python.org/3/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [MediaPipe Guide](https://google.github.io/mediapipe/)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Tutorials
- [Real Python](https://realpython.com/)
- [Python.org Tutorials](https://docs.python.org/3/tutorial/)
- [Automate the Boring Stuff](https://automatetheboringstuff.com/)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

### MIT License Summary
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ❌ Liability
- ❌ Warranty

---

## 👤 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

## 🌟 Star History

If you find this repository helpful, please consider giving it a star! ⭐

It helps others discover these projects and motivates continued development.

---

## 📞 Support

### Getting Help
- 📧 **Email**: Open an issue for bugs
- 💬 **Discussions**: Use GitHub Discussions for questions
- 📖 **Wiki**: Check the wiki for detailed guides (coming soon)

### Frequently Asked Questions

**Q: Which Python version should I use?**  
A: Python 3.8 or higher is recommended for all projects.

**Q: Can I use these projects commercially?**  
A: Yes! The MIT license allows commercial use.

**Q: How do I report a bug?**  
A: Open an issue with detailed steps to reproduce.

**Q: Can I contribute?**  
A: Absolutely! See the Contributing section above.

---

## 🙏 Acknowledgments

- **MediaPipe Team**: For the amazing face detection library
- **OpenCV Community**: For computer vision tools
- **Python Community**: For extensive library ecosystem
- **All Contributors**: Thank you for your contributions!

---

## 📈 Changelog

### Version 1.0.0 (Current)
- ✨ Initial public release
- 🎭 Facial emotion recognition suite
- 📝 WordPress exporter
- 🔧 Multiple utility scripts
- 📚 Beginner examples

---

<div align="center">

**Made with ❤️ and Python**

[⬆ Back to Top](#-python-projects-collection)

</div>

