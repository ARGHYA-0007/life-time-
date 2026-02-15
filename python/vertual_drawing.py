import cv2
import mediapipe as mp
import time
import numpy as np
cap=cv2.VideoCapture(0)
mphands=mp.solutions.hands
mpdraw=mp.solutions.drawing_utils
hand=mphands.Hands(min_detection_confidence=0.85,min_tracking_confidence=0.85)
cap.set(3,1280)
cap.set(4,720)
tipids=[4,8,12,16,20]
i=0
drawcolor=(0, 0, 0)
thickness=15
xp,yp=0,0
imagecanvas = np.ones((720, 1280, 3), np.uint8) * 255
erasarthickness=200
img1=cv2.imread(r"C:\Users\arghy\OneDrive\Desktop\program\1cb.jpg")
img2=cv2.imread(r"C:\Users\arghy\OneDrive\Desktop\program\2cb.jpg")
img3=cv2.imread(r"C:\Users\arghy\OneDrive\Desktop\program\3cb.jpg")
img4=cv2.imread(r"C:\Users\arghy\OneDrive\Desktop\program\4cb.jpg")
img1 = cv2.resize(img1, (1280, 125))
img2 = cv2.resize(img2, (1280, 125))
img3 = cv2.resize(img3, (1280, 125))
img4 = cv2.resize(img4, (1280, 125))
img=[img1,img2,img3,img4]
while True:
    ret,frame=cap.read()
    flipped_frame=cv2.flip(frame,1)
    rgb=cv2.cvtColor(flipped_frame,cv2.COLOR_BGR2RGB)


    h,w,_=flipped_frame.shape
    result=hand.process(rgb)

    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(flipped_frame,handlms,mphands.HAND_CONNECTIONS)
        x1,y1=int(handlms.landmark[8].x*w),int(handlms.landmark[8].y*h)
        x2,y2=int(handlms.landmark[12].x*w),int(handlms.landmark[12].y*h)
        finger=[]
        if handlms.landmark[4].x<handlms.landmark[2].x:
            finger.append(1)
        else:
            finger.append(0)
        for id in range(1,5):

            if handlms.landmark[tipids[id]].y<handlms.landmark[tipids[id]-2].y:
                finger.append(1)
            else:
                finger.append(0)
        if finger[1] and finger[2]:
            print("selection mode")
            xp,yp=x1,y1
            if y1<125:
                if 0<x1<320:
                    i=0
                    drawcolor=(0,0,0)
                elif 320<x1<640:
                    i=1
                    drawcolor=(255, 0, 0)
                elif 640<x1<960:
                    i=2
                    drawcolor=(0, 0, 255)
                elif 960<x1<1280:
                    i=3
                    drawcolor=(255, 255, 255)
            cv2.rectangle(flipped_frame,(x1-25,y1),(x2+25,y2),drawcolor,cv2.FILLED)
        elif finger[1] == False :
            xp,yp=x1,y1
        if finger[1] and not finger[2]:
            if xp==0 and yp==0:
                xp,yp=x1,y1
            if drawcolor==(255,255,255):
                cv2.line(flipped_frame,(xp,yp),(x1,y1),drawcolor,erasarthickness)
                cv2.line(imagecanvas,(xp,yp),(x1,y1),drawcolor,erasarthickness)
            else:
                cv2.line(flipped_frame,(xp,yp),(x1,y1),drawcolor,thickness)
                cv2.line(imagecanvas,(xp,yp),(x1,y1),drawcolor,thickness)
            print("drawing mode")
            cv2.circle(flipped_frame,(x1,y1),10,drawcolor,cv2.FILLED)

            xp,yp=x1,y1
    imggray = cv2.cvtColor(imagecanvas, cv2.COLOR_BGR2GRAY)
    _, imginv = cv2.threshold(imggray, 250, 255, cv2.THRESH_BINARY_INV) # Changed to INV and 250 if pixel<250->white pixel>250->black
    imginv = cv2.cvtColor(imginv, cv2.COLOR_GRAY2BGR)

    flipped_frame = cv2.bitwise_and(flipped_frame, cv2.bitwise_not(imginv))# here all color will show black
    flipped_frame = cv2.bitwise_or(flipped_frame, cv2.bitwise_and(imagecanvas, imginv))# now all brush will get their color
    # flipped_frame=cv2.bitwise_and(flipped_frame,imginv)
    # flipped_frame=cv2.bitwise_or(flipped_frame,imagecanvas)
    if not ret:
        break
    flipped_frame[0:125,0:1280]=img[i]
    cv2.imshow("frame", flipped_frame)
    # cv2.imshow("imagecanvas", imagecanvas)
    if cv2.waitKey(1) & 0xFF==ord(" "):
        break
cap.release()
cv2.destroyAllWindows()