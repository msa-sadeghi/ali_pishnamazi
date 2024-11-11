# def bubble_sort(arr):
#     for j in range(len(arr)):
#         r = False
#         for i in range(len(arr)-j-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 r = True
#         if not r :
#             break
# arr = [1,2,3,4,5,6,7]
# bubble_sort(arr)
# print(arr)


from tkinter import *

window = Tk()
window.title("snake")
window.resizable(False, False)

label = Label(window, text=f"Score", font=("Courier", 30))
label.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")



window.mainloop()