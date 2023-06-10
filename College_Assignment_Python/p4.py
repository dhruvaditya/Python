#Inverted right angle triangle
height=int(input("Enter the height of the triangle: "))
for i in range(height,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()