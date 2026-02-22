import pyautogui

class Controller:
    def __init__(self):
        pass

    def execute_gesture(self, gesture):
        if gesture == "RIGHT":
            pyautogui.press("right")
        elif gesture == "LEFT":
            pyautogui.press("left")
        elif gesture == "JUMP":
            pyautogui.press("space")
        elif gesture == "SLIDE":
            pyautogui.press("down")