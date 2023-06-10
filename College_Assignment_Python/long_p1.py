def fibb(n):
    if(n==0 or n==1):
        return 1;
    else:
        return fibb(n-1)+fibb(n-2)
n=int(input("Enter the nth term"))
print(fibb(n-1))