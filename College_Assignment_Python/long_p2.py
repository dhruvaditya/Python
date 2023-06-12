import math
def main():
    n = int(input("Please enter a value for N:"))
    total=0
    for i in range(1,n):
        total += (-1)**(i+1)*((1.0/(i+i+1)))

    value = 4*(1-total)
    value2=value-math.pi
    print(value)
    print("The difference between calculated pie and inbuit pie is: ",value2)

main()