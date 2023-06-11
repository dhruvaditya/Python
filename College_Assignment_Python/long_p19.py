n=int(input("Enter the number of line"))
for i in range(1,n+1):
    for j in range(0,i):
        if(j==i-1):
            print(i,end=' ')
        else:
            print(' ',end=' ')
    print()