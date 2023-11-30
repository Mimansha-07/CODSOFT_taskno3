import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) 
    for _ in range(length))
    result_var.set(password)

# Create the main window
box = tk.Tk()
box.title("Password Generator")

# Create and configure the frame
frame = ttk.Frame(box, padding="10")
frame.title(password generator)
frame.grid(row=6, column=8)
entry = tk.Entry(box, width=22)
entry.grid(row=0, cloumn=0, columnspan=5)

# Add widgets to the frame
generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=0, column=0)

result_var = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_var, wraplength=300, justify=tk.LEFT)
result_label.grid(row=1, column=0, pady=10)

# Run the main loop
root.mainloop()
