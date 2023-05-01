#Building a Calculator
def multiply(a,b):
  return(a*b);
def add(a,b):
  return(a+b)
def sub(a,b):
  return(a-b)

def div(a,b):
  return(a/b)

operations={"*":multiply,
            "+":add,
            "-":sub,
            "%":div
           }
num1=int(input("Enter your first number"))
num2=int(input("Enter second number"))
for key in operations:
  print(key)

print("Chose one of a operation")
op=input("Write Here")
if(op=="*"):
  print(multiply(num1,num2))
elif(op=="-"):
  print(sub(num1,num2))
elif(op=="%"):
  print(div(num1,num2))
elif(op=="+"):
  print(add(num1,num2))

