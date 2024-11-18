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


class Snake:
    def __init__(self) -> None:
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []
        for i in range(BODY_SIZE):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill="yellow", tag="snake")
            print(type(square))
            self.squares.append(square)

class Food:
    def __init__(self) -> None:
        x = randint(0, (GAME_WIDTH//SPACE_SIZE-1)) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT//SPACE_SIZE-1)) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x,y, x+SPACE_SIZE, y + SPACE_SIZE, fill="red", tag="food")

from tkinter import *
from random import randint
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
BODY_SIZE = 2
score = 0
window = Tk()
window.title("snake")
window.resizable(False, False)
label = Label(window, text=f"Score:{score}", font=("Courier", 30))
label.pack()

canvas = Canvas(window, bg="black", width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

restart_button = Button(window, bg="white", fg="darkgreen", text="restart", font=("courior", 14))
restart_button.pack(side="left")
exit_button = Button(window, bg="white", fg="darkgreen", text="exit", font=("courior", 14), command=window.destroy)
exit_button.pack(side="right")
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()
window.mainloop()