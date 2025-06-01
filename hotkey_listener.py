from ui.overlay import show_overlay
from nlp_parser import parse_text
from db_task import save_task
import keyboard
import time
import threading

def handle_input(user_input):
    if user_input and user_input.strip():
        task_obj = parse_text(user_input)
        save_task(task_obj)
        print(f"task saved: {task_obj.task_name}, {task_obj.task_deadline}, {task_obj.task_priority}, {task_obj.created_at}")
    else:
        print("user input is empty")

def start_hotkey_listener(): 
    keyboard.add_hotkey('alt+=', lambda: threading.Thread(target=show_overlay, kwargs={'callback': handle_input}).start(), suppress=True)

start_hotkey_listener()
while True:
    time.sleep(5)

