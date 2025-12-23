#!/usr/bin/env python3
"""Real-time facial emotion detection using MediaPipe landmarks.

Detects emotions (Happy, Sad, Surprised, Angry, Neutral) instantly based on facial geometry.
Much faster than LLM analysis - works in real-time!
"""
import cv2
import mediapipe as mp
import numpy as np
import json
from datetime import datetime
import math


class EmotionDetector:
    """Real-time emotion detection from facial landmarks."""
    
    def __init__(self, use_calibration=True):
        """Initialize the detector."""
        self.detector = self._setup_face_landmarker()
        self.calibration = None
        self.using_calibration = False
        
        # Try to load calibration profile
        if use_calibration:
            self.load_calibration()
    
    def load_calibration(self):
        """Load personalized calibration profile if available."""
        import os
        
        if os.path.exists("emotion_calibration_profile.json"):
            try:
                with open("emotion_calibration_profile.json", 'r') as f:
                    self.calibration = json.load(f)
                self.using_calibration = True
                print("✓ Loaded personalized calibration profile!")
                print(f"  Calibrated for: {', '.join(self.calibration.keys())}")
            except Exception as e:
                print(f"⚠ Could not load calibration: {e}")
                print("  Using default thresholds")
        else:
            print("ℹ No calibration profile found. Using default thresholds.")
            print("  Run 'Emotion Trainer' to create personalized profile.")
    
    def get_threshold(self, emotion, metric, default):
        """Get threshold from calibration or use default."""
        if not self.calibration or emotion not in self.calibration:
            return default
        
        calibrated_value = self.calibration[emotion].get(metric)
        if calibrated_value is None:
            return default
        
        return calibrated_value
        
    def _setup_face_landmarker(self):
        """Setup MediaPipe face landmarker."""
        import os
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
    
    def detect_emotion(self, face_landmarks):
        """Detect emotion from facial landmarks with improved accuracy.
        
        Returns: dict with emotion, confidence, and metrics
        """
        if len(face_landmarks) < 468:
            return {"emotion": "Unknown", "confidence": 0.0, "metrics": {}}
        
        # Key landmarks for emotion detection
        left_mouth = face_landmarks[61]
        right_mouth = face_landmarks[291]
        upper_lip_top = face_landmarks[13]
        lower_lip_bottom = face_landmarks[14]
        upper_lip_center = face_landmarks[0]
        lower_lip_center = face_landmarks[17]
        
        # Eyes
        left_eye_top = face_landmarks[159]
        left_eye_bottom = face_landmarks[145]
        right_eye_top = face_landmarks[386]
        right_eye_bottom = face_landmarks[374]
        left_eye_inner = face_landmarks[133]
        right_eye_inner = face_landmarks[362]
        
        # Eyebrows - using multiple points for better accuracy
        left_eyebrow_inner = face_landmarks[55]
        left_eyebrow_outer = face_landmarks[46]
        right_eyebrow_inner = face_landmarks[285]
        right_eyebrow_outer = face_landmarks[276]
        
        # Face reference points
        nose_tip = face_landmarks[1]
        face_center = face_landmarks[168]
        
        # Calculate emotion metrics
        
        # 1. Mouth metrics
        mouth_height = self.calculate_distance(upper_lip_top, lower_lip_bottom)
        mouth_width = self.calculate_distance(left_mouth, right_mouth)
        mouth_aspect_ratio = mouth_height / (mouth_width + 0.001)
        
        # 2. Smile detection - check if corners are higher than center
        # Positive = smile, Negative = frown
        mouth_corner_avg_y = (left_mouth.y + right_mouth.y) / 2
        mouth_center_y = lower_lip_center.y
        smile_curve = mouth_center_y - mouth_corner_avg_y
        
        # 3. Eye metrics
        left_eye_height = self.calculate_distance(left_eye_top, left_eye_bottom)
        right_eye_height = self.calculate_distance(right_eye_top, right_eye_bottom)
        eye_aspect_ratio = (left_eye_height + right_eye_height) / 2
        
        # 4. Eyebrow metrics (relative to eyes)
        left_brow_raise = left_eye_top.y - left_eyebrow_inner.y
        right_brow_raise = right_eye_top.y - right_eyebrow_inner.y
        eyebrow_raise = (left_brow_raise + right_brow_raise) / 2
        
        # 5. Eyebrow angle (for anger/concern detection)
        left_brow_angle = left_eyebrow_inner.y - left_eyebrow_outer.y
        right_brow_angle = right_eyebrow_inner.y - right_eyebrow_outer.y
        
        # Store metrics for display
        metrics = {
            "smile_curve": float(smile_curve * 1000),
            "mouth_open": float(mouth_aspect_ratio * 100),
            "eye_open": float(eye_aspect_ratio * 100),
            "brow_raise": float(eyebrow_raise * 100)
        }
        
        # Get calibrated thresholds or use defaults
        if self.using_calibration:
            # Use calibrated values to determine thresholds
            happy_smile = self.get_threshold("Happy", "smile_curve", 0.007)
            neutral_smile = self.get_threshold("Neutral", "smile_curve", 0.000)
            sad_smile = self.get_threshold("Sad", "smile_curve", -0.003)
            sleepy_eye = self.get_threshold("Sleepy", "eye_aspect_ratio", 0.020)
            neutral_eye = self.get_threshold("Neutral", "eye_aspect_ratio", 0.022)
            
            # Calculate dynamic thresholds based on calibration
            happy_threshold_low = happy_smile * 0.6
            happy_threshold_high = happy_smile * 0.9
            sad_threshold = sad_smile * 0.8
            sleepy_threshold = sleepy_eye * 1.05
        else:
            # Default thresholds
            happy_threshold_low = 0.004
            happy_threshold_high = 0.007
            sad_threshold = -0.003
            sleepy_threshold = 0.021
        
        # Emotion detection with improved logic
        # Using a scoring system instead of if-elif
        emotion_scores = {
            "Neutral": 0.4,  # Higher base score for neutral
            "Happy": 0.0,
            "Sad": 0.0,
            "Surprised": 0.0,
            "Angry": 0.0,
            "Disgusted": 0.0,
            "Sleepy": 0.0
        }
        
        # === HAPPY DETECTION ===
        # Strong smile curve + not too wide mouth (use calibrated thresholds)
        if smile_curve > happy_threshold_high:
            emotion_scores["Happy"] += 0.5
            if smile_curve > happy_threshold_high * 1.3:
                emotion_scores["Happy"] += 0.3
        elif smile_curve > happy_threshold_low and mouth_aspect_ratio < 0.35:
            emotion_scores["Happy"] += 0.3
        
        # === SAD DETECTION ===
        # Downturned mouth + slightly closed eyes (use calibrated thresholds)
        if smile_curve < sad_threshold:
            emotion_scores["Sad"] += 0.5
            if smile_curve < -0.006:
                emotion_scores["Sad"] += 0.3
        if eyebrow_raise < 0.02 and smile_curve < -0.002:
            emotion_scores["Sad"] += 0.2
        
        # === SURPRISED DETECTION ===
        # Wide eyes + open mouth + raised eyebrows
        if eye_aspect_ratio > 0.026:
            emotion_scores["Surprised"] += 0.3
        if mouth_aspect_ratio > 0.5:
            emotion_scores["Surprised"] += 0.3
        if eyebrow_raise > 0.025:
            emotion_scores["Surprised"] += 0.3
        if eye_aspect_ratio > 0.026 and mouth_aspect_ratio > 0.5:
            emotion_scores["Surprised"] += 0.2
        
        # === ANGRY DETECTION === (Made more sensitive)
        # Lowered/furrowed brows + tension + slight frown
        if eyebrow_raise < 0.020:  # Increased from 0.018
            emotion_scores["Angry"] += 0.4  # Increased
        if smile_curve < 0.000 and eye_aspect_ratio < 0.023:  # Made less strict
            emotion_scores["Angry"] += 0.4  # Increased
        # Eyebrows angled down (inner part lower)
        if left_brow_angle < -0.001 or right_brow_angle < -0.001:  # Made more sensitive
            emotion_scores["Angry"] += 0.3
        # Tense face - mouth slightly closed
        if mouth_aspect_ratio < 0.30 and abs(smile_curve) < 0.003:
            emotion_scores["Angry"] += 0.2
        
        # === DISGUSTED DETECTION === (Made more sensitive)
        # Wrinkled nose area + raised upper lip + narrowed eyes
        if mouth_aspect_ratio < 0.28 and smile_curve > -0.002:  # Made less strict
            emotion_scores["Disgusted"] += 0.4  # Increased
        if eye_aspect_ratio < 0.021 and smile_curve > -0.001:  # Adjusted
            emotion_scores["Disgusted"] += 0.3  # Increased
        # Slight nose wrinkle creates specific mouth shape
        if 0.15 < mouth_aspect_ratio < 0.32 and eyebrow_raise < 0.021:
            emotion_scores["Disgusted"] += 0.3
        
        # === SLEEPY/TIRED DETECTION === (use calibrated thresholds)
        # Droopy/half-closed eyes + relaxed face + no strong expressions
        if eye_aspect_ratio < sleepy_threshold:
            emotion_scores["Sleepy"] += 0.5  # Increased
            if eye_aspect_ratio < 0.019:
                emotion_scores["Sleepy"] += 0.3
        # Relaxed mouth (not smiling or frowning strongly)
        if abs(smile_curve) < 0.004 and mouth_aspect_ratio < 0.38:  # More lenient
            emotion_scores["Sleepy"] += 0.3  # Increased
        # Slightly lowered or relaxed eyebrows
        if 0.017 < eyebrow_raise < 0.024:  # Wider range
            emotion_scores["Sleepy"] += 0.2
        
        # === NEUTRAL REFINEMENT ===
        # If no strong features detected, boost neutral
        max_non_neutral = max([score for emotion, score in emotion_scores.items() if emotion != "Neutral"])
        if max_non_neutral < 0.4:  # Reduced threshold to make neutral less dominant
            emotion_scores["Neutral"] = 0.8
        
        # Penalize neutral if there are strong facial movements
        if abs(smile_curve) > 0.003 or abs(eyebrow_raise - 0.020) > 0.006:  # Made more sensitive
            emotion_scores["Neutral"] *= 0.3  # Stronger penalty
        
        # Get the emotion with highest score
        emotion = max(emotion_scores, key=emotion_scores.get)
        confidence = min(emotion_scores[emotion], 0.99)
        
        # Require minimum confidence threshold
        if confidence < 0.4:
            emotion = "Neutral"
            confidence = 0.5
        
        return {
            "emotion": emotion,
            "confidence": confidence,
            "metrics": metrics,
            "scores": {k: round(v, 2) for k, v in emotion_scores.items()}
        }
    
    def mouse_callback(self, event, x, y, flags, param):
        """Handle mouse events."""
        self.mouse_x = x
        self.mouse_y = y
    
    def run(self):
        """Run real-time emotion detection."""
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Could not open camera")
            return
        
        print("\n" + "="*50)
        print("🎭 REAL-TIME EMOTION DETECTOR")
        print("="*50)
        print("✓ Detects 468+ facial landmarks (>120 required)")
        print("✓ Emotions: Happy, Sad, Surprised, Angry, Disgusted, Sleepy, Neutral")
        print("\nControls:")
        print("  'q' - Quit")
        print("  's' - Save snapshot")
        print("  'd' - Toggle debug mode (show all emotion scores)")
        print("="*50 + "\n")
        
        frame_count = 0
        emotion_history = []
        fps_start_time = datetime.now()
        debug_mode = False
        
        # Mouse tracking
        self.mouse_x = 0
        self.mouse_y = 0
        
        cv2.namedWindow('Real-time Emotion Detection')
        cv2.setMouseCallback('Real-time Emotion Detection', self.mouse_callback)
        
        while cap.isOpened():
            success, camera_frame = cap.read()
            if not success:
                continue
            
            frame_count += 1
            camera_frame = cv2.flip(camera_frame, 1)
            
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
            camera_display_w, camera_display_h = 500, 375
            camera_resized = cv2.resize(camera_frame, (camera_display_w, camera_display_h))
            
            # Draw landmarks on camera
            if result.face_landmarks:
                for face_landmarks in result.face_landmarks:
                    for idx in range(0, len(face_landmarks), 8):
                        landmark = face_landmarks[idx]
                        x = int(landmark.x * camera_display_w)
                        y = int(landmark.y * camera_display_h)
                        cv2.circle(camera_resized, (x, y), 1, (0, 255, 0), -1)
                    
                    # Draw key points
                    key_points = [1, 33, 263, 13, 14, 61, 291]
                    for idx in key_points:
                        landmark = face_landmarks[idx]
                        x = int(landmark.x * camera_display_w)
                        y = int(landmark.y * camera_display_h)
                        cv2.circle(camera_resized, (x, y), 3, (0, 0, 255), -1)
            
            # Place camera in top right
            cam_x = display_w - camera_display_w - 20
            cam_y = 20
            display[cam_y:cam_y+camera_display_h, cam_x:cam_x+camera_display_w] = camera_resized
            cv2.rectangle(display, (cam_x-2, cam_y-2), 
                         (cam_x+camera_display_w+2, cam_y+camera_display_h+2),
                         (255, 255, 255), 2)
            
            # === LEFT SIDE: Information ===
            info_x = 30
            info_y = 50
            
            if result.face_landmarks:
                for face_landmarks in result.face_landmarks:
                    # Detect emotion
                    emotion_data = self.detect_emotion(face_landmarks)
                    emotion_history.append(emotion_data["emotion"])
                    if len(emotion_history) > 30:
                        emotion_history.pop(0)
                    
                    # Emotion colors
                    colors = {
                        "Happy": (0, 255, 0),
                        "Sad": (255, 100, 100),
                        "Surprised": (0, 255, 255),
                        "Angry": (0, 0, 255),
                        "Disgusted": (180, 0, 180),
                        "Sleepy": (100, 100, 200),
                        "Neutral": (200, 200, 200)
                    }
                    color = colors.get(emotion_data["emotion"], (255, 255, 255))
                    
                    # Status header
                    cv2.putText(display, "STATUS:", (info_x, info_y),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (150, 150, 150), 2)
                    
                    cv2.putText(display, f"Landmarks: {len(face_landmarks)}", 
                               (info_x, info_y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                    
                    # Calibration status
                    if self.using_calibration:
                        cal_text = "Profile: CALIBRATED"
                        cal_color = (0, 255, 255)
                    else:
                        cal_text = "Profile: DEFAULT"
                        cal_color = (150, 150, 150)
                    cv2.putText(display, cal_text, (info_x, info_y + 55),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, cal_color, 1)
                    
                    # Large emotion display
                    emotion_y = info_y + 110
                    cv2.putText(display, "CURRENT EMOTION:", (info_x, emotion_y),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 150, 150), 2)
                    
                    emotion_text = emotion_data["emotion"].upper()
                    cv2.putText(display, emotion_text,
                               (info_x, emotion_y + 60), cv2.FONT_HERSHEY_SIMPLEX, 2.5, color, 4)
                    
                    cv2.putText(display, f"Confidence: {emotion_data['confidence']:.0%}",
                               (info_x, emotion_y + 110), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    
                    # Metrics section
                    metrics_y = emotion_y + 160
                    cv2.putText(display, "FACIAL METRICS:", (info_x, metrics_y),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (150, 150, 150), 2)
                    
                    metrics_start_y = metrics_y + 30
                    for i, (key, value) in enumerate(emotion_data["metrics"].items()):
                        text = f"{key.replace('_', ' ').title()}: {value:.2f}"
                        cv2.putText(display, text, (info_x, metrics_start_y + i * 25),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    
                    # Debug mode - show all emotion scores
                    if debug_mode and "scores" in emotion_data:
                        debug_y = metrics_start_y + 120
                        cv2.putText(display, "DEBUG - ALL SCORES:",
                                   (info_x, debug_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
                        
                        debug_start_y = debug_y + 30
                        for i, (emotion, score) in enumerate(sorted(emotion_data["scores"].items(), 
                                                        key=lambda x: x[1], reverse=True)):
                            score_text = f"{emotion}: {score:.2f}"
                            score_color = colors.get(emotion, (255, 255, 255))
                            cv2.putText(display, score_text, (info_x, debug_start_y + i * 22),
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, score_color, 1)
                    
                    # Print emotion changes
                    if frame_count % 30 == 0:
                        print(f"Frame {frame_count}: {emotion_data['emotion']} "
                              f"({emotion_data['confidence']:.0%})")
                        if debug_mode and "scores" in emotion_data:
                            print(f"  Scores: {emotion_data['scores']}")
                    
                    break  # Only process first face
            else:
                # No face detected
                cv2.putText(display, "STATUS:", (info_x, info_y),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (150, 150, 150), 2)
                cv2.putText(display, "No face detected", (info_x, info_y + 50),
                           cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
            
            # FPS display (bottom left)
            fps_text = f"FPS: {int(30 / ((datetime.now() - fps_start_time).total_seconds() + 0.001))}"
            cv2.putText(display, fps_text, (info_x, display_h - 100),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
            
            # Bottom instructions
            instructions_y = display_h - 60
            cv2.rectangle(display, (0, instructions_y - 10), (display_w, display_h), (30, 30, 30), -1)
            
            cv2.putText(display, "Controls: 'Q' Quit  |  'S' Snapshot  |  'D' Debug Mode",
                       (30, instructions_y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
            
            if debug_mode:
                cv2.putText(display, "[DEBUG MODE: ON]", (30, instructions_y + 38),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
            
            cv2.imshow('Real-time Emotion Detection', display)
            
            # Handle keys
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s') and result.face_landmarks:
                filename = f"emotion_snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(filename, camera_frame)
                print(f"📸 Snapshot saved: {filename}")
            elif key == ord('d'):
                debug_mode = not debug_mode
                print(f"🔍 Debug mode: {'ON' if debug_mode else 'OFF'}")
        
        cap.release()
        cv2.destroyAllWindows()
        
        # Summary
        print("\n" + "="*50)
        print("SESSION SUMMARY")
        print("="*50)
        if emotion_history:
            print(f"Total frames: {frame_count}")
            print("\nEmotion distribution:")
            for emotion in ["Happy", "Sad", "Surprised", "Angry", "Disgusted", "Sleepy", "Neutral"]:
                count = emotion_history.count(emotion)
                if count > 0:
                    pct = (count / len(emotion_history)) * 100
                    bar = "█" * int(pct / 2)
                    print(f"  {emotion:10s}: {bar} {pct:.1f}%")
        print("="*50)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Real-time facial emotion detection (FAST - no LLM needed!)'
    )
    args = parser.parse_args()
    
    detector = EmotionDetector()
    detector.run()


if __name__ == "__main__":
    main()
