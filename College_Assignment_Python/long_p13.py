from math import sqrt
def is_prime(num):
    is_prime=True
    for i in range(2,round(sqrt(num)+1)):
        if num % i==0:
            is_prime = False
            break
    return is_prime
def main():
    num= eval(input("Enter an even integer greater than 2: "))
    while num%2 ==1 or num <=2:
        print("That's not an even integer greater than 2: Try again")
        num=eval(input("Enter an even integer greater than 2: "))
    primes_list=[]
    for i in range(2,num+1):
        if is_prime(i):
            primes_list.append(i)
    done =False
    for i in primes_list:
        for j in primes_list:
            if i+j == num:
                print(i,"+",j,"-",num)
                done=True
                break
        if done:
            break
main()