#72

def generate_numeric_value(string):
    sum=0
    for char in string:
        print(char)
        m=char.lower()
        c=(ord(m)-96)
        sum=sum+c

    return sum
str=input("Enter the string of which you wanna know numeric value")
print(generate_numeric_value(str))


