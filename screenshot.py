import pyautogui


class Screenshooter:
    def __init__(self, count, screenshots_path):
        self.count = count
        self.screenshots_path = screenshots_path

    def take_screenshot(self):
        pyautogui.screenshot().save(f"{self.screenshots_path}/screenshot{self.count}.png")
        self.count += 1
