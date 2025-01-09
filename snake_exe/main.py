# pyinstaller --onefile --windowed --icon=images\orange.ico --add-data="images:images" --name=mygame  .\main.py

from turtle_game_utils import *
from time import sleep
display_surface = make_screen()

root = display_surface._root
root.resizable(False, False)
root.iconbitmap(resource_path("images\orange.ico"))

snake_head = make_turtle("square", "black")
snake_head.direction = ""

snake_food = make_turtle("circle", "red")
change_food_position(snake_food)

display_surface.listen()
display_surface.onkeypress(lambda: go_up(snake_head),
                           "Up")
display_surface.onkeypress(lambda: go_down(snake_head),
                           "Down")
display_surface.onkeypress(lambda: go_right(snake_head),
                           "Right")
display_surface.onkeypress(lambda: go_left(snake_head),
                           "Left")


running = True
while running:
    display_surface.update()
    move_snake(snake_head)
    sleep(0.2)
