import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("400x578")
root.title("Simple Calculator")

screen = tk.StringVar()
screen.set("")

entry = tk.Entry(root, textvar=screen, font="lucida 40 bold", bg="aqua", bd=10)
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0

for button_text in buttons:
    btn = tk.Button(button_frame, text=button_text, font="lucida 25 bold", padx=20, pady=20, bg="aqua", bd=8)
    btn.grid(row=row, column=col, sticky="nsew")
    btn.bind("<Button-1>", on_button_click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)

button_frame.grid_rowconfigure(1, weight=1)
button_frame.grid_rowconfigure(2, weight=1)
button_frame.grid_rowconfigure(3, weight=1)
button_frame.grid_rowconfigure(4, weight=1)

root.mainloop()
