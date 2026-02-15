import time
import datetime
import winsound  # Only works on Windows

alarm_time = input("Enter alarm time (HH:MM:SS, 24-hour format): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    if now == alarm_time:
        print("Wake up!")
        # Play a beep sound
        winsound.Beep(1000, 1000)  # frequency, duration in ms
        break
    time.sleep(1)