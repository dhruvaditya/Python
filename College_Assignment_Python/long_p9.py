def is_valid_date(date):
    try:
        month, day, year = map(int, date.split('/'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if year < 0:
            return False

        # Check for specific month and day validity
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if day > 29:
                return False
            if day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                return False

        return True
    except ValueError:
        return False
dates = ["12/25/2022", "13/32/2023", "02/29/2024", "02/29/2025", "04/31/2026", "02/29/2028", "12/05/2029"]
for date in dates:
    if is_valid_date(date):
        print(f"{date} is a valid date.")
    else:
        print(f"{date} is not a valid date.")