#this file exixts in sub branch
# ●  ┌  ─  ┐  │  └  ┘
import random
"-----------"
"|         |"
"|         |"
"|         |"
"-----------"

die_art = {1:("-----------",
              "|         |",
              "|    1    |",
              "|         |",
              "-----------"),
            2:("-----------",
               "|2        |",
               "|         |",
               "|        2|",
               "-----------"),
            3:("-----------",
              "|3        |",
              "|    3    |",
              "|        3|",
              "-----------"),
            4:("-----------",
               "|4       4|",
               "|         |",
               "|4       4|",
               "-----------"),
            5:("-----------",
               "|5       5|",
               "|    5    |",
               "|5       5|",
               "-----------"),
            6:("-----------",
               "|6       6|",
               "|6       6|",
               "|6       6|",
               "-----------")}

dice = []
num_dice = int(input("enter the amount of dice: "))
total = 0
for die in range(num_dice):
    dice.append(random.randint(1,6))
print(dice)

if dice == 1:
    print("-----------",
          "|         |",
          "|    1    |",
          "|         |",
          "-----------")
for die in dice:
    total += die
print(total)