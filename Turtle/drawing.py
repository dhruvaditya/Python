from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def dwn():
    angle=10
    tim.right(angle)
def up():
    angle=10
    tim.left(angle)
screen.listen();
screen.onkey(key="space",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="w",fun=up)
screen.onkey(key="c",fun=dwn)
screen.exitonclick()