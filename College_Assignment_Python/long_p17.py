def function(n):
    sum=0
    for i in range(1, n + 1):
        if (n % i == 0):
            sum+=i

    return sum
num=int(input("Enter a number"))
print(function(num))