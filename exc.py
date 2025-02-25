#this file exists in main branch
import random

guess = int(input("enter a number from 1 to 10: "))
print(f"your guess is -> {guess}")
start = 1
end = 10
result = random.randint(start, end)
print(f"the result is -> {result}")


while True:
    if guess > result:
        print(f"your guess -> {guess} and our result -> {result}")
        print("your guess if bigger than the result")
        guess = int(input("enter a number from 1 to 10: "))
    elif guess < result:
        print(f"your guess -> {guess} and our result -> {result}")
        print("your guess is smaller than the result")
        guess = int(input("enter a number from 1 to 10: "))
    elif guess == result:
        print(f"your guess -> {guess} and our result -> {result}")
        print("wow, your guess is perfect")
        break
