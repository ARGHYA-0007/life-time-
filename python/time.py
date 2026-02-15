import time
import os
from datetime import datetime

# Cross-platform screen clear
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Consistent-width ASCII numbers and colon
ascii_digits = {
    '0': ["  ___  ",
          " / _ \\ ",
          "| | | |",
          "| |_| |",
          " \\___/ "],
    '1': ["  __   ",
          " /_ |  ",
          "  | |  ",
          "  | |  ",
          "  |_|  "],
    '2': ["  ___  ",
          " |__ \\ ",
          "    ) |",
          "   / / ",
          "  |___|"],
    '3': ["  ____ ",
          " |___ \\",
          "   __) |",
          "  |__ < ",
          "  ___) |"],
    '4': ["  _  _  ",
          " | || | ",
          " | || |_",
          " |__   _|",
          "    |_|  "],
    '5': ["  _____",
          " | ____|",
          " | |__  ",
          " |___ \\ ",
          "  ___) |"],
    '6': ["   __  ",
          "  / /  ",
          " / /_  ",
          " | '_ \\ ",
          " | (_) |"],
    '7': [" ______",
          "|____  |",
          "    / / ",
          "   / /  ",
          "  /_/   "],
    '8': ["  ___  ",
          " / _ \\ ",
          "| (_) |",
          " > _ < ",
          "| (_) |"],
    '9': ["  ___  ",
          " / _ \\ ",
          "| (_) |",
          " \\__, |",
          "   /_/ "],
    ':': ["     ",
          " (_) ",
          "     ",
          " (_) ",
          "     "]
}

def display_time(use_12_hour=False):
    try:
        while True:
            start_time = time.time()
            clear()
            now = datetime.now()

            if use_12_hour:
                time_str = now.strftime("%I:%M:%S")  # 12-hour format
            else:
                time_str = now.strftime("%H:%M:%S")  # 24-hour format

            lines = [""] * 5
            for char in time_str:
                art = ascii_digits.get(char, [" "] * 5)
                for i in range(5):
                    lines[i] += art[i] + "  "

            for line in lines:
                print(line)

            # Sleep to sync with exact second change
            elapsed = time.time() - start_time
            time.sleep(max(0, 1 - elapsed))
    except KeyboardInterrupt:
        print("\nClock stopped. Goodbye!")

# Run in 12-hour mode if you want:
display_time(use_12_hour=False)
