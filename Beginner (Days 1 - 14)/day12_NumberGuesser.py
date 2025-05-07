import random

def logo():
    print('''
  _   _                 _                  _____                               
 | \ | |               | |                / ____|                              
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___  ___ _ __ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __|/ _ \ '__|
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \  __/ |   
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/\___|_|   
                                                                               
''')

"""Main"""
lowerNum = 1
upperNum = 100
logo()
print("Welcome to the Number Guessing Game!")
print(f"I am thinking of a number between {lowerNum} and {upperNum}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

while difficulty != 'easy' and difficulty != 'hard':
    difficulty = input("Invalid entry! Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

secretNum = random.randint(1,100)
userGuess = -1
while userGuess != secretNum and attempts > 0:
    print("\n")
    if attempts > 1:
        print(f"The number is now in range of [{lowerNum},{upperNum}]. You have {attempts} lives left.")
    else:
        print(f"The number is now in range of [{lowerNum},{upperNum}]. You have {attempts} life left.")
    
    userGuess = int(input("Make a Guess: "))
    attempts -= 1

    if userGuess > secretNum and attempts > 0:
        print("Too High! \nGuess Again.")
        if upperNum > userGuess:
            upperNum = userGuess - 1
    elif userGuess < secretNum and attempts > 0:
        print("Too Low! \nGuess Again.")
        if lowerNum < userGuess:
            lowerNum = userGuess + 1
    elif userGuess == secretNum:
        print("Yay! You correctly guess the number!")
    else:
        print(f"Sorry out of attempts! The number was {secretNum}.")

        