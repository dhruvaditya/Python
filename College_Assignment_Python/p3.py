#use a for loop to print a right angle triangle and allow user to give the height
height=int(input("Enter the height of the triangle: "))
for i in range(1,height+1):
    for j in range(1,i+1):
        print("*",end=" ")

    print()
