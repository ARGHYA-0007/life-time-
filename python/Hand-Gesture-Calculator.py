import cv2
import time
import math
import mediapipe as mp

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils
hand = mphands.Hands()

last_click_time = 0
click_delay = 1.0
expression = ""

while True:
    ret, frame = cap.read()
    flipped_frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB)

    cv2.rectangle(flipped_frame, (10, 10), (320, 75), (255, 255, 255), cv2.FILLED)
    cv2.putText(flipped_frame, expression, (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    result = hand.process(rgb_frame)

    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(flipped_frame, handlms, mphands.HAND_CONNECTIONS)
            h, w, _ = flipped_frame.shape
            thumbtip = handlms.landmark[4]
            indextip = handlms.landmark[8]
            x1, y1 = int(thumbtip.x * w), int(thumbtip.y * h)
            x2, y2 = int(indextip.x * w), int(indextip.y * h)
            length = math.hypot(x2 - x1, y2 - y1)

            # Get current time
            current_time = time.time()

            # Only detect click if enough time has passed since last click
            if length < 40 and (current_time - last_click_time) > click_delay:
                if 10 < x2 < 70 and 235 < y2 < 295:
                    expression += "1"
                    last_click_time = current_time
                elif 90 < x2 < 150 and 235 < y2 < 295:
                    expression += "2"
                    last_click_time = current_time
                elif 170 < x2 < 230 and 235 < y2 < 295:
                    expression += "3"
                    last_click_time = current_time
                elif 10 < x2 < 70 and 160 < y2 < 220:
                    expression += "4"
                    last_click_time = current_time
                elif 90 < x2 < 150 and 160 < y2 < 220:
                    expression += "5"
                    last_click_time = current_time
                elif 170 < x2 < 230 and 160 < y2 < 220:
                    expression += "6"
                    last_click_time = current_time
                elif 10 < x2 < 70 and 85 < y2 < 145:
                    expression += "7"
                    last_click_time = current_time
                elif 90 < x2 < 150 and 85 < y2 < 145:
                    expression += "8"
                    last_click_time = current_time
                elif 170 < x2 < 230 and 85 < y2 < 145:
                    expression += "9"
                    last_click_time = current_time
                elif 90 < x2 < 150 and 310 < y2 < 370:
                    expression += "0"
                    last_click_time = current_time
                elif 250 < x2 < 310 and 85 < y2 < 145:
                    expression += "+"
                    last_click_time = current_time
                elif 250 < x2 < 310 and 160 < y2 < 220:
                    expression += "-"
                    last_click_time = current_time
                elif 250 < x2 < 310 and 235 < y2 < 295:
                    expression += "*"
                    last_click_time = current_time
                elif 250 < x2 < 310 and 310 < y2 < 370:
                    expression += "/"
                    last_click_time = current_time
                elif 10 < x2 < 70 and 310 < y2 < 370:
                    expression = ""  # Clear
                    last_click_time = current_time
                elif 170 < x2 < 230 and 310 < y2 < 370:
                    try:
                        expression = str(eval(expression))  # Calculate
                    except:
                        expression = "Error"
                    last_click_time = current_time

    # Draw calculator buttons
    cv2.rectangle(flipped_frame, (10, 85), (70, 145), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "7", (30, 125), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (90, 85), (150, 145), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "8", (110, 125), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (170, 85), (230, 145), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "9", (190, 125), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (250, 85), (310, 145), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "+", (265, 125), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (10, 160), (70, 220), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "4", (30, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (90, 160), (150, 220), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "5", (110, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (170, 160), (230, 220), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "6", (190, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (250, 160), (310, 220), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "-", (270, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (10, 235), (70, 295), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "1", (30, 275), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (90, 235), (150, 295), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "2", (110, 275), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (170, 235), (230, 295), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "3", (190, 275), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (250, 235), (310, 295), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "*", (268, 275), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (10, 310), (70, 370), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "C", (25, 350), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (90, 310), (150, 370), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "0", (110, 350), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (170, 310), (230, 370), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "=", (185, 350), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
    cv2.rectangle(flipped_frame, (250, 310), (310, 370), (0, 0, 0), 5)
    cv2.putText(flipped_frame, "/", (270, 350), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)

    if not ret:
        break
    cv2.imshow("frame", flipped_frame)
    if cv2.waitKey(1) & 0xFF == ord(" "):
        break

cap.release()
cv2.destroyAllWindows()