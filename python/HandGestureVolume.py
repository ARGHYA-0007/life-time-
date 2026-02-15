import cv2
import mediapipe as mp
import math
import numpy as np



cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands

hands = mphands.Hands(min_detection_confidence=0.7)

mpdraw = mp.solutions.drawing_utils



from pycaw.pycaw import AudioUtilities
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
print(f"Audio output: {device.FriendlyName}")
print(f"- Muted: {bool(volume.GetMute())}")
print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB") # this decide the volume
volRange=volume.GetVolumeRange()
minvolume = volRange[0]
maxvolume = volRange[1]
minhandrange=30
maxhandrange=230
percent =0

volbar=170
while True:

    ret, frame = cap.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    flipped_frame = cv2.flip(frame, 1)

    flipped_frame_rgb = cv2.flip(frame_rgb, 1)


    result = hands.process(flipped_frame_rgb)


    if result.multi_hand_landmarks:

        for handlms in result.multi_hand_landmarks:

            mpdraw.draw_landmarks(flipped_frame, handlms, mphands.HAND_CONNECTIONS)
            cv2.putText(flipped_frame,"hand detected",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)


            h,w,s=flipped_frame.shape
            thumbtip=handlms.landmark[4]
            indextip=handlms.landmark[8]

            x1,y1=int(thumbtip.x*w),int(thumbtip.y*h)
            x2,y2=int(indextip.x*w),int(indextip.y*h)

            cx,cy=(x1+x2)//2,(y1+y2)//2

            cv2.circle(flipped_frame,(cx,cy),10,(255,2,255),-1)
            cv2.circle(flipped_frame,(x1,y1),10,(255,2,255),-1)
            cv2.circle(flipped_frame,(x2,y2),10,(255,2,255),-1)
            cv2.line(flipped_frame,(x1,y1),(x2,y2),(255,2,255),5)

            length=math.hypot(x2-x1,y2-y1) # for getting length between (x1,y1) and (x2,y2)

            # print(length)

            # handrange 25-210
            # volume range -96.0 - 0.0
            vol=np.interp(length,[minhandrange,maxhandrange],[minvolume,maxvolume])
            volbar=np.interp(length,[minhandrange,maxhandrange],[300,70])
            percent=np.interp(length,[minhandrange,maxhandrange],[0,100])
            print(percent)
            # converting length by comparing handrange and volume range
            volume.SetMasterVolumeLevel(vol,None) # this decide the volume
            # the 'vol' in this func give number between minvolume and max volume depending on the length and min,max range
            if length<50:
                cv2.circle(flipped_frame,(cx,cy),10,(255,255,255),-1)
    cv2.rectangle(flipped_frame,(50,70),(100,300),(0,255,0),5)
    cv2.rectangle(flipped_frame,(50,int(volbar)),(100,300),(0,255,0),-1)
    cv2.putText(flipped_frame,f"{str(int(percent))}%",(50,55),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)

    if not ret:
        break

    cv2.imshow("frame", flipped_frame)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()

cv2.destroyAllWindows()