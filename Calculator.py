import tkinter as tk
import math

# ---------- Functions ----------

def click(value):
    try:
        if value == "=":
            result = str(eval(screen.get()))
            history_list.insert(tk.END, screen.get() + " = " + result)
            screen.set(result)

        elif value == "C":
            screen.set("")

        elif value == "√":
            result = str(math.sqrt(float(screen.get())))
            history_list.insert(tk.END, f"√({screen.get()}) = {result}")
            screen.set(result)

        elif value == "x²":
            result = str(float(screen.get()) ** 2)
            history_list.insert(tk.END, f"{screen.get()}² = {result}")
            screen.set(result)

        elif value == "sin":
            result = str(math.sin(math.radians(float(screen.get()))))
            history_list.insert(tk.END, f"sin({screen.get()}) = {result}")
            screen.set(result)

        elif value == "cos":
            result = str(math.cos(math.radians(float(screen.get()))))
            history_list.insert(tk.END, f"cos({screen.get()}) = {result}")
            screen.set(result)

        elif value == "tan":
            result = str(math.tan(math.radians(float(screen.get()))))
            history_list.insert(tk.END, f"tan({screen.get()}) = {result}")
            screen.set(result)

        elif value == "log":
            result = str(math.log10(float(screen.get())))
            history_list.insert(tk.END, f"log({screen.get()}) = {result}")
            screen.set(result)

        elif value == "!":
            result = str(math.factorial(int(float(screen.get()))))
            history_list.insert(tk.END, f"{screen.get()}! = {result}")
            screen.set(result)

        else:
            screen.set(screen.get() + value)

    except:
        screen.set("Error")


def key_input(event):
    key = event.char
    if key in "0123456789+-*/.":
        screen.set(screen.get() + key)
    elif key == "\r":
        click("=")


def clear_history():
    history_list.delete(0, tk.END)


# ---------- Theme Toggle ----------
dark_mode = True

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        root.configure(bg="#1e1e1e")
        entry.config(bg="#2d2d2d", fg="white", insertbackground="white")
    else:
        root.configure(bg="#f5f5f5")
        entry.config(bg="white", fg="black", insertbackground="black")


# ---------- UI ----------

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x550")
root.configure(bg="#1e1e1e")

screen = tk.StringVar()

entry = tk.Entry(root, textvar=screen, font="Arial 20",
                 bg="#2d2d2d", fg="white", insertbackground="white")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Buttons
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
    ['C','√','x²','!'],
    ['sin','cos','tan','log']
]

for row in buttons:
    frame = tk.Frame(root, bg=root["bg"])
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 14",
                      bg="#3c3f41", fg="white", relief="flat")
        b.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        b.bind("<Button-1>", lambda e, val=btn: click(val))

# Theme Button
tk.Button(root, text="Toggle Theme", command=toggle_theme).pack(pady=5)

# History Panel
history_frame = tk.Frame(root)
history_frame.pack(fill="both", padx=10, pady=5)

tk.Label(history_frame, text="History").pack()

history_list = tk.Listbox(history_frame)
history_list.pack(fill="both", expand=True)

# Clear History Button
tk.Button(root, text="Clear History", command=clear_history).pack(pady=5)

# Keyboard Support
root.bind("<Key>", key_input)

root.mainloop()