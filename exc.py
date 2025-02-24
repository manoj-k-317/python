#this file exixts in sub branch

foods = []
prices = []
total = 0

while True:
    food = input("enter a food to buy: ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of the {food}: "))
        foods.append(food) 
        prices.append(price)

print("--------YOUR CART IS READY --------")
for food in foods:
    print(food, end=" ")
for price in prices:
    total += price
print()
print(total)