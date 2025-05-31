from ui.overlay import show_overlay
import keyboard

def start_hotkey_listener(): 
    keyboard.add_hotkey('alt+q', lambda: show_overlay(callback=lambda user_input: print(user_input)))
    keyboard.wait('right alt+`')

if __name__ == '__main__':
    start_hotkey_listener()