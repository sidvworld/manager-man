from ui.overlay import show_overlay
from nlp_parser import parse_text
from db_task import save_task, init_db
import keyboard
import time

def handle_input(user_input):
    if user_input:
        task_obj = parse_text(user_input)
        save_task(task_obj)
        print(f"task saved: {task_obj.task_name}, {task_obj.task_deadline}, {task_obj.task_priority}, {task_obj.created_at}")

def start_hotkey_listener(): 
    init_db()
    keyboard.add_hotkey('alt+q', lambda: show_overlay(callback=handle_input), suppress=True)
    keyboard.wait('right alt+`')

if __name__ == '__main__':
    start_hotkey_listener()
    while True:
        time.sleep(1)