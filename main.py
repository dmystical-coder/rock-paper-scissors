# Import modules
import random
import time

# Store all possible options
option = {
    "R":"Rock",
    "P":"Paper",
    "S":"Scissors",
}

#gameplay
def play():
    #validate user input
    # ask the user to pick an option between "R", "P" or "S"
    user = input("What do you choose? Type 'R' for Rock, 'P' for Paper or 'S' for Scissors.\n").upper()

    while user not in option:
        print("You haven't entered the right option.\nPlease, Try again!")
        user = input("What do you choose? Type 'R' for Rock, 'P' for Paper or 'S' for Scissors : ")
        
    # Make a choice for the CPU (computer player)
    choose = ["R", "S", "P"]
    computer = random.choice(choose)

    # Print both player's moves in the format: `Player (Rock) : CPU (Paper)`
    print(f"Player ({option[user]}) : CPU ({option[computer]})")

    # Check both player's moves and decide winner
    if user == "R":
        if computer == "R":
            print("There is a tie!")
            play()
        elif computer == "P":
            print("Computer wins!")
        else:
            print("You win!")
    elif user == "P":
        if computer == "R":
            print("You win!")
        elif computer == "P":
            print("There is a tie!")
            play()
        else:
            print("Computer wins!")
    elif user == "S":
        if computer == "R":
            print("Computer wins")
        elif computer == "P":
            print("You win!")
        else:
            print("There is a tie!")
            play()
    else:
        pass

# Welcome Message
print("Welcome to the Rock-Paper-Scissors game.")
time.sleep(3)
print('''Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules. ''')
time.sleep(3)
print("The Rules: \nRock beats Scissors\nPaper beats Rock\nScissors beats Paper")
time.sleep(3)
play()
