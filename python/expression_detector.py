import cv2
import numpy as np

def anime_filter(frame):
    # 1. Downscale for speed
    small = cv2.pyrDown(frame)
    small = cv2.pyrDown(small)

    # 2. Apply multiple bilateral filters (anime smooth skin)
    for _ in range(5):
        small = cv2.bilateralFilter(small, 9, 75, 75)

    # 3. Upscale back
    smooth = cv2.pyrUp(small)
    smooth = cv2.pyrUp(smooth)

    # 4. Edge detection (anime black lines)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(edges, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY,
                                  9, 2)

    # 5. Combine smooth colors + edges
    cartoon = cv2.bitwise_and(smooth, smooth, mask=edges)

    return cartoon


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    
    anime_frame = anime_filter(frame)

    cv2.imshow("Anime Filter", anime_frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()





