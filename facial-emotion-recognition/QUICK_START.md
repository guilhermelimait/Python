# Facial Emotion Detection Suite - Quick Start Guide

## 🚀 How to Run (Without VS Code)

### Option 1: Double-Click (Easiest)
Simply **double-click** on `start_emotion_detector.bat`

The menu will show three options:
1. **Emotion Detector** - Real-time emotion detection
2. **Emotion Trainer** - Calibrate to your face
3. **Face Puppeteer** - Control a photo with your face
4. Exit

### Option 2: Command Prompt
1. Open **Command Prompt** (press `Win + R`, type `cmd`, press Enter)
2. Navigate to this folder:
   ```
   cd .\pc-test-agent
   ```
3. Run:
   ```
   start_emotion_detector.bat
   ```

### Option 3: PowerShell
1. Open **PowerShell** (press `Win + X`, select "Windows PowerShell")
2. Navigate to this folder:
   ```
   cd .\pc-test-agent
   ```
3. Run:
   ```
   .\start_emotion_detector.ps1
   ```

### Option 4: Direct Python Commands
Run individual programs directly:
```bash
python emotion_detector.py    # Real-time emotion detection
python emotion_trainer.py      # Calibration training
python face_puppeteer.py       # Face puppeteering
```

---

## 🎭 Three Applications

### 1. Emotion Detector
**Real-time facial emotion detection from your camera**
- Detects 7 emotions: Happy, Sad, Surprised, Angry, Disgusted, Sleepy, Neutral
- Shows confidence percentage and facial metrics
- Uses personalized calibration if you've trained it
- Controls:
  - **'q'** - Quit
  - **'s'** - Save snapshot
  - **'d'** - Toggle debug mode (show all emotion scores)

### 2. Emotion Trainer
**Train the system to recognize YOUR facial expressions**
- Captures 3 samples for each of 7 emotions
- Creates personalized calibration profile
- Greatly improves detection accuracy
- Controls:
  - Follow on-screen instructions
  - Click "CAPTURE" button for each emotion
  - Click "FINISH" when done
- **Tip**: Run this first for best results!

### 3. Face Puppeteer
**Control a photo's facial expressions with your face**
- Load any image (jpg, png, bmp)
- Your facial movements animate the face in the photo
- Deforms the image face to match your expressions
- Display modes:
  - **'1'** - Show original image only
  - **'2'** - Show animated image only
  - **'3'** - Side-by-side (your face + animated)
- Controls:
  - **'q'** - Quit
  - **'s'** - Save snapshot

---

## 📋 Requirements
- Python 3.8 or higher
- Webcam (built-in or external)
- Internet connection (first run only - to download face model)
- For Face Puppeteer: An image file to animate

---

## 📊 What You'll See

### Emotion Detector
- Live camera feed (top right)
- Current emotion in large text (left side)
- Confidence percentage
- Facial metrics (smile, mouth, eyes, eyebrows)
- Calibration status
- FPS counter

### Emotion Trainer
- Camera feed (top right)
- Current emotion being captured (left side)
- Progress indicator (samples collected)
- Clickable CAPTURE button
- Instructions at bottom

### Face Puppeteer
- Your camera feed
- Target image animated with your expressions
- Side-by-side comparison
- FPS counter
- Processing status

---

## 🔧 Troubleshooting

**Camera not working?**
- Make sure no other app is using the camera
- Try closing other video apps (Zoom, Teams, etc.)

**Python not found?**
- Install Python from: https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

**Packages failing to install?**
- Run Command Prompt as Administrator
- Try: `pip install opencv-python mediapipe numpy`

**Face Puppeteer is slow?**
- Close other programs to free up CPU
- Use smaller images (system automatically resizes to 800px max width)
- Performance improves after a few seconds as the system optimizes

**Emotion detection not accurate?**
- Run the Emotion Trainer first to create a personalized profile
- Ensure good lighting on your face
- Face the camera directly

---

## 📁 Files
- `emotion_detector.py` - Real-time emotion detection
- `emotion_trainer.py` - Calibration training system
- `face_puppeteer.py` - Face animation/puppeteering
- `start_emotion_detector.bat` - Windows batch launcher with menu
- `start_emotion_detector.ps1` - PowerShell launcher with menu
- `face_landmarker.task` - MediaPipe face model (auto-downloaded)
- `emotion_calibration_profile.json` - Your personalized calibration (created by trainer)
- `requirements.txt` - Python dependencies

---

## 💡 Tips
- **For best emotion detection**: Run Emotion Trainer first to create a calibration profile
- Good lighting improves all applications
- Face the camera directly for best results
- Face Puppeteer works best with clear, front-facing photos
- Training snapshots and emotion data are saved automatically for reference
- Keep your full face visible in frame
- The detector analyzes 468+ facial landmarks (exceeds 120 minimum requirement)

---

**Enjoy real-time emotion detection!** 🎭
