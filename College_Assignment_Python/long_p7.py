# The speeding ticked fine policy in Podunksvill is $50 plus $5
def cal(speed,limit):
    fine=0
    illegal=False
    if(speed>limit):
        fine=(50)+(speed-limit)*(5)
    elif(speed>90):
        fine+=200
    return int(fine)
def main():
    limit=int(input("Enter the speed limit"))
    speed=int(input("Enter the clock speed"))
    fine=cal(speed,limit)
    if(fine==0):
        print("NO FINE")
    else:
        print("There is a fine of $",fine,sep=' ')



if __name__ =='__main__':
    main()
