#this file exists in main branch
rows = int(input("enter the number of rows: "))
columns = int(input("enter the number of columns: "))
icon = input("enter any icon to use: ")

for i in range(rows):
    for j in range(columns):
        print(icon, end=" ")
    print()