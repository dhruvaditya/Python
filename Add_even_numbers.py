#To add even numbers from 2 to 100
print("hello python")
#First method is by using range functionality
total = 0
for number in range(2, 100, 2):
  total += number

print(total)

#Second method is by first checking a number is even then adding it to the total
total2 = 0
for number in range(1, 100):
  if (number % 2 == 0):
    total2 += number
print(total2)
