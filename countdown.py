#! python3
# countdown.py

import time
import subprocess

timeLeft = 5

while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1
# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)
