def Inverstment_Return(invested_money,rate_of_return):
    #To return time in which the amount will be doubled
    t=((invested_money)*100)/(invested_money*rate_of_return)
    return t
amount=int(input("Enter the amount which you want double"))
#25 din me paisa double hoga aapka
return_of_company=int(input("How much return company give in 1 year"))
print("Your money will be doubled in ",Inverstment_Return(amount,return_of_company)," year")
#Ye bas hera pheri me hota hai asli duniya me paisa double karna hai to padhna hoga
