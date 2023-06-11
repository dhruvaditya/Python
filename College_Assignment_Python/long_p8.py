def main():
    year = input("Enter a year between 1982 and 2048: ")
    if year < 1982 or year > 2048:
        print("Illegal date")
    else:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        days_after = d + e
        days = 22 + days_after
        print
        "In year ", year, ", Easter falls on",
        if days <= 31:
            print
            "March ", str(days)
        else:
            print
            "April ", str(days - 31)


main()