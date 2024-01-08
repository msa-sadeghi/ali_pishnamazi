from random import randint
from turtle import Screen, Turtle
main_screen = Screen()
main_screen.setup(600, 600)
main_screen.bgcolor("black")
main_screen.title("snake game")
main_screen.tracer(False)

def create_turtle(sh, c):
    my_turtle = Turtle()
    my_turtle.shape(sh)
    my_turtle.color(c)
    my_turtle.penup()
    return my_turtle


def change_position(object):
    x = randint(-270, 270)
    y = randint(-270, 240)
    object.goto(x,y)


