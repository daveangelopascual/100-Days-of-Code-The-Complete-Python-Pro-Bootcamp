import random

rock = """
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)"""
    
paper = """
            _______
        ---'    ____)_
                ______)
                _______)
                _______)
        ---.__________)"""

scissors = """
            _______
        ---'   ____)__
                ______)
            __________)
            (____)
        ---.__(___)"""

print("Let's play Rock Paper Scissor! Can you beat the computer?")
user = int(input("Type 1 for Rock, 2 for Paper, 3 for Scissors: "))

computer = random.randint(1,3)

if user == 1:
    print("\n       You chose Rock!")
    print(rock)
    
elif user == 2:
    print("\n       You chose Paper!")
    print(paper)

elif user == 3:
    print("\n       You chose Scissors!")
    print(scissors)


if computer == 1:
    print("\n       The CPU chose Rock!")
    print(rock)
    
elif computer == 2:
    print("\n       The CPU chose Paper!")
    print(paper)

elif computer == 3:
    print("\n       The CPU chose Scissors!")
    print(scissors)

if computer == user:
    print("\n       It's a Draw!")

elif (computer == 1 and user == 2) or (computer == 2 and user == 1):
    print("\n       Paper beats Rock!")
    if computer == 2:
        print("The computer wins!")
    elif user == 2:
        print("You beat the computer!")

elif (computer == 1 and user == 3) or (computer == 3 and user == 1):
    print("\n       Rock beats Scissors!")
    if computer == 1:
        print("The computer wins!")
    elif user == 1:
        print("You beat the computer!")

elif (computer == 2 and user == 3) or (computer == 3 and user == 2):
    print("\n       Scissors beats Paper!")
    if computer == 3:
        print("The computer wins!")
    elif user == 3:
        print("You beat the computer!")