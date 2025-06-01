from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading
import os
import sys

from hotkey_listener import start_hotkey_listener

def on_quit(icon, item):
    icon.stop()
    sys.exit()

def setup_tray():
    icon_path = "assets/taskforce-logo.ico"
    if not os.path.exists(icon_path):
        print("icon not found:", icon_path)
        return

    image = Image.open(icon_path)
    menu = Menu(MenuItem("Quit", on_quit))
    return Icon("TaskManager", image, "Task Manager", menu)

if __name__ == "__main__":
    try:
        threading.Thread(target=start_hotkey_listener, daemon=True).start()
    except Exception as e:
        print(f"hotkey thread error: {e}")

    tray_icon = setup_tray()
    if tray_icon:
        tray_icon.run()