#To find the gcd of two numbers
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a2 % b)


a=int(input("Enter first number"))
b=int(input("Enter second number"))

# prints 12
print(f"The gcd of {a} and {b} is : ", end="")
print(gcd(a, b))