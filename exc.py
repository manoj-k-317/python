#this file exixts in sub branch

menu = {"popcorn":160,
        "drinks":190,
        "fries":150,
        "water":60,
        "ice":130,
        "sandwich":130}

cart = []
total = 0
items = menu.items()

print("------ M E N U ------")
for key, value in items:
    print(f"{key:<10} rs:{value}/-")
print("make sure to to type correctly")

while True:
    food = input("type in what you need or press q to quit: ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    elif menu.get(food) is None:
        print(f"sorry, {food} is not availabe")

for food in cart:
    print(food)
    total += menu.get(food)

print()
print(f"your total is {total}")