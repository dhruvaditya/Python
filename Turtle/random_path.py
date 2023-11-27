import random
import turtle as t
tim=t.Turtle()
def color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
tim.speed("fastest")
tim.color(color())
for _ in range(100):
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)
    tim.circle(100)
screen=t.Screen()
screen.exitonclick()
# direction=[0,90,180,270]
# for _ in range(200):
#     tim.color(color())
#     tim.forward(20)
#     tim.setheading(random.choice(direction))
