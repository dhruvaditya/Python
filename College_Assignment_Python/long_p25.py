def digital_root(num):
    sum=0
    while(num>0):
        sum+=num%10
        num=num//10
    return int(sum)

n=int(input("Enter the number of which you wanna know digital root"))
print(digital_root(n))