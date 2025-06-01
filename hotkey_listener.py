from ui.overlay import show_overlay
from nlp_parser import parse_text
from server_db.db_tasks import save_task_table
import keyboard
import time
import threading

def handle_input(user_input):
    if user_input and user_input.strip():
        task_obj = parse_text(user_input)
        save_task_table(task_obj)
    else:
        print("user input is empty")

def start_hotkey_listener(): 
    keyboard.add_hotkey('alt+=', lambda: threading.Thread(target=show_overlay, kwargs={'callback': handle_input}).start(), suppress=True)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    start_hotkey_listener()
