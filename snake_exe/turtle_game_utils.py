import sys
import os
from turtle import Screen, Turtle
from random import randint


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS',
                        os.path.dirname(
                             os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def make_screen():
    window = Screen()
    window.bgcolor('blue')
    window.title('Snake Game')
    window.setup(width=600, height=600)
    return window


def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.speed(0)
    my_turtle.penup()
    return my_turtle


def change_food_position(food):
    xpos = randint(-270, 270)
    ypos = randint(-270, 270)
    food.goto(xpos, ypos)


def go_up(head):
    head.direction = "up"


def go_down(head):
    head.direction = "down"


def go_left(head):
    head.direction = "left"


def go_right(head):
    head.direction = "right"


def move_snake(head):
    if head.direction == "up":
        snake_head_y_position = head.ycor()
        snake_head_y_position += 20
        head.sety(snake_head_y_position)

    if head.direction == "down":
        snake_head_y_position = head.ycor()
        snake_head_y_position -= 20
        head.sety(snake_head_y_position)

    if head.direction == "left":
        snake_head_x_position = head.xcor()
        snake_head_x_position -= 20
        head.setx(snake_head_x_position)

    if head.direction == "right":
        snake_head_x_position = head.xcor()
        snake_head_x_position += 20
        head.setx(snake_head_x_position)
