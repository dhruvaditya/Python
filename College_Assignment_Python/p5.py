import random
count=0
for _ in range(10000):
        num=random.randint(1,100)
        if(num%12==0):
            count=count+1

print(count)