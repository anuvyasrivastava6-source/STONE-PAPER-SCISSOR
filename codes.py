import random

choices = ["stone", "paper", "scissor"]
user = input("Enter stone, paper or scissor: ").lower()
comp = random.choice(choices)

print("Computer chose:", comp)

if user == comp:
    print("It's a tie!")
elif (user == "stone" and comp == "scissor") or \
     (user == "paper" and comp == "stone") or \
     (user == "scissor" and comp == "paper"):
    print("You win!")
else:
    print("You lose!")