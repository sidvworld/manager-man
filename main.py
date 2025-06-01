import pystray
from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading
import sys
import os

from hotkey_listener import start_hotkey_listener

def on_quit(icon, item):
    icon.stop()
    sys.exit()

def setup_tray():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, "taskforce_downsized.png")
    image = Image.open(icon_path)

    menu = Menu(
        MenuItem("Quit", on_quit)
    )
    icon = Icon("TaskManager", image, "Task Manager", menu)
    icon.run()

if __name__ == "__main__":
    threading.Thread(target=start_hotkey_listener, daemon=True).start()
    setup_tray()
