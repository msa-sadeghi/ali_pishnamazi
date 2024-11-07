import tkinter as tk
from tkinter import Button
root = tk.Tk()
# root.title("my app")

root.resizable(False, False)
# root.attributes("-fullscreen", True)
# root.overrideredirect(True)

root.geometry("1000x850")
center_x = root.winfo_width()//2
center_y = root.winfo_height()//2
print(center_x, center_y)
root.update()


exit_btn = Button(root, text="x", command=root.destroy, font=("arial", 23),border=0)


exit_btn.place(x=root.winfo_screenwidth()-50, y=0)

my_button = Button(root, text="تایید", padx=30, pady=30, bg="#000000", fg="WHITE")
my_button.pack(side="bottom")

print(root.winfo_width())
root.mainloop()