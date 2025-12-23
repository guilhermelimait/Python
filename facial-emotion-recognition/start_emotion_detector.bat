@echo off
REM ========================================
REM Facial Emotion Detector Launcher
REM ========================================

echo.
echo ====================================
echo  Facial Emotion Detector
echo ====================================
echo.
echo Choose what to run:
echo.
echo 1. Emotion Detector (Real-time detection)
echo 2. Emotion Trainer (Calibrate to your face)
echo 3. Face Puppeteer (Control a photo with your face)
echo 4. Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto detector
if "%choice%"=="2" goto trainer
if "%choice%"=="3" goto puppeteer
if "%choice%"=="4" goto end
echo Invalid choice. Exiting.
goto end

:detector
echo.
echo Starting Emotion Detector...
python emotion_detector.py
if errorlevel 1 (
    echo.
    echo ERROR: Emotion detector exited with an error
    pause
    exit /b 1
)
goto end

:trainer
echo.
echo Starting Emotion Trainer...
python emotion_trainer.py
if errorlevel 1 (
    echo.
    echo ERROR: Emotion trainer exited with an error
    pause
    exit /b 1
)
goto end

:puppeteer
echo.
echo Starting Face Puppeteer...
python face_puppeteer.py
if errorlevel 1 (
    echo.
    echo ERROR: Face puppeteer exited with an error
    pause
    exit /b 1
)
goto end

:end
echo.
echo Application closed.
pause
