import tkinter as tk
import pyautogui

def update_coords():
    x, y = pyautogui.position()  # Get mouse position globally
    coords_label.config(text=f"Mouse Position: ({round(x)}, {round(y)})")
    root.after(50, update_coords)  # Call update_coords every 50ms

# Create the main window
root = tk.Tk()
root.title("Global Mouse Position Tracker")

# Set the size of the window
root.geometry("400x200")

# Create a label to display the mouse coordinates
coords_label = tk.Label(root, text="Mouse Position: (0, 0)", font=("Arial", 14))
coords_label.pack(pady=50)

# Start tracking the mouse position
update_coords()

# Run the application
root.mainloop()
