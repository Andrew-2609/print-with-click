import pyautogui


class Screenshooter:
    def __init__(self, start_count_from, screenshots_path):
        self.count = start_count_from
        self.screenshots_path = screenshots_path

    def take_screenshot(self):
        pyautogui.screenshot().save(f"{self.screenshots_path}/screenshot{self.count}.png")
        self.count += 1
