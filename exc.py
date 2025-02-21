#this file exixts in sub branch

unit = input("enter your unit pls (c or k or f): ")
temp = float(input("enter your temprature: "))
conversion = input("select the conversion type (c or k or f):")

#c to k
if unit == "c" and conversion == "k":
    converted = round(temp + 273.15, 2)
    print(f"converted your {temp}c to {converted}k")
#k to c
elif unit == "k" and conversion == "c":
    converted = round(temp - 273.15, 2)
    print(f"converted your {temp}k to {converted}c")
#k to f
elif unit == "k" and conversion == "f":
    converted = round((temp - 273.15) * (9/5) + 32 , 2)
    print(f"converted your {temp}k to {converted}f")
#f to k
elif unit == "f" and conversion == "k":
    converted = round((temp - 32) * (5/9) + 273.15 , 2)
    print(f"converted your {temp}f to {converted}k")
#c to f
elif unit == "c" and conversion == "f":
    converted = round((temp *(9/5)) + 32, 2)
    print(f"converted your {temp}c to {converted}f")
#f to c
elif unit == "f" and conversion == "c":
    converted = round((temp - 32) * 5/9, 2)
    print(f"converted your {temp}f to {converted}c")