import cv2
import numpy as np
from collections import deque
import math

class AdvancedShapeDetector:
    def __init__(self):
        self.shape_colors = {
            'triangle': (0, 255, 255), 'square': (0, 255, 0), 'rectangle': (255, 0, 0),
            'pentagon': (255, 255, 0), 'hexagon': (255, 0, 255), 'circle': (0, 0, 255),
            'ellipse': (128, 0, 128), 'star': (0, 165, 255), 'arrow': (255, 128, 0),
            'cross': (128, 255, 128), 'heart': (180, 105, 255), 'trapezoid': (200, 200, 0),
            'parallelogram': (100, 149, 237), 'rhombus': (255, 20, 147), 'unknown': (128, 128, 128)
        }
        self.trajectory_history = {}
        self.shape_persistence = {}
        self.frame_count = 0
        self.prev_gray = None
        
    def calculate_hu_moments(self, contour):
        """Calculate Hu moments for shape matching"""
        moments = cv2.moments(contour)
        hu_moments = cv2.HuMoments(moments).flatten()
        return -np.sign(hu_moments) * np.log10(np.abs(hu_moments) + 1e-10)
    
    def calculate_shape_features(self, contour):
        """Extract comprehensive shape features"""
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        
        if area < 100 or perimeter == 0:
            return None
        
        # Basic geometry
        hull = cv2.convexHull(contour)
        hull_area = cv2.contourArea(hull)
        solidity = area / hull_area if hull_area > 0 else 0
        
        # Circularity and compactness
        circularity = 4 * np.pi * area / (perimeter * perimeter)
        
        # Bounding shapes
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w) / h if h > 0 else 0
        extent = area / (w * h) if (w * h) > 0 else 0
        
        # Fit ellipse and get eccentricity
        if len(contour) >= 5:
            ellipse = cv2.fitEllipse(contour)
            major_axis = max(ellipse[1])
            minor_axis = min(ellipse[1])
            eccentricity = np.sqrt(1 - (minor_axis / major_axis) ** 2) if major_axis > 0 else 0
        else:
            ellipse = None
            eccentricity = 0
        
        # Convexity defects
        defects_count = 0
        if len(contour) > 3:
            hull_indices = cv2.convexHull(contour, returnPoints=False)
            if len(hull_indices) > 3:
                try:
                    defects = cv2.convexityDefects(contour, hull_indices)
                    if defects is not None:
                        defects_count = len(defects)
                except:
                    pass
        
        return {
            'area': area, 'perimeter': perimeter, 'solidity': solidity,
            'circularity': circularity, 'aspect_ratio': aspect_ratio,
            'extent': extent, 'eccentricity': eccentricity,
            'defects_count': defects_count, 'ellipse': ellipse,
            'bbox': (x, y, w, h), 'hull': hull
        }
    
    def detect_advanced_shape(self, contour, features):
        """Advanced shape detection with multiple algorithms"""
        if features is None:
            return None, None, 0, 0
        
        peri = features['perimeter']
        approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
        vertices = len(approx)
        
        area = features['area']
        circularity = features['circularity']
        solidity = features['solidity']
        aspect_ratio = features['aspect_ratio']
        extent = features['extent']
        defects_count = features['defects_count']
        
        # Calculate moments and center
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
        
        shape = "unknown"
        confidence = 0
        
        # Enhanced shape detection with confidence scoring
        if vertices == 3:
            shape = "triangle"
            confidence = self.classify_triangle(approx, aspect_ratio)
            
        elif vertices == 4:
            shape, confidence = self.classify_quadrilateral(approx, aspect_ratio, extent)
            
        elif vertices == 5:
            shape = "pentagon"
            confidence = 90 if 0.8 < solidity < 1.0 else 70
            
        elif vertices == 6:
            shape = "hexagon"
            confidence = 90 if 0.8 < solidity < 1.0 else 70
            
        elif vertices > 10:
            if circularity > 0.85:
                shape = "circle"
                confidence = int(circularity * 100)
            elif circularity > 0.7:
                shape = "ellipse"
                confidence = int(circularity * 90)
            else:
                shape = f"curved-{vertices}"
                confidence = 60
                
        elif 7 <= vertices <= 10:
            if defects_count > 5 and solidity < 0.7:
                shape = "star"
                confidence = int((1 - solidity) * 100)
            elif self.detect_heart(contour, features):
                shape = "heart"
                confidence = 75
            elif self.detect_cross(contour, features):
                shape = "cross"
                confidence = 75
            elif self.detect_arrow(contour, features):
                shape = "arrow"
                confidence = 75
            else:
                shape = f"{vertices}-gon"
                confidence = 65
        
        # Calculate rotation angle
        if features['ellipse']:
            angle = features['ellipse'][2]
        else:
            angle = 0
        
        return shape, (cX, cY), angle, confidence
    
    def classify_triangle(self, approx, aspect_ratio):
        """Classify triangle type"""
        # Calculate side lengths
        sides = []
        for i in range(3):
            p1 = approx[i][0]
            p2 = approx[(i + 1) % 3][0]
            dist = np.linalg.norm(p1 - p2)
            sides.append(dist)
        
        sides.sort()
        # Check if equilateral, isosceles, or scalene
        if abs(sides[0] - sides[2]) < 10:
            return 95  # Equilateral
        elif abs(sides[0] - sides[1]) < 10 or abs(sides[1] - sides[2]) < 10:
            return 85  # Isosceles
        return 75  # Scalene
    
    def classify_quadrilateral(self, approx, aspect_ratio, extent):
        """Classify quadrilateral shapes"""
        # Calculate angles
        angles = []
        for i in range(4):
            p1 = approx[i][0]
            p2 = approx[(i + 1) % 4][0]
            p3 = approx[(i + 2) % 4][0]
            
            v1 = p1 - p2
            v2 = p3 - p2
            angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-10))
            angles.append(np.degrees(angle))
        
        right_angles = sum(1 for a in angles if 85 <= a <= 95)
        
        if right_angles == 4:
            if 0.95 <= aspect_ratio <= 1.05:
                return "square", 95
            else:
                return "rectangle", 90
        elif right_angles == 0:
            if 0.95 <= aspect_ratio <= 1.05:
                return "rhombus", 85
            else:
                return "parallelogram", 80
        elif right_angles == 2:
            return "trapezoid", 75
        
        return "quadrilateral", 70
    
    def detect_heart(self, contour, features):
        """Detect heart shape"""
        if features['solidity'] < 0.6 or features['aspect_ratio'] > 1.3:
            return False
        
        # Heart has specific convexity defects pattern
        hull_indices = cv2.convexHull(contour, returnPoints=False)
        if len(hull_indices) > 3:
            try:
                defects = cv2.convexityDefects(contour, hull_indices)
                if defects is not None and len(defects) >= 1:
                    # Check for deep defect at top
                    max_defect = max(defects, key=lambda x: x[0][3])
                    if max_defect[0][3] > 5000:
                        return True
            except:
                pass
        return False
    
    def detect_cross(self, contour, features):
        """Detect cross/plus shape"""
        if not (0.6 < features['solidity'] < 0.8):
            return False
        
        if not (0.8 <= features['aspect_ratio'] <= 1.2):
            return False
        
        return features['defects_count'] >= 4
    
    def detect_arrow(self, contour, features):
        """Detect arrow shape"""
        if features['solidity'] > 0.85:
            return False
        
        # Arrows typically have 2-3 major defects
        if 2 <= features['defects_count'] <= 4:
            return True
        return False
    
    def track_shape_motion(self, shape_id, center):
        """Track shape movement and calculate velocity"""
        if shape_id not in self.trajectory_history:
            self.trajectory_history[shape_id] = deque(maxlen=30)
        
        self.trajectory_history[shape_id].append(center)
        
        # Calculate velocity
        if len(self.trajectory_history[shape_id]) > 1:
            prev = self.trajectory_history[shape_id][-2]
            curr = self.trajectory_history[shape_id][-1]
            velocity = math.sqrt((curr[0] - prev[0])**2 + (curr[1] - prev[1])**2)
            direction = math.degrees(math.atan2(curr[1] - prev[1], curr[0] - prev[0]))
            return velocity, direction
        
        return 0, 0
    
    def draw_advanced_visualization(self, frame, contour, shape, center, angle, confidence, features, shape_id):
        """Advanced visualization with multiple overlays"""
        if shape is None:
            return
        
        color = self.shape_colors.get(shape, (128, 128, 128))
        
        # Draw filled contour with transparency
        overlay = frame.copy()
        cv2.drawContours(overlay, [contour], -1, color, -1)
        cv2.addWeighted(overlay, 0.2, frame, 0.8, 0, frame)
        
        # Draw contour outline
        cv2.drawContours(frame, [contour], -1, color, 3)
        
        # Draw convex hull
        hull = features['hull']
        cv2.drawContours(frame, [hull], -1, (255, 255, 255), 1)
        
        # Draw bounding box
        x, y, w, h = features['bbox']
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 1)
        
        # Draw minimum enclosing circle
        (cx, cy), radius = cv2.minEnclosingCircle(contour)
        cv2.circle(frame, (int(cx), int(cy)), int(radius), (255, 0, 255), 1)
        
        # Draw fitted ellipse
        if features['ellipse']:
            cv2.ellipse(frame, features['ellipse'], (0, 255, 255), 1)
        
        # Draw center and orientation
        cv2.circle(frame, center, 7, (255, 255, 255), -1)
        cv2.circle(frame, center, 5, color, -1)
        
        # Draw orientation line
        if angle != 0:
            length = 50
            end_x = int(center[0] + length * np.cos(np.radians(angle)))
            end_y = int(center[1] + length * np.sin(np.radians(angle)))
            cv2.arrowedLine(frame, center, (end_x, end_y), (255, 255, 0), 2)
        
        # Draw trajectory
        if shape_id in self.trajectory_history:
            points = list(self.trajectory_history[shape_id])
            for i in range(1, len(points)):
                cv2.line(frame, points[i-1], points[i], color, 2)
        
        # Calculate velocity
        velocity, direction = self.track_shape_motion(shape_id, center)
        
        # Draw information panel
        panel_x, panel_y = x, y - 10
        info_lines = [
            f"{shape.upper()} ({confidence}%)",
            f"Area: {int(features['area'])}",
            f"Perim: {int(features['perimeter'])}",
            f"Circ: {features['circularity']:.2f}",
            f"Sol: {features['solidity']:.2f}",
            f"Ang: {int(angle)}°",
            f"Vel: {velocity:.1f}px/f",
            f"Dir: {int(direction)}°"
        ]
        
        # Draw semi-transparent background for text
        for i, line in enumerate(info_lines):
            y_pos = panel_y - (len(info_lines) - i) * 20
            (text_w, text_h), _ = cv2.getTextSize(line, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 1)
            cv2.rectangle(frame, (panel_x - 5, y_pos - text_h - 5),
                         (panel_x + text_w + 5, y_pos + 5), (0, 0, 0), -1)
            cv2.putText(frame, line, (panel_x, y_pos),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
    
    def apply_background_subtraction(self, frame, method='MOG2'):
        """Advanced background subtraction"""
        if not hasattr(self, 'bg_subtractor'):
            if method == 'MOG2':
                self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
            else:
                self.bg_subtractor = cv2.createBackgroundSubtractorKNN(detectShadows=True)
        
        fg_mask = self.bg_subtractor.apply(frame)
        return fg_mask


def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    detector = AdvancedShapeDetector()
    
    # Create control windows
    cv2.namedWindow('Controls')
    cv2.createTrackbar('Min Area', 'Controls', 100, 5000, lambda x: None)
    cv2.createTrackbar('Epsilon', 'Controls', 4, 10, lambda x: None)
    cv2.createTrackbar('Blur', 'Controls', 5, 25, lambda x: None)
    cv2.createTrackbar('Thresh', 'Controls', 127, 255, lambda x: None)
    cv2.createTrackbar('Canny Low', 'Controls', 50, 255, lambda x: None)
    cv2.createTrackbar('Canny High', 'Controls', 150, 255, lambda x: None)
    cv2.createTrackbar('Morph', 'Controls', 2, 10, lambda x: None)
    cv2.createTrackbar('Method', 'Controls', 0, 4, lambda x: None)
    
    print("\n" + "="*60)
    print("ADVANCED SHAPE DETECTION SYSTEM")
    print("="*60)
    print("\nKEYBOARD CONTROLS:")
    print("  SPACE    - Exit program")
    print("  't'      - Simple threshold")
    print("  'a'      - Adaptive threshold")
    print("  'c'      - Canny edge detection")
    print("  'b'      - Background subtraction")
    print("  'o'      - Otsu's threshold")
    print("  's'      - Save screenshot")
    print("  'r'      - Reset trajectory history")
    print("\nFEATURES:")
    print("  • Multi-algorithm shape detection")
    print("  • Motion tracking & velocity calculation")
    print("  • Confidence scoring")
    print("  • Real-time trajectory visualization")
    print("  • Advanced geometric analysis")
    print("="*60 + "\n")
    
    method = 't'
    frame_count = 0
    fps_history = deque(maxlen=30)
    
    while True:
        start_time = cv2.getTickCount()
        ret, frame = cap.read()
        
        if not ret:
            break
        
        flipped = cv2.flip(frame, 1)
        
        # Get parameters
        min_area = cv2.getTrackbarPos('Min Area', 'Controls')
        epsilon_factor = cv2.getTrackbarPos('Epsilon', 'Controls') / 100.0
        blur_size = cv2.getTrackbarPos('Blur', 'Controls')
        thresh_val = cv2.getTrackbarPos('Thresh', 'Controls')
        canny_low = cv2.getTrackbarPos('Canny Low', 'Controls')
        canny_high = cv2.getTrackbarPos('Canny High', 'Controls')
        morph_size = cv2.getTrackbarPos('Morph', 'Controls')
        method_val = cv2.getTrackbarPos('Method', 'Controls')
        
        blur_size = blur_size if blur_size % 2 == 1 else blur_size + 1
        blur_size = max(1, blur_size)
        
        # Preprocessing
        gray = cv2.cvtColor(flipped, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (blur_size, blur_size), 0)
        
        # Apply selected method
        if method_val == 0 or method == 't':
            _, thresh = cv2.threshold(blurred, thresh_val, 255, cv2.THRESH_BINARY)
        elif method_val == 1 or method == 'a':
            thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 11, 2)
        elif method_val == 2 or method == 'c':
            thresh = cv2.Canny(blurred, canny_low, canny_high)
        elif method_val == 3 or method == 'b':
            thresh = detector.apply_background_subtraction(flipped)
        else:  # Otsu
            _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Morphological operations
        if morph_size > 0:
            kernel = np.ones((morph_size, morph_size), np.uint8)
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filter and process contours
        shape_stats = {}
        valid_shapes = []
        
        for idx, contour in enumerate(contours):
            features = detector.calculate_shape_features(contour)
            
            if features and features['area'] >= min_area:
                shape, center, angle, confidence = detector.detect_advanced_shape(contour, features)
                
                if shape:
                    shape_id = f"{shape}_{idx}"
                    detector.draw_advanced_visualization(flipped, contour, shape, center,
                                                       angle, confidence, features, shape_id)
                    
                    shape_stats[shape] = shape_stats.get(shape, 0) + 1
                    valid_shapes.append((shape, confidence))
        
        # Draw HUD
        hud_x, hud_y = 10, 30
        cv2.rectangle(flipped, (5, 5), (350, 250), (0, 0, 0), -1)
        cv2.rectangle(flipped, (5, 5), (350, 250), (0, 255, 0), 2)
        
        # Calculate FPS
        end_time = cv2.getTickCount()
        fps = cv2.getTickFrequency() / (end_time - start_time)
        fps_history.append(fps)
        avg_fps = np.mean(fps_history)
        
        hud_info = [
            f"FPS: {avg_fps:.1f}",
            f"Frame: {frame_count}",
            f"Shapes: {len(valid_shapes)}",
            f"Method: {['Thresh', 'Adaptive', 'Canny', 'BG-Sub', 'Otsu'][method_val]}",
            "",
            "Shape Statistics:"
        ]
        
        for line in hud_info:
            cv2.putText(flipped, line, (hud_x, hud_y), cv2.FONT_HERSHEY_SIMPLEX,
                       0.5, (0, 255, 0), 1)
            hud_y += 20
        
        # Display shape counts
        for shape, count in sorted(shape_stats.items()):
            color = detector.shape_colors.get(shape, (255, 255, 255))
            cv2.putText(flipped, f"  {shape}: {count}", (hud_x, hud_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            hud_y += 20
        
        # Show windows
        cv2.imshow('Advanced Shape Detection', flipped)
        cv2.imshow('Processed', thresh)
        
        # Keyboard handling
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):
            break
        elif key == ord('t'):
            cv2.setTrackbarPos('Method', 'Controls', 0)
            method = 't'
        elif key == ord('a'):
            cv2.setTrackbarPos('Method', 'Controls', 1)
            method = 'a'
        elif key == ord('c'):
            cv2.setTrackbarPos('Method', 'Controls', 2)
            method = 'c'
        elif key == ord('b'):
            cv2.setTrackbarPos('Method', 'Controls', 3)
            method = 'b'
        elif key == ord('o'):
            cv2.setTrackbarPos('Method', 'Controls', 4)
            method = 'o'
        elif key == ord('s'):
            cv2.imwrite(f'shape_detection_{frame_count}.png', flipped)
            print(f"Screenshot saved: shape_detection_{frame_count}.png")
        elif key == ord('r'):
            detector.trajectory_history.clear()
            print("Trajectory history reset")
        
        frame_count += 1
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()