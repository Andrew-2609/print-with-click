from datetime import datetime

from pynput.mouse import Listener, Button

from screenshot import Screenshooter

print("\n" + "-" * 32)
print("# Welcome!\n")

defining_path = True
while defining_path:
    try:
        screenthots_path = input(
            "## Where do you want to save the screenshots from now on?\n > Type the absolute path (ex: '/home/bob': ")
        my_screenshooter = Screenshooter(start_count_from=0, screenshots_path=screenthots_path)
        my_screenshooter.take_screenshot()

        defining_path = False
    except FileNotFoundError:
        print("### The given path was invalid. Please, try again!\n")
    except KeyboardInterrupt:
        print("\n\n# Exiting...\n")
        exit(0)


def on_click(x, y, button, pressed):
    if pressed and button == Button.left:
        my_screenshooter.take_screenshot()
        print(f"Printed at {datetime.now()} when you clicked at ({x}, {y})")


with Listener(on_click=on_click) as listener:
    try:
        print("Listening...")
        listener.join()
    except KeyboardInterrupt:
        print("\n\n# Exiting...")
        exit(0)
