#shopping cart program

item = str(input("enter what you have purchased: "))
price = float(input("enter the price rate of the product: "))
quantity = int(input("enter the total number of items you have purchased: "))

print(f"you have purchased {quantity} {item}")
print(f"which in total costs {price*quantity}")