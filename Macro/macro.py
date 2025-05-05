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


def move_mouse(x, y):
    mouse_controller.position = (x, y)

def keyboard_press(key):
    keyboard_controller.press(key.char)
    keyboard_controller.release(key.char)

def click(right_left):
    if right_left == 'left':
        mouse_controller.click(Button.left)
    elif right_left == 'right':
        mouse_controller.click(Button.right)

def run_macro():
    print("Macro started. Press 'z' to stop.")
    while running:
        move_mouse(1300,800)
        click('left')
        for x in range(30):
            move_mouse(700,1100)
            click('left')
            time.sleep(0.1)
            click('left')
        move_mouse(1400,757) # 1
        click('left')
        time.sleep(0.1) 
        move_mouse(1650,757) # 2
        click('left')
        time.sleep(0.1)
        move_mouse(1900,757) # 3
        click('left')
        time.sleep(0.1)
        move_mouse(2131,757) # 4
        click('left')
        time.sleep(0.1)
        move_mouse(2370,757) # 5
        click('left')
        time.sleep(0.1)
        move_mouse(1400,1152) # 1
        click('left')
        time.sleep(0.1)
        move_mouse(1650,1152) # 2
        click('left')
        time.sleep(0.1)
        move_mouse(1900,1152) # 3
        click('left')
        time.sleep(0.1)
        move_mouse(2131,1152) # 4
        click('left')
        time.sleep(0.1)
        move_mouse(2370,1152) # 5
        click('left')
        time.sleep(0.1)


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
