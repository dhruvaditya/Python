import turtle as t
tim=t.Turtle()
i=5
side=5
while(i>0):
    for _ in range(side):
        angle=360/side
        tim.forward(100)
        tim.right(angle)
    side=side+1
    i=i-1