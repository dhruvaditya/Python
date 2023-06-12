#One way to find the last digit of a number is to mod by 10
#In this first we will take power and convert it to 2^power then find the last digit
#A
def single_digit(power):
    num= 2**power
    digit=num%10
    return digit
#B
def double_digit(power):
    num=2**power
    digit=num%100
    return  digit
#C
def calculate(power,digit):
    num=2**power
    c=10**digit
    result=num%c
    return result

power=int(input("Enter the power of 2"))
d=int(input("digit of no. of digits"))
result=calculate(power,d)
result_str=str(result).zfill(d)
print("The result is:", result_str)


