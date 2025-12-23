#!/usr/bin/env python3
"""Train the emotion detector with your personal facial expressions.

Captures your facial metrics for each emotion to create a personalized profile.
"""
import importlib
import subprocess
import sys
import json
from datetime import datetime
import math
import os


def ensure_dependencies():
    missing = []
    for pkg, module in [
        ("opencv-python", "cv2"),
        ("mediapipe", "mediapipe"),
        ("numpy", "numpy"),
    ]:
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

import cv2
import mediapipe as mp
import numpy as np


class EmotionTrainer:
    """Collect training data for personalized emotion detection."""
    
    def __init__(self):
        """Initialize the trainer."""
        self.detector = self._setup_face_landmarker()
        self.training_data = []
        self.emotions_to_train = [
            "Neutral", "Happy", "Sad", "Angry", 
            "Surprised", "Disgusted", "Sleepy"
        ]
        self.current_emotion_index = 0
        
    def _setup_face_landmarker(self):
        """Setup MediaPipe face landmarker."""
        import urllib.request
        
        model_path = "face_landmarker.task"
        if not os.path.exists(model_path):
            print("Downloading face landmarker model...")
            url = "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"
            urllib.request.urlretrieve(url, model_path)
            print("✓ Model downloaded")
        
        base_options = mp.tasks.BaseOptions(model_asset_path=model_path)
        options = mp.tasks.vision.FaceLandmarkerOptions(
            base_options=base_options,
            output_face_blendshapes=False,
            output_facial_transformation_matrixes=False,
            num_faces=1,
            min_face_detection_confidence=0.5,
            min_face_presence_confidence=0.5,
            min_tracking_confidence=0.5,
            running_mode=mp.tasks.vision.RunningMode.VIDEO
        )
        return mp.tasks.vision.FaceLandmarker.create_from_options(options)
    
    def calculate_distance(self, point1, point2):
        """Calculate Euclidean distance between two points."""
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    
    def extract_metrics(self, face_landmarks):
        """Extract facial metrics from landmarks."""
        if len(face_landmarks) < 468:
            return None
        
        # Same landmark points as main detector
        left_mouth = face_landmarks[61]
        right_mouth = face_landmarks[291]
        upper_lip_top = face_landmarks[13]
        lower_lip_bottom = face_landmarks[14]
        lower_lip_center = face_landmarks[17]
        
        left_eye_top = face_landmarks[159]
        left_eye_bottom = face_landmarks[145]
        right_eye_top = face_landmarks[386]
        right_eye_bottom = face_landmarks[374]
        
        left_eyebrow_inner = face_landmarks[55]
        left_eyebrow_outer = face_landmarks[46]
        right_eyebrow_inner = face_landmarks[285]
        right_eyebrow_outer = face_landmarks[276]
        
        # Calculate metrics
        mouth_height = self.calculate_distance(upper_lip_top, lower_lip_bottom)
        mouth_width = self.calculate_distance(left_mouth, right_mouth)
        mouth_aspect_ratio = mouth_height / (mouth_width + 0.001)
        
        mouth_corner_avg_y = (left_mouth.y + right_mouth.y) / 2
        mouth_center_y = lower_lip_center.y
        smile_curve = mouth_center_y - mouth_corner_avg_y
        
        left_eye_height = self.calculate_distance(left_eye_top, left_eye_bottom)
        right_eye_height = self.calculate_distance(right_eye_top, right_eye_bottom)
        eye_aspect_ratio = (left_eye_height + right_eye_height) / 2
        
        left_brow_raise = left_eye_top.y - left_eyebrow_inner.y
        right_brow_raise = right_eye_top.y - right_eyebrow_inner.y
        eyebrow_raise = (left_brow_raise + right_brow_raise) / 2
        
        left_brow_angle = left_eyebrow_inner.y - left_eyebrow_outer.y
        right_brow_angle = right_eyebrow_inner.y - right_eyebrow_outer.y
        
        return {
            "smile_curve": float(smile_curve),
            "mouth_aspect_ratio": float(mouth_aspect_ratio),
            "eye_aspect_ratio": float(eye_aspect_ratio),
            "eyebrow_raise": float(eyebrow_raise),
            "left_brow_angle": float(left_brow_angle),
            "right_brow_angle": float(right_brow_angle)
        }
    
    def draw_button(self, image, x, y, w, h, text, color, mouse_x, mouse_y):
        """Draw a clickable button."""
        # Check if mouse is over button
        hover = x < mouse_x < x + w and y < mouse_y < y + h
        button_color = tuple(min(255, c + 30) for c in color) if hover else color
        
        # Draw button
        cv2.rectangle(image, (x, y), (x + w, y + h), button_color, -1)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
        
        # Draw text
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        text_x = x + (w - text_size[0]) // 2
        text_y = y + (h + text_size[1]) // 2
        cv2.putText(image, text, (text_x, text_y),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        return hover
    
    def mouse_callback(self, event, x, y, flags, param):
        """Handle mouse events."""
        if event == cv2.EVENT_MOUSEMOVE:
            self.mouse_x = x
            self.mouse_y = y
        elif event == cv2.EVENT_LBUTTONDOWN:
            self.mouse_clicked = True
    
    def run_training(self):
        """Run the training session."""
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Could not open camera")
            return
        
        print("\n" + "="*60)
        print("🎓 EMOTION DETECTOR TRAINING MODE")
        print("="*60)
        print("This will capture YOUR facial expressions for each emotion.")
        print("The detector will then calibrate to YOUR face!")
        print("\nInstructions:")
        print("1. Make the emotion shown on screen")
        print("2. Click 'CAPTURE' button or press SPACE (3 samples per emotion)")
        print("3. Press 'q' to quit")
        print("="*60 + "\n")
        
        current_emotion = self.emotions_to_train[self.current_emotion_index]
        samples_per_emotion = 3
        current_samples = 0
        frame_count = 0
        
        # Mouse tracking
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_clicked = False
        
        cv2.namedWindow('Emotion Training')
        cv2.setMouseCallback('Emotion Training', self.mouse_callback)
        
        instructions = {
            "Neutral": "Relax your face completely. No expression.",
            "Happy": "SMILE naturally! Corners of mouth UP.",
            "Sad": "FROWN. Corners of mouth DOWN. Look sad.",
            "Angry": "FURROW your brows! Tense face. Look angry.",
            "Surprised": "Wide eyes! Open mouth! Raise eyebrows!",
            "Disgusted": "Wrinkle nose! Upper lip UP. 'Eww' face.",
            "Sleepy": "HALF-CLOSE your eyes. Relaxed, tired face."
        }
        
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                continue
            
            frame_count += 1
            camera_frame = cv2.flip(image, 1)
            
            # Detect landmarks
            rgb_frame = cv2.cvtColor(camera_frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            timestamp_ms = frame_count * 33
            
            result = self.detector.detect_for_video(mp_image, timestamp_ms)
            
            # Create main display (1280x720)
            display_w, display_h = 1280, 720
            display = np.zeros((display_h, display_w, 3), dtype=np.uint8)
            display[:] = (40, 40, 40)  # Dark gray background
            
            # === TOP RIGHT: Camera feed ===
            cam_h, cam_w = camera_frame.shape[:2]
            # Resize camera to fit top right (500x375)
            camera_display_w, camera_display_h = 500, 375
            camera_resized = cv2.resize(camera_frame, (camera_display_w, camera_display_h))
            
            # Draw landmarks on camera
            if result.face_landmarks:
                for face_landmarks in result.face_landmarks:
                    for idx in range(0, len(face_landmarks), 8):
                        landmark = face_landmarks[idx]
                        x = int(landmark.x * camera_display_w)
                        y = int(landmark.y * camera_display_h)
                        cv2.circle(camera_resized, (x, y), 2, (0, 255, 0), -1)
            
            # Place camera in top right
            cam_x = display_w - camera_display_w - 20
            cam_y = 20
            display[cam_y:cam_y+camera_display_h, cam_x:cam_x+camera_display_w] = camera_resized
            
            # Draw camera border
            cv2.rectangle(display, (cam_x-2, cam_y-2), 
                         (cam_x+camera_display_w+2, cam_y+camera_display_h+2),
                         (255, 255, 255), 2)
            
            # === TOP LEFT: Emotion info ===
            info_x = 30
            info_y = 50
            
            # Current emotion (large)
            cv2.putText(display, "MAKE THIS EMOTION:", (info_x, info_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 150, 150), 2)
            
            emotion_colors = {
                "Neutral": (200, 200, 200),
                "Happy": (0, 255, 0),
                "Sad": (255, 100, 100),
                "Angry": (0, 0, 255),
                "Surprised": (0, 255, 255),
                "Disgusted": (180, 0, 180),
                "Sleepy": (100, 100, 200)
            }
            emotion_color = emotion_colors.get(current_emotion, (255, 255, 255))
            
            cv2.putText(display, current_emotion.upper(), (info_x, info_y + 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 2.0, emotion_color, 4)
            
            # Progress bars
            progress_y = info_y + 130
            cv2.putText(display, f"Sample Progress: {current_samples}/{samples_per_emotion}",
                       (info_x, progress_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)
            
            # Progress bar for current emotion
            bar_w = 400
            bar_h = 30
            bar_x = info_x
            bar_y = progress_y + 15
            cv2.rectangle(display, (bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h), (80, 80, 80), -1)
            fill_w = int((current_samples / samples_per_emotion) * bar_w)
            cv2.rectangle(display, (bar_x, bar_y), (bar_x + fill_w, bar_y + bar_h), emotion_color, -1)
            cv2.rectangle(display, (bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h), (255, 255, 255), 2)
            
            # Overall progress
            overall_y = bar_y + bar_h + 40
            total_emotions = len(self.emotions_to_train)
            cv2.putText(display, f"Overall: {self.current_emotion_index + 1}/{total_emotions} emotions",
                       (info_x, overall_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)
            
            overall_bar_y = overall_y + 15
            cv2.rectangle(display, (bar_x, overall_bar_y), (bar_x + bar_w, overall_bar_y + bar_h), (80, 80, 80), -1)
            overall_fill = int((self.current_emotion_index / total_emotions) * bar_w)
            cv2.rectangle(display, (bar_x, overall_bar_y), (bar_x + overall_fill, overall_bar_y + bar_h), (0, 200, 255), -1)
            cv2.rectangle(display, (bar_x, overall_bar_y), (bar_x + bar_w, overall_bar_y + bar_h), (255, 255, 255), 2)
            
            # Face detection status
            status_y = overall_bar_y + bar_h + 40
            if result.face_landmarks:
                status_text = "✓ Face Detected - Ready to Capture!"
                status_color = (0, 255, 0)
            else:
                status_text = "✗ No Face Detected"
                status_color = (0, 0, 255)
            cv2.putText(display, status_text, (info_x, status_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, status_color, 2)
            
            # === BOTTOM: Instructions ===
            instructions_y = display_h - 180
            
            # Background for instructions
            cv2.rectangle(display, (0, instructions_y - 20), (display_w, display_h), (30, 30, 30), -1)
            
            cv2.putText(display, "HOW TO MAKE THIS EMOTION:",
                       (30, instructions_y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
            
            instruction_text = instructions[current_emotion]
            cv2.putText(display, instruction_text,
                       (30, instructions_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
            
            # Draw CAPTURE button
            button_w, button_h = 300, 70
            button_x = (display_w - button_w) // 2
            button_y = instructions_y + 80
            
            button_color = (0, 200, 0) if result.face_landmarks else (100, 100, 100)
            button_hover = self.draw_button(display, button_x, button_y, button_w, button_h,
                                           "CAPTURE SAMPLE", button_color,
                                           self.mouse_x, self.mouse_y)
            
            # Quit instruction
            cv2.putText(display, "Press 'Q' to quit",
                       (display_w - 200, display_h - 20),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)
            
            cv2.imshow('Emotion Training', display)
            
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q'):
                break
            elif (key == ord(' ') or (self.mouse_clicked and button_hover)) and result.face_landmarks:
                # Capture sample
                self.mouse_clicked = False  # Reset click
                
                for face_landmarks in result.face_landmarks:
                    metrics = self.extract_metrics(face_landmarks)
                    if metrics:
                        sample = {
                            "emotion": current_emotion,
                            "metrics": metrics,
                            "timestamp": datetime.now().isoformat()
                        }
                        self.training_data.append(sample)
                        current_samples += 1
                        
                        print(f"✓ Captured {current_emotion} sample {current_samples}/{samples_per_emotion}")
                        
                        # Save snapshot
                        snapshot_file = f"training_{current_emotion}_{current_samples}.jpg"
                        cv2.imwrite(snapshot_file, camera_frame)
                        
                        if current_samples >= samples_per_emotion:
                            # Move to next emotion
                            current_samples = 0
                            self.current_emotion_index += 1
                            
                            if self.current_emotion_index >= len(self.emotions_to_train):
                                print("\n🎉 Training complete!")
                                cap.release()
                                cv2.destroyAllWindows()
                                self.save_training_data()
                                self.analyze_and_calibrate()
                                return
                            
                            current_emotion = self.emotions_to_train[self.current_emotion_index]
                            print(f"\n→ Next emotion: {current_emotion}")
                        
                        break
            
            # Reset mouse click if not on button
            if self.mouse_clicked:
                self.mouse_clicked = False
        
        cap.release()
        cv2.destroyAllWindows()
        
        if self.training_data:
            self.save_training_data()
            self.analyze_and_calibrate()
    
    def save_training_data(self):
        """Save training data to file."""
        filename = f"emotion_training_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(self.training_data, f, indent=2)
        print(f"\n💾 Training data saved: {filename}")
    
    def analyze_and_calibrate(self):
        """Analyze training data and create calibration profile."""
        if not self.training_data:
            print("No training data to analyze")
            return
        
        print("\n" + "="*60)
        print("📊 ANALYZING YOUR FACIAL METRICS")
        print("="*60)
        
        # Group by emotion
        emotion_metrics = {}
        for sample in self.training_data:
            emotion = sample["emotion"]
            if emotion not in emotion_metrics:
                emotion_metrics[emotion] = []
            emotion_metrics[emotion].append(sample["metrics"])
        
        # Calculate averages for each emotion
        calibration = {}
        for emotion, metrics_list in emotion_metrics.items():
            avg_metrics = {}
            for key in metrics_list[0].keys():
                values = [m[key] for m in metrics_list]
                avg_metrics[key] = sum(values) / len(values)
            calibration[emotion] = avg_metrics
            
            print(f"\n{emotion}:")
            print(f"  Smile curve: {avg_metrics['smile_curve']:.4f}")
            print(f"  Mouth ratio: {avg_metrics['mouth_aspect_ratio']:.4f}")
            print(f"  Eye ratio: {avg_metrics['eye_aspect_ratio']:.4f}")
            print(f"  Brow raise: {avg_metrics['eyebrow_raise']:.4f}")
        
        # Save calibration profile
        profile_file = "emotion_calibration_profile.json"
        with open(profile_file, 'w') as f:
            json.dump(calibration, f, indent=2)
        
        print("\n" + "="*60)
        print(f"✓ Calibration profile saved: {profile_file}")
        print("="*60)
        print("\n📋 RECOMMENDED THRESHOLDS FOR YOUR FACE:")
        print("="*60)
        
        # Generate threshold recommendations
        happy_smile = calibration.get("Happy", {}).get("smile_curve", 0.007)
        neutral_smile = calibration.get("Neutral", {}).get("smile_curve", 0.000)
        sad_smile = calibration.get("Sad", {}).get("smile_curve", -0.003)
        
        sleepy_eye = calibration.get("Sleepy", {}).get("eye_aspect_ratio", 0.020)
        neutral_eye = calibration.get("Neutral", {}).get("eye_aspect_ratio", 0.022)
        
        print(f"\nHappy threshold: smile_curve > {happy_smile * 0.8:.4f}")
        print(f"Sad threshold: smile_curve < {sad_smile * 0.8:.4f}")
        print(f"Sleepy threshold: eye_ratio < {sleepy_eye * 1.05:.4f}")
        print(f"Neutral smile range: {neutral_smile - 0.003:.4f} to {neutral_smile + 0.003:.4f}")
        
        print("\n💡 TIP: Run 'python emotion_detector.py --calibrated' to use this profile!")
        print("="*60)


def main():
    """Main entry point."""
    trainer = EmotionTrainer()
    trainer.run_training()


if __name__ == "__main__":
    main()
