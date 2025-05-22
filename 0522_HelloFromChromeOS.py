import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# user_name = input("Enter your name: ")
def greet():
    name = entry.get()
    today = datetime.now().strftime("%Y-%m-%d")
    messagebox.showinfo("Greeting", f"Hello! {name}, today is \"{today}\"")

root = tk.Tk()
root.title("Hello From ChromeOS")

tk.Label(root, text="Enter your name:").pack(padx=10, pady=5)
entry = tk.Entry(root)
entry.pack(padx=10, pady=5)

tk.Button(root, text="Greet", command=greet).pack(padx=10, pady=10)

root.mainloop()