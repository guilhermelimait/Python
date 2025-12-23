# ========================================
# Facial Emotion Detector Launcher (PowerShell)
# ========================================

Write-Host ""
Write-Host "====================================" -ForegroundColor Cyan
Write-Host " Facial Emotion Detector" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "[1/3] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "✗ ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if required packages are installed
Write-Host "[2/3] Checking dependencies..." -ForegroundColor Yellow
$checkPackages = python -c "import cv2, mediapipe, numpy" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Installing required packages..." -ForegroundColor Yellow
    pip install opencv-python mediapipe numpy requests
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ ERROR: Failed to install packages" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
    Write-Host "✓ Packages installed successfully" -ForegroundColor Green
}
else {
    Write-Host "✓ All dependencies installed" -ForegroundColor Green
}

Write-Host "[3/3] Ready to launch!" -ForegroundColor Yellow
Write-Host ""
Write-Host "Choose what to run:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Emotion Detector (Real-time detection)" -ForegroundColor White
Write-Host "2. Emotion Trainer (Calibrate to your face)" -ForegroundColor White
Write-Host "3. Exit" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Enter your choice (1-3)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "Starting Emotion Detector..." -ForegroundColor Green
        Write-Host "Controls:" -ForegroundColor Cyan
        Write-Host "  - Press 'q' to quit" -ForegroundColor White
        Write-Host "  - Press 's' to save snapshot" -ForegroundColor White
        Write-Host "  - Press 'd' to toggle debug mode" -ForegroundColor White
        Write-Host ""
        
        python emotion_detector.py
        
        if ($LASTEXITCODE -ne 0) {
            Write-Host ""
            Write-Host "✗ ERROR: Emotion detector exited with an error" -ForegroundColor Red
        }
        else {
            Write-Host ""
            Write-Host "✓ Emotion detector closed successfully." -ForegroundColor Green
        }
    }
    "2" {
        Write-Host ""
        Write-Host "Starting Emotion Trainer..." -ForegroundColor Green
        Write-Host ""
        Write-Host "This will capture YOUR facial expressions for calibration." -ForegroundColor Yellow
        Write-Host "Follow the on-screen instructions for each emotion." -ForegroundColor Yellow
        Write-Host ""
        
        python emotion_trainer.py
        
        if ($LASTEXITCODE -ne 0) {
            Write-Host ""
            Write-Host "✗ ERROR: Emotion trainer exited with an error" -ForegroundColor Red
        }
        else {
            Write-Host ""
            Write-Host "✓ Emotion trainer closed successfully." -ForegroundColor Green
        }
    }
    "3" {
        Write-Host ""
        Write-Host "Exiting..." -ForegroundColor Yellow
        exit 0
    }
    default {
        Write-Host ""
        Write-Host "✗ Invalid choice. Exiting." -ForegroundColor Red
    }
}

Write-Host ""
Read-Host "Press Enter to exit"
