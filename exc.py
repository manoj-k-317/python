#this file exixts in sub branch

row_1 = ["1","2","3"]
row_2 = ["4","5","6"]
row_3 = ["7","8","9"]
row_4 = ["#","0","*"]

num_pad = [row_1, row_2, row_3, row_4]
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()