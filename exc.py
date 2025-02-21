#this file exixts in sub branch

name = str(input("Enter your name please:"))

lenght = len(name)
if lenght > 12:
    print("name should not exceed 12 letters")

num_or_space = name.isalpha()
if num_or_space and lenght<=12:
    print("validation is completed")
elif num_or_space == False:
    print("your name should not contains space of number!, try again")