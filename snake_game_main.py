from snake_game_utils import *
from time import sleep
import os
score = 0

if os.path.exists("score.txt"):
    with open("score.txt", "r") as f:
        highscore = int(f.read())
else:
    highscore = 0
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)

def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"
def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"
def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)

main_screen.listen()
main_screen.onkeypress(go_up, "Up")
main_screen.onkeypress(go_down, "Down")
main_screen.onkeypress(go_left, "Left")
main_screen.onkeypress(go_right, "Right")

def close_the_window():
    with open("score.txt", "w") as f:
        f.write(str(highscore))
    global running
    running = False

root = main_screen._root
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", close_the_window)


scoreboard = create_turtle("square", "orange")
scoreboard.goto(0, 260)
scoreboard.ht()


tails = []

running = True
while running:
    main_screen.update()
    scoreboard.clear()
    scoreboard.write(f"Score:{score}, highScore:{highscore}", font=("arial", 22), align="center")


    if snake_head.distance(snake_food) < 20:
        change_position(snake_food)
        score += 1
        if score > highscore:
            highscore = score
        new_tail = create_turtle("square","darkgreen")
        tails.append(new_tail)

    for i in range(len(tails) - 1, 0, -1):
        x = tails[i-1].xcor()
        y = tails[i-1].ycor()
        tails[i].goto(x,y)
    if tails:
        tails[0].goto(snake_head.xcor(), snake_head.ycor())

    if snake_head.xcor() > 290 or snake_head.xcor() < -290:
        snake_head.setx(snake_head.xcor() * -1)

    if snake_head.ycor() > 240:
        snake_head.sety(-290)
    if snake_head.ycor() < -290:
        snake_head.sety(240)

    move()

    for tail in tails:
        if tail.distance(snake_head)<20:
            snake_head.home()
            snake_head.direction = ""
            score = 0
            for tail in tails:
                tail.ht()
            tails = []



    sleep(0.2)