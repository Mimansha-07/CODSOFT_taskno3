import tkinter as tk
from tkinter import messagebox

box = tk.Tk()
box.title("To-Do List")

frame_tasks = tk.Frame(box)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=15, width=50)
listbox_tasks.pack(side=tk.LEFT)
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(box, width=50)
entry_task.pack(pady=15)
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

button_add_task = tk.Button(box, text="Add Task", width=48, command=add_task)
button_add_task.pack()

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

button_delete_task = tk.Button(box, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_quit = tk.Button(box, text="Quit", width=48, command=box.destroy)
button_quit.pack()

box.mainloop()
