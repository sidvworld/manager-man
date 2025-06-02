from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading
import os
import sys
import queue
import time

from hotkey_listener import start_hotkey_listener
from ui.overlay import show_overlay

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
    return Icon("TaskForce", image, "TaskForce", menu)

overlay_queue = queue.Queue()

def overlay_poller():
    while True:
        try:
            overlay_queue.get(timeout=0.5)
            show_overlay(callback=handle_input)
        except queue.Empty:
            continue

if __name__ == "__main__":
    try:
        threading.Thread(target=start_hotkey_listener, args=(overlay_queue,), daemon=True).start()
    except Exception as e:
        print(f"hotkey thread error: {e}")

    tray_icon = setup_tray()
    if tray_icon:
        tray_icon.run()

    overlay_poller()