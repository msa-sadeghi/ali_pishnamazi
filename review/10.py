from turtle import *

sc = Screen()
sc.register_shape("SampleGIFImage_350kbmb.gif")
root = sc._root
root.iconbitmap("cat1.svg")
root.resizable(False, False)
# print(sc.window_height())
# print(sc.window_width())
# print(sc._title)
# name = float(sc.textinput("name", "enter your name: "))
# print(name)
# age = sc.numinput("age", "enter your age: ", minval=0, maxval=100)
# print(age)

s = Turtle()
s.shape("turtle") #'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
s.shape("SampleGIFImage_350kbmb.gif") #'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'

s.shapesize(3)
s.color("orange")
counter = 0
running = True
def my_func(x,y):
    print(x,y)
    global running
    running = False
s.begin_fill()
s.forward(300)
s.left(90)
s.forward(300)
s.left(90)
s.end_fill()
while running:
    s.left(10)
    sc.onscreenclick(my_func)
    s.onclick(my_func)
done()