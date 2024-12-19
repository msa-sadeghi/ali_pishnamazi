from tkinter import *
def my_func(e):
    print("Hello")

def do_exit():
    root.destroy()
   
root = Tk()
root.config(bg="red")
root.option_readfile("optionDb")
Label(root, text="salam").pack()
t1 = Toplevel(root)
Label(t1, text="python").pack()
t1.overrideredirect(True)

t1.bind('<Alt-F4>',lambda e: my_func(e))
t1.protocol("WM_DELETE_WINDOW",do_exit)
root.mainloop()

