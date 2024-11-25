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

# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)


# print(factorial(5))




class Snake:
    def __init__(self) -> None:
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []
        for i in range(BODY_SIZE):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill="yellow", tag="snake")

            self.squares.append(square)

class Food:
    def __init__(self) -> None:
        x = randint(0, (GAME_WIDTH//SPACE_SIZE-1)) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT//SPACE_SIZE-1)) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x,y, x+SPACE_SIZE, y + SPACE_SIZE, fill="red", tag="food")

def change_direction(new_dir):
    global direction
    if new_dir == "left":
        if direction != "right":
            direction = new_dir
    elif new_dir == "right":
        if direction != "left":
            direction = new_dir
    elif new_dir == "up":
        if direction != "down":
            direction = new_dir
    elif new_dir == "down":
        if direction != "up":
            direction = new_dir


def next_turn(snake, food):
    x,y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, [x,y])
    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill="yellow", tag="snake")
    
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score:{score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    window.after(200, next_turn, snake, food)
        

from tkinter import *
from random import randint
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
BODY_SIZE = 2
score = 0
direction = "down"
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

window.bind('<Up>',lambda e: change_direction("up"))
window.bind('<Down>',lambda e: change_direction("down"))
window.bind('<Left>',lambda e: change_direction("left"))
window.bind('<Right>',lambda e: change_direction("right"))

snake = Snake()
food = Food()
next_turn(snake, food)
window.mainloop()
