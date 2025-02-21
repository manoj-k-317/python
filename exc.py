#this file exixts in sub branch

operator = input("Pls enter an operator (+ - * / %): ")

if operator == "+":
    print("Addition operation initiated")
    a = int(input("enter value for (a): " ))
    b = int(input("enter value for (b): " ))
    print ("processing addition")
    c = a+b
    print(f"{a} + {b} = {c}")
elif operator == "-":
    print("Subtraction operation initiated")
    a = int(input("enter value for (a): " ))
    b = int(input("enter value for (b): " ))
    print ("processing subtraction")
    if a>b:
        c = a-b
        print(f"{a} - {b} = {c}")
    elif b>a:
        c = b-a
        print(f"{b} - {a} = {c}")
if operator == "*":
    print("Multiplication operation initiated")
    a = int(input("enter value for (a): " ))
    b = int(input("enter value for (b): " ))
    print ("processing multiploication")
    c = a*b
    print(f"{a} * {b} = {c}")
if operator == "/":
    print("Division operation initiated")
    a = int(input("enter value for (a): " ))
    b = int(input("enter value for (b): " ))
    print ("processing multiploication")
    c = a/b
    print(f"{a} / {b} = {c}")
if operator == "%":
    print("Reminder operation initiated")
    a = int(input("enter value for (a): " ))
    b = int(input("enter value for (b): " ))
    print ("processing multiploication")
    c = a%b
    print(f"{a} % {b} = {c}")