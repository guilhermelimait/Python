# Facial Emotion Detection Suite

A comprehensive real-time facial emotion detection system with personalized calibration and face puppeteering capabilities using MediaPipe and OpenCV.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![MediaPipe](https://img.shields.io/badge/mediapipe-0.10+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Features

### 1. **Real-Time Emotion Detection**
- Detects 7 emotions: Happy, Sad, Surprised, Angry, Disgusted, Sleepy, Neutral
- 468 facial landmarks tracking
- Real-time confidence scoring
- Personalized calibration support
- Debug mode for detailed emotion scores

### 2. **Emotion Trainer**
- Create personalized emotion profiles
- Capture 3 samples per emotion
- Improves detection accuracy significantly
- User-friendly interface with visual feedback

### 3. **Face Puppeteer**
- Animate photos with your facial expressions
- Real-time face deformation
- Multiple display modes
- Works with any image containing a face

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Webcam (built-in or external)
- Windows, macOS, or Linux

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/facial-emotion-detection.git
   cd facial-emotion-detection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   
   **Windows:**
   ```bash
   start_emotion_detector.bat
   ```
   
   **macOS/Linux:**
   ```bash
   python emotion_detector.py
   ```

## 📖 Usage

### Menu Options

When you run the launcher, you'll see:

```
====================================
 Facial Emotion Detector
====================================

Choose what to run:

1. Emotion Detector (Real-time detection)
2. Emotion Trainer (Calibrate to your face)
3. Face Puppeteer (Control a photo with your face)
4. Exit
```

### 1. Emotion Detector

Run real-time emotion detection from your webcam.

**Controls:**
- `q` - Quit
- `s` - Save snapshot
- `d` - Toggle debug mode

**Tips:**
- Run the Emotion Trainer first for best accuracy
- Ensure good lighting
- Face the camera directly

### 2. Emotion Trainer

Create a personalized calibration profile for improved accuracy.

**Process:**
1. Position your face in the camera
2. Follow on-screen instructions for each emotion
3. Click "CAPTURE" button 3 times per emotion
4. Click "FINISH" when complete

**Emotions to Train:**
- Neutral
- Happy
- Sad
- Surprised
- Angry
- Disgusted
- Sleepy

### 3. Face Puppeteer

Animate a photo using your facial expressions.

**Controls:**
- `q` - Quit
- `s` - Save snapshot
- `1` - Show original image
- `2` - Show animated image
- `3` - Side-by-side view

**Steps:**
1. Place an image in the project folder
2. Select it from the list or enter the path
3. Move your face to control the image

## 🔧 How It Works

### Emotion Detection Algorithm

1. **Landmark Detection**: MediaPipe detects 468 facial landmarks in real-time
2. **Feature Extraction**: Calculates key facial metrics:
   - Smile curve (mouth corners curvature)
   - Mouth aspect ratio (openness)
   - Eye aspect ratio (how wide eyes are)
   - Eyebrow raise (distance from eyes)
   - Brow angles (inner eyebrow positions)

3. **Emotion Scoring**: Each emotion gets a score based on facial geometry:
   ```python
   Happy: high smile_curve, normal mouth_aspect_ratio
   Sad: low mouth corners, low eyebrows
   Surprised: high mouth and eyes aspect ratio, raised eyebrows
   Angry: low eyebrow angle, squinted eyes
   Disgusted: wrinkled nose, raised upper lip
   Sleepy: low eye aspect ratio
   Neutral: baseline values
   ```

4. **Calibration**: Uses personalized thresholds from training data for improved accuracy

### Face Puppeteer Algorithm

1. **Face Detection**: Detects landmarks in both your face and the target image
2. **Normalization**: Maps your facial expression to the target face space
3. **Triangulation**: Creates Delaunay triangulation for both faces
4. **Warping**: Deforms each triangle to match your expression
5. **Rendering**: Displays the animated result in real-time

## 📁 Project Structure

```
facial-emotion-detection/
├── emotion_detector.py           # Main emotion detection application
├── emotion_trainer.py             # Calibration training system
├── face_puppeteer.py              # Face animation application
├── start_emotion_detector.bat     # Windows launcher
├── start_emotion_detector.ps1     # PowerShell launcher
├── requirements.txt               # Python dependencies
├── QUICK_START.md                 # Detailed user guide
├── README.md                      # This file
└── .gitignore                     # Git ignore rules
```

## 🛠️ Technical Details

### Dependencies
- **OpenCV** (`opencv-python`): Image processing and display
- **MediaPipe** (`mediapipe`): Face landmark detection
- **NumPy** (`numpy`): Numerical computations

### Performance
- **Emotion Detection**: 30+ FPS on modern hardware
- **Face Puppeteer**: 15-30 FPS depending on image size
- **Landmark Detection**: 468 points per frame

### Model
- Uses MediaPipe Face Landmarker model
- Automatically downloaded on first run (~10MB)
- Runs locally - no cloud API calls

## 🎨 Customization

### Adjust Emotion Thresholds

Edit the thresholds in `emotion_detector.py`:

```python
self.default_thresholds = {
    "smile_threshold": 0.05,
    "mouth_open_threshold": 0.3,
    "eye_close_threshold": 0.2,
    # ... more thresholds
}
```

### Change Display Layout

Modify display coordinates in the `run()` method:
- Camera position: `display[y:y+h, x:x+w]`
- Text position: `cv2.putText(..., (x, y), ...)`

## 📊 Output Files

### Generated Files
- `emotion_calibration_profile.json` - Your personalized thresholds
- `training_[emotion]_[1-3].jpg` - Training snapshots
- `emotion_snapshot_*.jpg` - Saved emotion snapshots
- `puppeteer_snapshot_*.jpg` - Saved puppeteer outputs

## 🐛 Troubleshooting

**Camera not detected:**
- Close other applications using the camera
- Check camera permissions in system settings

**Low FPS:**
- Close resource-intensive applications
- For Face Puppeteer: Use smaller images
- Reduce processing frequency in code

**Emotions not accurate:**
- Run Emotion Trainer to create a calibration profile
- Ensure good, even lighting
- Face the camera directly

**MediaPipe errors:**
- Update MediaPipe: `pip install --upgrade mediapipe`
- Ensure Python 3.8+

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [MediaPipe](https://google.github.io/mediapipe/) for face landmark detection
- [OpenCV](https://opencv.org/) for image processing
- Inspired by real-time emotion recognition research

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ using Python, MediaPipe, and OpenCV**

**Part of the [Python Projects Collection](../README.md)**

