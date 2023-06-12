def is_leap(year):


    # To get year (integer input) from the user
    # year = int(input("Enter a year: "))

    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        # print("{0} is a leap year".format(year))
        return True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        # print("{0} is a leap year".format(year))
        return True
    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        # print("{0} is not a leap year".format(year))
        return False
def is_valid_date(date):
    is_valid = True
    thiry_one_day_months=[1,3,5,7,8,10,12]
    date_list=date.split('/')
    if len(date_list)!=3:
        is_valid=False
    else:
        month,day,year=date_list
        try:
            month=int(month)
            day=int(day)
            year=int(year)
            if month>12 or month<1 or day>31 or day<1 or year<1:
                is_valid=False
            elif month not in thiry_one_day_months and day==31:
                is_valid =False
            if is_leap(year) and month==2 and day ==30:
                is_valid =False
            elif not is_leap(year) and month==2 and day>28:
                is_valid= False
        except:
            is_valid=False
    return is_valid


dates = ["12/25/2022", "13/32/2023", "02/29/2024", "02/29/2025", "04/31/2026", "02/29/2028", "12/05/2029"]
for date in dates:
    if is_valid_date(date):
        print(f"{date} is a valid date.")
    else:
        print(f"{date} is not a valid date.")