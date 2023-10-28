import time
from playsound import playsound
from turtle import *
import turtle

turt = turtle.Screen()
turt.bgcolor("ivory")
turtle = turtle.Turtle()


# turtle.shape("circle")
# turtle.color("yellow")
# turtle.width(7)
# colors=["peru","ivory","dark orange","coral","hot pink","gold","ivory","yellow",  "pink","green ","light green","red","violet"]
def pattern():
    colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']
    for x in range(130):
        pencolor(colors[x % 6])
        width(x / 5 + 1)
        forward(x)
        left(20)


def kite():
    time.sleep(3)
    for i in range(1):
        turtle.pensize(7)
        turtle.pencolor("ivory")

        # turtle.begin_fill()

        # turtle.color(colors[i%18])
        # turtle.begin_fill()
        turtle.goto(30, 30)
        turtle.color("light blue")
        turtle.begin_fill()

        turtle.forward(40)
        turtle.left(120)
        turtle.forward(40)
        turtle.left(120)

        turtle.backward(40)
        # turtle.end_fill()
        # turtle.pencolor('yellow')
        turtle.forward(40)
        # turtle.fillcolor("red")
        turtle.penup()
        turtle.towards(22, 36.64)
        turtle.pendown()
        turtle.right(100)
        turtle.fillcolor("lightblue")
        turtle.end_fill()
        turtle.begin_fill()
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)

        turtle.fillcolor("gray")
        turtle.end_fill()
        turtle.right(45)

        # turtle.backward(40)
        # turtle.forward(210)
        turtle.right(45)
        turtle.penup()
        turtle.towards(-94.9, 131)
        turtle.goto(-200, -200)
        turtle.color("orange")
        turtle.begin_fill()

        turtle.forward(40)
        turtle.left(120)
        turtle.forward(40)
        turtle.left(120)

        turtle.backward(40)
        turtle.end_fill()
        # turtle.pencolor('yellow')
        turtle.forward(40)
        # turtle.fillcolor("red")
        turtle.penup()
        turtle.towards(22, 36.64)
        turtle.pendown()
        turtle.right(100)
        turtle.begin_fill()
        turtle.fillcolor("coral")
        turtle, end_fill()
        turtle.begin_fill()
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)

        turtle.fillcolor("dark orange")
        turtle.end_fill()
        turtle.right(45)

        # turtle.backward(40)
        # turtle.forward(210)
        turtle.right(45)
        turtle.penup()
        turtle.towards(-94.9, 131)
        turtle.goto(200, 200)
        turtle.color("orange")
        turtle.begin_fill()

        turtle.forward(40)
        turtle.left(120)
        turtle.forward(40)
        turtle.left(120)

        turtle.backward(40)
        # turtle.end_fill()
        # turtle.pencolor('yellow')
        turtle.forward(40)
        # turtle.fillcolor("red")
        turtle.penup()
        turtle.towards(22, 36.64)
        turtle.pendown()
        turtle.right(100)
        turtle.fillcolor("aqua")
        turtle.end_fill()
        turtle.begin_fill()
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)

        turtle.fillcolor("red")
        turtle.end_fill()
        turtle.right(45)

        # turtle.backward(40)
        # turtle.forward(210)
        turtle.right(45)
        turtle.penup()
        turtle.towards(-94.9, 131)

        turtle.pendown()
        # turtle.circle(-150,extent=90)
        turtle.hideturtle()
    time.sleep(3)


def letter():
    for i in range(2):
        turtle.color('deep pink')
        style = ('Courier', 20, 'italic')

        turtle.write("HAPPY MAKAR SANKRANTI\n", font=("Calibri", 25, "bold"))
        # pendown()

        # turtle.write("MakarSankranti ", font=("Calibri", 30, "bold"))
        turtle.hideturtle()
    time.sleep(4)


def playsound1():
    playsound("song.mp3")


if __name__ == "__main__":
    # playsound1()

    kite()
    letter()
    # pattern()