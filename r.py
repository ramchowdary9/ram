import random
import sys
#create a list of play options
t = ["rock","paper","scissors"]

#assign a random play to the computer
computer = random.choice(t)

#set player to False


while True:
#set player to True
    player = input("Rock, Paper, Scissors?")
    player=player.lower()
    print("computer choosed",computer)
    print("player choosed",player)
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    if player=="q":
        print("thank u for playing with me")
        sys.exit()
    
    
