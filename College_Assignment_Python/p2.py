#Use a for loop to print a hollow box and allow user to give length and breadthh
rows=int(input("Enter the number of rows "))
column=int(input("Enter the numer of columns"))
for i in range(0,rows):
    for j in range(0,column):
        if(i==0 or i==rows-1 or j==0 or j==column-1):
            print("*",end="  ")
        else:
            print(" ",end="  ")
    print()