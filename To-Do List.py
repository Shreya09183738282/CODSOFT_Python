import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

root = tk.Tk()
root.title("To-Do List")

# Styling
input_bg_color = "black"
input_fg_color = "white"
listbox_bg_color = "aqua"
listbox_fg_color = "black"

entry = tk.Entry(root, font=("Helvetica", 16), bg=input_bg_color, fg=input_fg_color)
entry.pack(fill=tk.BOTH, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(fill=tk.BOTH, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(fill=tk.BOTH, padx=10, pady=5)

listbox = tk.Listbox(root, font=("Helvetica", 16), bg=listbox_bg_color, fg=listbox_fg_color)
listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
