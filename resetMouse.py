#! python3
# resetMouse.py - resets mouse on click - usuful for students with
# cognitive disabilities.

import pyautogui

width, height = pyautogui.size()
midWidth = width + 1 / 2
midHeight = height + 1 / 2
try:
    while True:
        pyautogui.moveTo(midWidth, midHeight)
except KeyboardInterrupt:
    print('\nDone.')
