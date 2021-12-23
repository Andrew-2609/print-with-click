from pynput.mouse import Listener, Button


def on_click(x, y, button, pressed):
    if pressed and button == Button.left:
        print(x, y)
        print("Mouse clicked.")


with Listener(on_click=on_click) as listener:
    listener.join()
