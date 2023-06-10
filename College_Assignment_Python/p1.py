# #Use a for loop to print a box. Allow the user to specify how wide and how high the box should be
rows = int(input("Enter Number of Rows: "))
columns = int(input("Enter Number of Columns: "))

print("Box Pattern with", rows, "rows and", columns, "columns")

for i in range(0, rows):
    for j in range(0, columns):
        print('*',end=' ')
    print()