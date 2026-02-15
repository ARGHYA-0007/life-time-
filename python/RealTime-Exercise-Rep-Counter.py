import cv2
import mediapipe as mp
import math
import numpy as np
mppose=mp.solutions.pose
mpdraw=mp.solutions.drawing_utils
pose=mppose.Pose()
cap=cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
import math
count=0
dir=1
# Calculate angle at point 2 (elbow) formed by points 1, 2, 3
def calculate_angle(x1, y1, x2, y2, x3, y3):
    # Calculate the angle using atan2
    angle_rad = math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2)

    # Convert to degrees
    angle_deg = math.degrees(angle_rad)

    # Make sure angle is positive
    angle_deg = abs(angle_deg)

    # If angle is greater than 180, take the smaller angle
    if angle_deg > 180:
        angle_deg = 360 - angle_deg

    return angle_deg
while True:
    ret,frame=cap.read()
    flipped_frame = cv2.flip(frame, 1)
    rgb_frame=cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB)
    result=pose.process(rgb_frame)
    h,w,_=flipped_frame.shape
    if result.pose_landmarks:
        # mpdraw.draw_landmarks(flipped_frame,result.pose_landmarks)
        lm11=result.pose_landmarks.landmark[11]
        lm13=result.pose_landmarks.landmark[13]
        lm15=result.pose_landmarks.landmark[15]
        lm12=result.pose_landmarks.landmark[12]
        lm14=result.pose_landmarks.landmark[14]
        lm16=result.pose_landmarks.landmark[16]
        x1, y1 = lm11.x, lm11.y
        x2, y2 = lm13.x, lm13.y
        x3, y3 = lm15.x, lm15.y
        x4, y4 = lm12.x, lm12.y
        x5, y5 = lm14.x, lm14.y
        x6, y6 = lm16.x, lm16.y
        x1, y1 = int(x1 * w), int(y1 * h)
        x2, y2 = int(x2 * w), int(y2 * h)
        x3, y3 = int(x3 * w), int(y3 * h)
        x4, y4 = int(x4 * w), int(y4 * h)
        x5, y5 = int(x5 * w), int(y5 * h)
        x6, y6 = int(x6 * w), int(y6 * h)
        cv2.circle(flipped_frame,(x1,y1),10,(255,0,0),cv2.FILLED)
        cv2.circle(flipped_frame,(x1,y1),15,(255,0,0),5)
        cv2.circle(flipped_frame,(x2,y2),10,(255,0,0),cv2.FILLED)
        cv2.circle(flipped_frame,(x2,y2),15,(255,0,0),5)
        cv2.circle(flipped_frame,(x3,y3),10,(255,0,0),cv2.FILLED)
        cv2.circle(flipped_frame,(x3,y3),15,(255,0,0),5)
        cv2.circle(flipped_frame,(x4,y4),10,(255,0,0),cv2.FILLED)
        cv2.circle(flipped_frame,(x4,y4),15,(255,0,0),5)
        cv2.circle(flipped_frame,(x5,y5),10,(255,0,0),cv2.FILLED)
        cv2.circle(flipped_frame,(x5,y5),15,(255,0,0),5)
        cv2.circle(flipped_frame,(x6,y6),10,(255,0,0),cv2.FILLED)
        cv2.circle(flipped_frame,(x6,y6),15,(255,0,0),5)
        cv2.line(flipped_frame,(x1,y1),(x2,y2),(255,0,0),5)
        cv2.line(flipped_frame,(x3,y3),(x2,y2),(255,0,0),5)
        cv2.line(flipped_frame,(x4,y4),(x5,y5),(255,0,0),5)
        cv2.line(flipped_frame,(x6,y6),(x5,y5),(255,0,0),5)
        angle_right=calculate_angle(x1,y1,x2,y2,x3,y3)
        angle_left=calculate_angle(x4,y4,x5,y5,x6,y6)
        cv2.putText(flipped_frame,str(int(angle_right)),(x2-70,y2-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        cv2.putText(flipped_frame,str(int(angle_left)),(x5-70,y5-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        per_right=np.interp(angle_right,(30,130),(0,100))
        per_left=np.interp(angle_left,(30,130),(0,100))
        if per_left==100 and per_right==100:
            if dir==1:
                count+=0.5
                dir=0
        if per_left==0 and per_right==0:
            if dir==0:
                count+=0.5
                dir=1
        cv2.putText(flipped_frame,str(int(count)),(0,350),cv2.FONT_HERSHEY_SIMPLEX,10,(0,255,0),10)
    if not ret:
        break
    cv2.imshow("frame", flipped_frame)
    if cv2.waitKey(1) & 0xFF==ord(" "):
        break
cap.release()
cv2.destroyAllWindows()