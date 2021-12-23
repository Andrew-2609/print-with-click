import pyautogui


class Screenshooter:
    def __init__(self, count):
        self.count = count

    def take_screenshot(self):
        pyautogui.screenshot().save(f"screenshots/screenshot{self.count}.png")
        self.count += 1
