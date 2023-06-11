# Write a program to find all numbers between 1 and 1000 that are divisible by 7 and end in  a 6
def checker():
    interger_list=[]
    for i in range(1,1001):
        if(i%7==0 and i%10==6):
            interger_list.append(i)

    return interger_list

print(checker())