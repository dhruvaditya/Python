#By this way we can do operations in an array
#conditional statement in python

student={"Aditya":99,"Ashutosh":78,"Ayush":53,"Piyush":32}
for key in student:
  if(student[key]>90):
    print("Outstanding")
  
  elif(student[key]>70):
    print("Excellent")
  
  elif(student[key]>50):
    print("Average")
  
  else:
    print("fail")
  
