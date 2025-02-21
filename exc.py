#this file exixts in sub branch

unit = input("kilograms of grams (kg or g)?: ")

if unit == "kg":
    print("coverting grams to kilograms")
    weight = float(input("Enter your wight in grams: "))
    result = weight / 1000
    print(f"{result} kilograms")

elif unit == "g":
    print("coverting kilograms to grams")
    weight = float(input("Enter your wight in grams: "))
    result = weight * 1000
    print(f"{result} grams")