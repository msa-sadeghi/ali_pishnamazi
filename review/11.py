import tkinter as tk
from tkinter import Button
root = tk.Tk()
root.title("my app")
# root.geometry("700x550")
root.resizable(False, False)
root.attributes("-fullscreen", True)
root.overrideredirect(True)

exit_btn = Button(root, text="x", command=root.destroy, font=("arial", 23),border=0)

exit_btn.place(x=root.winfo_screenwidth()-50, y=0)


root.mainloop()