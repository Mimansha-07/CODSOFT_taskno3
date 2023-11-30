import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = length_var.get()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)
    password_history.insert(0, f"{password}  ({length} characters)")

# Create the main window
pg = tk.Tk()
pg.title("Password Generator")
# Create and configure the frame
frame = ttk.Frame(pg, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add widgets to the frame
ttk.Label(frame, text="Enter Username:").grid(row=0, column=0, sticky=tk.W)
username_var = tk.StringVar()
username_entry = ttk.Entry(frame, textvariable=username_var)
username_entry.grid(row=0, column=1, sticky=tk.W)

ttk.Label(frame, text="Password Length:").grid(row=1, column=0, sticky=tk.W)
length_var = tk.IntVar(value=12)
length_entry = ttk.Entry(frame, textvariable=length_var)
length_entry.grid(row=1, column=1, sticky=tk.W)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(frame, text="Generated Password:", font=('Helvetica', 10, 'bold'))
result_label.grid(row=3, column=0, columnspan=2, pady=5)

password_history = tk.Listbox(frame, height=2, selectbackground="lightgrey", selectmode=tk.SINGLE)
password_history.grid(row=4, column=0, columnspan=2, pady=4, sticky=tk.W+tk.E)

def accept_password():
    accepted_passwords.insert(tk.END, result_var.get())
accept_button = ttk.Button(frame, text="Accept", command=accept_password)
accept_button.grid(row=5, column=0, pady=5)

reject_button = ttk.Button(frame, text="Reject", command=lambda: result_var.set(""))
reject_button.grid(row=5, column=1, pady=5)

# Run the main loop
pg.mainloop()
