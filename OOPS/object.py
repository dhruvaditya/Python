class Software:
    def __init__(self,name,sal,age,dob):
        self.name=name
        self.sal=sal
        self.age=age
        self.dob=dob
    def code(self):
        print(f"{self.name} is writing code...")
        
se1=Software("Ram",2000,23,"SDE")
se2=Software("shyam",2000,23,"SDE")
se3=Software("Vikram",2000,23,"SDE")
print(se1.name,se1.age)
se1.code()
se2.code()
