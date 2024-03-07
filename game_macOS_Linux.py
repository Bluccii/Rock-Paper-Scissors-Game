import random
import os
import time

userWinCount = 0
computerWinCount = 0
tieCount = 0
roundCount = 1
numOfRounds = int(input("How many rounds would you like to play? (Enter a number): "))
os.system('clear')

while roundCount != (numOfRounds + 1): 
    print(f"------------------------------------------------")
    print(f"This is the start of round {roundCount}!")
    print(f"User has {userWinCount} Wins, and Computer has {computerWinCount} Wins!")

    userChoice = str(input("Choose Rock, Paper or Scissors: ")).lower()
    randomChoice = random.choice(["Rock", "Paper", "Scissors"]).lower()

    if userChoice == "rock" and randomChoice == "paper":
        print(f"You chose {userChoice} and the other user chose {randomChoice}")
        print(f"You Lost!")
        print(f"------------------------------------------------")
        time.sleep(5)
        os.system('clear')
        computerWinCount += 1
    elif userChoice == "scissors" and randomChoice == "rock":
        print(f"You chose {userChoice} and the other user chose {randomChoice}")
        print(f"You Lost!")
        print(f"------------------------------------------------")
        time.sleep(5)
        os.system('clear')
        computerWinCount += 1
    elif userChoice == "paper" and randomChoice == "scissors":
        print(f"You chose {userChoice} and the other user chose {randomChoice}")
        print(f"You Lost!")
        print(f"------------------------------------------------")
        time.sleep(5)
        os.system('clear')
        computerWinCount += 1
    elif userChoice == randomChoice:
        print(f"You chose {userChoice} and the other user chose {randomChoice}")
        print(f"It's a Tie!")
        print(f"------------------------------------------------")
        time.sleep(5)
        os.system('clear')
        tieCount += 1
    else:
        print(f"You chose {userChoice} and the other user chose {randomChoice}")
        print(f"You Won!")
        print(f"------------------------------------------------")
        time.sleep(5)
        os.system('clear')
        userWinCount += 1
    roundCount += 1

print(f"------------------------------------------------")
print(f"The game is over! A total of {roundCount - 1} rounds were played.")
print("")
print(f"STATS:")
print(f"The User finished the game with {userWinCount} Wins!")
print(f"The Computer finished the game with {computerWinCount} Wins!")
print(f"There were {tieCount} Ties")
print(f"------------------------------------------------")