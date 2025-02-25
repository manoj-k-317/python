#this file exixts in sub branch

import random
opn = ("rock", "paper", "scissors")
#system_opn = random.choice(opn)
user_opn = (input("enter your option: ")).lower()

score = 0

while True:
    system_opn = random.choice(opn)

    while user_opn not in opn:
        user_opn = (input("pls enter a valid option: ")).lower()
        break

    if user_opn == "q":
        print("game quit")
        break

    print(f"user's choice is {user_opn}")
    print(f"system's choice is {system_opn}")
    
    if user_opn == "rock" and system_opn == "rock":
        print("--- DRAW ---")
        user_opn = (input("playing again! enter your option: ")).lower()
    elif user_opn == "paper" and system_opn == "paper":
        print("--- DRAW ---")
        user_opn = (input("playing again! enter your option: ")).lower()
    elif user_opn == "scissors" and system_opn == "scissors":
        print("--- DRAW ---")
        user_opn = (input("playing again! enter your option: ")).lower()
    elif user_opn == "rock" and system_opn == "paper":
        print("--- USER WON ---")
        user_opn = (input("playing again! enter your option: ")).lower()
    elif user_opn == "rock" and system_opn == "scissors":
        print("--- USER WON ---")
        user_opn = (input("playing again! enter your option: ")).lower()
    elif user_opn == "paper" and system_opn == "rock":
        print("--- SYSTEM WON ---")
        user_opn = (input("playing again! enter your option: ")).lower()
    elif user_opn == "paper" and system_opn == "scissors":
        print("--- SYSTEM WON ---")
        user_opn = (input("playing again! enter your option: ")).lower()
    elif user_opn == "scissors" and system_opn == "rock":
        print("--- SYSTEM WON ---")
        user_opn = (input("playing again! enter your option: ")).lower()
    elif user_opn == "scissors" and system_opn == "paper":
        print("--- USER WON ---")
        user_opn = (input("playing again! enter your option: ")).lower()

