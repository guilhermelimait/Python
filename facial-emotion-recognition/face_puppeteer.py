"""
Face Puppeteer - Control a photo with your face movements
Uses MediaPipe to map your facial movements to an imported image
"""

import importlib
import subprocess
import sys
from datetime import datetime
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

class FacePuppeteer:
    def __init__(self):
        """Initialize the face puppeteer."""
        # Initialize MediaPipe Face Landmarker
        base_options = mp.tasks.BaseOptions(
            model_asset_path='face_landmarker.task'
        )
        options = mp.tasks.vision.FaceLandmarkerOptions(
            base_options=base_options,
            running_mode=mp.tasks.vision.RunningMode.VIDEO,
            num_faces=1
        )
        self.detector = mp.tasks.vision.FaceLandmarker.create_from_options(options)
        
        # Target image and landmarks
        self.target_image = None
        self.target_landmarks = None
        self.target_face_rect = None
        
        # Mouse tracking
        self.mouse_x = 0
        self.mouse_y = 0
        
    def load_target_image(self, image_path):
        """Load and detect face in target image."""
        if not os.path.exists(image_path):
            print(f"❌ Image not found: {image_path}")
            return False
        
        self.target_image = cv2.imread(image_path)
        if self.target_image is None:
            print(f"❌ Could not load image: {image_path}")
            return False
        
        print(f"✓ Loaded image: {image_path}")
        print(f"  Resolution: {self.target_image.shape[1]}x{self.target_image.shape[0]}")
        
        # Detect face in target image
        rgb_image = cv2.cvtColor(self.target_image, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)
        
        # Use image mode for static image
        base_options = mp.tasks.BaseOptions(model_asset_path='face_landmarker.task')
        options = mp.tasks.vision.FaceLandmarkerOptions(
            base_options=base_options,
            running_mode=mp.tasks.vision.RunningMode.IMAGE,
            num_faces=1
        )
        image_detector = mp.tasks.vision.FaceLandmarker.create_from_options(options)
        result = image_detector.detect(mp_image)
        
        if not result.face_landmarks:
            print("❌ No face detected in target image")
            return False
        
        self.target_landmarks = result.face_landmarks[0]
        print(f"✓ Detected {len(self.target_landmarks)} facial landmarks in target image")
        
        # Calculate face bounding box
        h, w = self.target_image.shape[:2]
        x_coords = [int(lm.x * w) for lm in self.target_landmarks]
        y_coords = [int(lm.y * h) for lm in self.target_landmarks]
        self.target_face_rect = (min(x_coords), min(y_coords), 
                                  max(x_coords), max(y_coords))
        
        return True
    
    def get_delaunay_triangles(self, points, w, h):
        """Get Delaunay triangulation for points."""
        rect = (0, 0, w, h)
        subdiv = cv2.Subdiv2D(rect)
        
        for p in points:
            if 0 <= p[0] < w and 0 <= p[1] < h:
                subdiv.insert((float(p[0]), float(p[1])))
        
        triangles = []
        for t in subdiv.getTriangleList():
            pt1 = (t[0], t[1])
            pt2 = (t[2], t[3])
            pt3 = (t[4], t[5])
            
            if self.rect_contains(rect, pt1) and self.rect_contains(rect, pt2) and self.rect_contains(rect, pt3):
                ind = []
                for pt in [pt1, pt2, pt3]:
                    for i, p in enumerate(points):
                        if abs(pt[0] - p[0]) < 1.0 and abs(pt[1] - p[1]) < 1.0:
                            ind.append(i)
                            break
                if len(ind) == 3:
                    triangles.append(ind)
        
        return triangles
    
    def rect_contains(self, rect, point):
        """Check if point is inside rectangle."""
        return rect[0] <= point[0] < rect[0] + rect[2] and rect[1] <= point[1] < rect[1] + rect[3]
    
    def warp_triangle(self, img1, img2, t1, t2):
        """Warp triangle from img1 to img2 (optimized)."""
        try:
            r1 = cv2.boundingRect(np.float32([t1]))
            r2 = cv2.boundingRect(np.float32([t2]))
            
            # Skip invalid rectangles
            if r1[2] <= 0 or r1[3] <= 0 or r2[2] <= 0 or r2[3] <= 0:
                return
            
            # Check bounds
            if (r1[0] < 0 or r1[1] < 0 or r1[0]+r1[2] > img1.shape[1] or r1[1]+r1[3] > img1.shape[0] or
                r2[0] < 0 or r2[1] < 0 or r2[0]+r2[2] > img2.shape[1] or r2[1]+r2[3] > img2.shape[0]):
                return
            
            t1_rect = []
            t2_rect = []
            
            for i in range(3):
                t1_rect.append(((t1[i][0] - r1[0]), (t1[i][1] - r1[1])))
                t2_rect.append(((t2[i][0] - r2[0]), (t2[i][1] - r2[1])))
            
            # Get mask
            mask = np.zeros((r2[3], r2[2], 3), dtype=np.float32)
            cv2.fillConvexPoly(mask, np.int32(t2_rect), (1.0, 1.0, 1.0), 16, 0)
            
            # Get image rect
            img1_rect = img1[r1[1]:r1[1] + r1[3], r1[0]:r1[0] + r1[2]]
            
            if img1_rect.shape[0] == 0 or img1_rect.shape[1] == 0:
                return
            
            # Warp
            warp_mat = cv2.getAffineTransform(np.float32(t1_rect), np.float32(t2_rect))
            img2_rect = cv2.warpAffine(img1_rect, warp_mat, (r2[2], r2[3]), 
                                       None, cv2.INTER_LINEAR, cv2.BORDER_REFLECT_101)
            
            # Apply mask and blend
            img2_rect = img2_rect * mask
            img2[r2[1]:r2[1]+r2[3], r2[0]:r2[0]+r2[2]] = \
                img2[r2[1]:r2[1]+r2[3], r2[0]:r2[0]+r2[2]] * ((1.0, 1.0, 1.0) - mask) + img2_rect
        except Exception as e:
            # Silently skip problematic triangles
            pass
    
    def apply_facial_expression(self, source_landmarks, target_image, target_landmarks):
        """Apply source facial expression to target image using fast simplified warping.
        Maps key facial landmarks from source (your camera) to target (image face).
        """
        h, w = target_image.shape[:2]
        
        # Resize for faster processing (max 800px width)
        max_width = 800
        if w > max_width:
            scale = max_width / w
            new_w, new_h = int(w * scale), int(h * scale)
            target_resized = cv2.resize(target_image, (new_w, new_h))
        else:
            scale = 1.0
            new_w, new_h = w, h
            target_resized = target_image.copy()
        
        # Use minimal key facial landmarks for maximum speed
        # Face contour, eyes, nose, mouth
        key_indices = [
            # Face outline (fewer points)
            10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288,
            152, 234, 127, 162, 21, 54, 103, 67,
            # Eyes (minimal)
            33, 133, 159, 145, 362, 263, 386, 374,
            # Eyebrows (minimal)
            70, 107, 336, 296,
            # Nose
            1, 195,
            # Mouth (key points only)
            61, 291, 0, 17, 84, 314,
            78, 308, 13, 14
        ]
        
        # Convert to pixel coordinates
        target_points = []
        warped_points = []
        
        # Calculate face centers and scales
        target_x = [target_landmarks[i].x for i in key_indices]
        target_y = [target_landmarks[i].y for i in key_indices]
        target_center_x = sum(target_x) / len(target_x)
        target_center_y = sum(target_y) / len(target_y)
        target_scale_x = max(target_x) - min(target_x)
        target_scale_y = max(target_y) - min(target_y)
        
        source_x = [source_landmarks[i].x for i in key_indices]
        source_y = [source_landmarks[i].y for i in key_indices]
        source_center_x = sum(source_x) / len(source_x)
        source_center_y = sum(source_y) / len(source_y)
        source_scale_x = max(source_x) - min(source_x)
        source_scale_y = max(source_y) - min(source_y)
        
        # Map landmarks (scaled to processing resolution)
        for i in key_indices:
            # Target (original position)
            tx = target_landmarks[i].x * new_w
            ty = target_landmarks[i].y * new_h
            target_points.append([tx, ty])
            
            # Source mapped to target space
            norm_x = (source_landmarks[i].x - source_center_x) / source_scale_x
            norm_y = (source_landmarks[i].y - source_center_y) / source_scale_y
            wx = (norm_x * target_scale_x + target_center_x) * new_w
            wy = (norm_y * target_scale_y + target_center_y) * new_h
            warped_points.append([wx, wy])
        
        target_points = np.array(target_points, dtype=np.float32)
        warped_points = np.array(warped_points, dtype=np.float32)
        
        # Add corners
        corners = np.array([
            [0, 0], [new_w-1, 0], [0, new_h-1], [new_w-1, new_h-1],
            [new_w//2, 0], [new_w//2, new_h-1], [0, new_h//2], [new_w-1, new_h//2]
        ], dtype=np.float32)
        
        target_points = np.vstack([target_points, corners])
        warped_points = np.vstack([warped_points, corners])
        
        # Get triangulation
        triangles = self.get_delaunay_triangles(target_points, new_w, new_h)
        
        # Create output
        result = target_resized.astype(np.float32)
        
        # Warp each triangle (limit iterations for speed)
        for idx, indices in enumerate(triangles):
            if len(indices) == 3:
                try:
                    t1 = [target_points[i] for i in indices]
                    t2 = [warped_points[i] for i in indices]
                    self.warp_triangle(target_resized.astype(np.float32), result, t1, t2)
                except:
                    pass
        
        result = np.uint8(np.clip(result, 0, 255))
        
        # Upscale back if needed
        if scale != 1.0:
            result = cv2.resize(result, (w, h))
        
        return result
    
    def mouse_callback(self, event, x, y, flags, param):
        """Handle mouse events."""
        self.mouse_x = x
        self.mouse_y = y
    
    def run(self):
        """Run the face puppeteer."""
        # Ask for image path
        print("\n" + "="*60)
        print("🎭 FACE PUPPETEER - Control a Photo with Your Face")
        print("="*60)
        
        # Check for images in current directory
        image_files = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
        
        if image_files:
            print("\nAvailable images in current directory:")
            for i, img in enumerate(image_files[:10], 1):
                print(f"  {i}. {img}")
            print()
        
        image_path = input("Enter image path (or number from list): ").strip()
        
        # Check if it's a number from the list
        if image_path.isdigit() and image_files:
            idx = int(image_path) - 1
            if 0 <= idx < len(image_files):
                image_path = image_files[idx]
        
        if not self.load_target_image(image_path):
            return
        
        print("\n✓ Starting camera...")
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Could not open camera")
            return
        
        print("\nControls:")
        print("  'q' - Quit")
        print("  's' - Save snapshot")
        print("  '1' - Show original target image")
        print("  '2' - Show animated image only")
        print("  '3' - Show side-by-side (default)")
        print("="*60 + "\n")
        
        frame_count = 0
        display_mode = 3  # 1=original, 2=animated, 3=side-by-side
        last_animated = None  # Cache last animated result
        process_every = 2  # Process every N frames for speed
        fps_time = datetime.now()
        fps_counter = 0
        current_fps = 0
        
        cv2.namedWindow('Face Puppeteer')
        cv2.setMouseCallback('Face Puppeteer', self.mouse_callback)
        
        while cap.isOpened():
            success, camera_frame = cap.read()
            if not success:
                continue
            
            frame_count += 1
            fps_counter += 1
            camera_frame = cv2.flip(camera_frame, 1)
            
            # Calculate FPS
            if (datetime.now() - fps_time).total_seconds() >= 1.0:
                current_fps = fps_counter
                fps_counter = 0
                fps_time = datetime.now()
            
            # Detect face in camera
            rgb_frame = cv2.cvtColor(camera_frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            timestamp_ms = frame_count * 33
            
            result = self.detector.detect_for_video(mp_image, timestamp_ms)
            
            # Debug: Print face detection status
            if frame_count % 30 == 0:
                if result.face_landmarks:
                    print(f"Frame {frame_count}: Face detected with {len(result.face_landmarks[0])} landmarks")
                else:
                    print(f"Frame {frame_count}: No face detected in camera")
            
            # Create display
            display_w, display_h = 1280, 720
            display = np.zeros((display_h, display_w, 3), dtype=np.uint8)
            display[:] = (40, 40, 40)
            
            if result.face_landmarks and len(result.face_landmarks) > 0:
                source_landmarks = result.face_landmarks[0]
                
                # Only process warping every N frames for better performance
                if frame_count % process_every == 0:
                    # Apply facial expression warping
                    animated_image = self.apply_facial_expression(
                        source_landmarks, 
                        self.target_image.copy(), 
                        self.target_landmarks
                    )
                    last_animated = animated_image
                elif last_animated is not None:
                    animated_image = last_animated
                else:
                    animated_image = self.target_image.copy()
                
                # Resize for display
                target_h, target_w = self.target_image.shape[:2]
                scale = min(500 / target_w, 375 / target_h)
                new_w, new_h = int(target_w * scale), int(target_h * scale)
                
                target_resized = cv2.resize(self.target_image, (new_w, new_h))
                animated_image = cv2.resize(animated_image, (new_w, new_h))
                
                # Display based on mode
                if display_mode == 1:  # Original only
                    y_offset = (display_h - new_h) // 2
                    x_offset = (display_w - new_w) // 2
                    display[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = target_resized
                    
                elif display_mode == 2:  # Animated only
                    y_offset = (display_h - new_h) // 2
                    x_offset = (display_w - new_w) // 2
                    display[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = animated_image
                    
                else:  # Side by side (default)
                    # Camera on left
                    camera_resized = cv2.resize(camera_frame, (500, 375))
                    display[50:425, 50:550] = camera_resized
                    
                    # Animated image on right
                    y_offset = 50 + (375 - new_h) // 2
                    x_offset = 630 + (500 - new_w) // 2
                    display[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = animated_image
                    
                    # Labels
                    cv2.putText(display, "YOUR FACE", (200, 450),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                    cv2.putText(display, "ANIMATED IMAGE", (780, 450),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                # Status info
                cv2.putText(display, f"Camera Landmarks: {len(source_landmarks)}", (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(display, f"Target Landmarks: {len(self.target_landmarks)}", (10, 60),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(display, f"FPS: {current_fps}", (10, 90),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
                cv2.putText(display, f"Mode: {['', 'ORIGINAL', 'ANIMATED', 'SIDE-BY-SIDE'][display_mode]}", 
                           (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                cv2.putText(display, "Status: ACTIVE", (10, 150),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                
            else:
                # Show camera feed even when no face detected
                camera_resized = cv2.resize(camera_frame, (500, 375))
                display[50:425, 390:890] = camera_resized
                
                cv2.putText(display, "No face detected in camera", (display_w//2 - 250, display_h//2),
                           cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
                cv2.putText(display, "Make sure your face is visible and well-lit", (display_w//2 - 300, display_h//2 + 40),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
            
            # Instructions at bottom
            instructions_y = display_h - 50
            cv2.rectangle(display, (0, instructions_y - 10), (display_w, display_h), (30, 30, 30), -1)
            cv2.putText(display, "Controls: 'Q' Quit  |  'S' Snapshot  |  '1,2,3' Display Mode",
                       (30, instructions_y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
            
            cv2.imshow('Face Puppeteer', display)
            
            # Handle keys
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                filename = f"puppeteer_snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(filename, display)
                print(f"📸 Snapshot saved: {filename}")
            elif key == ord('1'):
                display_mode = 1
                print("Display mode: Original target image")
            elif key == ord('2'):
                display_mode = 2
                print("Display mode: Animated image only")
            elif key == ord('3'):
                display_mode = 3
                print("Display mode: Side-by-side")
        
        cap.release()
        cv2.destroyAllWindows()
        print("\n✓ Face Puppeteer closed")

if __name__ == "__main__":
    puppeteer = FacePuppeteer()
    puppeteer.run()
