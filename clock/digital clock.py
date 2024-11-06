import tkinter as tk
import time

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(window, font=("calibri", 40, "bold"), background="purple", foreground="white")
clock_label.pack(anchor="center")

# Function to update the clock
def update_clock():
    current_time = time.strftime("%H:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Update every second

# Start the clock
update_clock()

# Run the window's main loop
window.mainloop()
