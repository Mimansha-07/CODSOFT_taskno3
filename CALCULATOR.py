import tkinter as tk
import math

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for displaying the input and result
entry = tk.Entry(root, width=22, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# Buttons
button_texts = [
    'C', '√', '/', '<-',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '!', '0', '.', '='  
]

# Create buttons dynamically using a nested loop
row_val = 1
for i in range(5):
    for j in range(4):
        index = i * 4 + j
        button_text = button_texts[index]
        
        if button_text == 'C':
            tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 16), command=clear_entry).grid(row=row_val, column=j)
        elif button_text == '√':
            tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 16), command=calculate_square_root).grid(row=row_val, column=j)
        else:
            tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 16), command=lambda b=button_text: on_button_click(b) 
                      if b != '=' else calculate_result()).grid(row=row_val, column=j)

    row_val += 1

root.mainloop()
