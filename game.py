import random

userChoice = str(input("Choose Rock, Paper or Scissors: ")).lower()
randomChoice = random.choice(["Rock", "Paper", "Scissors"]).lower()

if userChoice == "rock" and randomChoice == "paper":
    print(f"You chose {userChoice} and the other user chose {randomChoice}")
    print(f"You Lost!")
elif userChoice == "scissors" and randomChoice == "rock":
    print(f"You chose {userChoice} and the other user chose {randomChoice}")
    print(f"You Lost!")
elif userChoice == "paper" and randomChoice == "scissors":
    print(f"You chose {userChoice} and the other user chose {randomChoice}")
    print(f"You Lost!")
elif userChoice == randomChoice:
    print(f"You chose {userChoice} and the other user chose {randomChoice}")
    print(f"It's a Tie!")
else:
    print(f"You chose {userChoice} and the other user chose {randomChoice}")
    print(f"You Won!")
