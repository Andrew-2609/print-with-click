from datetime import datetime

from pynput.mouse import Listener, Button

from screenshot import Screenshooter

screenthots_path = input(
    "Where do you want to save the screenshots from now on?\nType the absolute path (ex: '/home/bob': ")
my_screenshooter = Screenshooter(0, screenthots_path)


def on_click(x, y, button, pressed):
    if pressed and button == Button.left:
        my_screenshooter.take_screenshot()
        print(f"Printed at {datetime.now()} when you clicked at ({x}, {y})")


with Listener(on_click=on_click) as listener:
    try:
        print("Listening...")
        listener.join()
    except KeyboardInterrupt:
        exit(0)
