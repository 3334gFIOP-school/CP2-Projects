from pynput import mouse, keyboard
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Listener as KeyboardListener, Key
import threading
import time

# Controllers
mouse_controller = MouseController()
keyboard_controller = KeyboardController()

# Global flag to stop macro
running = True

def run_macro():
    print("Macro started. Press 'z' to stop.")
    while running:
        # Example actions
        mouse_controller.position = (0, 0)
        time.sleep(0.5)

        mouse_controller.click(Button.left)
        time.sleep(0.5)

        mouse_controller.scroll(0, 2)  # scroll up
        time.sleep(0.5)

        keyboard_controller.press('a')
        keyboard_controller.release('a')
        time.sleep(0.5)

def on_press(key):
    global running
    try:
        if key.char == 'z':
            print("Stopping macro...")
            running = False
            return False  # Stop listener
    except AttributeError:
        pass

def main():
    # Start the macro in a separate thread
    macro_thread = threading.Thread(target=run_macro)
    macro_thread.start()

    # Listen for 'z' key to stop
    with KeyboardListener(on_press=on_press) as listener:
        listener.join()

    macro_thread.join()
    print("Macro ended.")

if __name__ == "__main__":
    main()
