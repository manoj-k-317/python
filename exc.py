#this file exixts in sub branch

questions = ("how many elemnets are present in teyvat?",
             "how many operator classes are availabe in delta force?",
             "what is my highest kill in delta force?",
             "what is the highest damage i hit in genshin?")
options = (("A. 9","B. 7","C. 8","D. 6"),
           ("A. 4","B. 6","C. 5","D. 8"),
           ("A. 100","B. 89","C. 75","D. 68"),
           ("A. 150k","B. 700k","C. 850k", "D. 1m"))
answers = ("B","A","B","B")
guesses = []
score = 0
qnn = 0

for qn in questions:
    print(qn)
    for opn in options[qnn]:
        print(opn)
    guess = input("enter an option [A/B/C/D]: ")
    guesses.append(guess.upper())
    if guess == answers:
        print("correct")
        score += 1
    else:
        print("incorrect")
        print(f"option {answers[qnn]} is the correct answer")
    qnn += 1