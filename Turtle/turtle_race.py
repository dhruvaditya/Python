import random
import turtle
from turtle import Turtle,Screen
screen = Screen()
screen.setup(width=500,height=500)
all_turtle=[]
is_race=False
user_bet=screen.textinput(title="Make your bet",prompt="Which color will wing?")
colors=["red","orange","yellow","green","purple","blue"]
y_positions=[-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_positions[turtle_index])
    all_turtle.append(tim)
if user_bet:
    is_race=True
while is_race:
    for tur in all_turtle:
        if(tur.xcor()>230):
            is_race=False
            winning_color=tur.pencolor()
            if(winning_color==user_bet):
                print(f"You win! {winning_color} is the winner")
            else:
                print(f"You Lost!{winning_color} is the winner")
        rand_distance=random.randint(0,10)
        tur.forward(rand_distance)
screen.exitonclick()