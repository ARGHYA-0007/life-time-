import cv2
import mediapipe as mp

class HandDetection:
    def __init__(self, camera_id=0):
        self.cap = cv2.VideoCapture(camera_id)

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands()
        self.mpdraw = mp.solutions.drawing_utils

    def start(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            result = self.hands.process(rgb_frame)

            if result.multi_hand_landmarks:
                for handlms in result.multi_hand_landmarks:
                    self.mpdraw.draw_landmarks(frame,handlms,self.mphands.HAND_CONNECTIONS)
                cv2.putText(frame,"Hand Detected",(10, 30),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 255),2)

            cv2.imshow("Hand Detection", frame)




            if cv2.waitKey(1) & 0xFF == ord(' '):
                break

        self.cap.release()
        cv2.destroyAllWindows()
    def middlefinger(self):
        result = self.hands.process(rgb_frame)
        if result.multi_hand_landmarks:
            for handlms in result.multi_hand_landmarks:
                self.mpdraw.draw_landmarks(frame,handlms,self.mphands.HAND_CONNECTIONS)
                if handlms.landmark[12].x>handlms.landmark[10].x:
                    cv2.putText(flipped_frame,"showing middle finger\nput that in your ass ",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)

