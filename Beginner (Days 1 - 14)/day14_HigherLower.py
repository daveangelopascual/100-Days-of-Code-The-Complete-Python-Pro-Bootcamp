import random
import day13_HigherLower_GameData

def title():
    print('''
        _       _                
  /\  /(_) __ _| |__   ___ _ __   
 / /_/ / |/ _` | '_ \ / _ \ '__| __                        
/ __  /| | (_| | | | |  __/ |   / /  _____      _____ _ __ 
\/ /_/ |_|\__, |_| |_|\___|_|  / /  / _ \ \ /\ / / _ \ '__| 
          |___/               / /__| (_) \ V  V /  __/ |   
                              \____/\___/ \_/\_/ \___|_|                                
    ''')

def vs():
    print('''
__   _____   
\ \ / / __|  
 \ V /\__ \_ 
  \_/ |___(_)
             
    ''')

def clear():
    print("\n"*20)

dataSet = day13_HigherLower_GameData.data

def validateAns(guess, choiceA, choiceB):
    if choiceA['follower_count'] > choiceB['follower_count']:
        validAns = 'a'
    else:
        validAns = 'b'
    
    if guess == validAns:
        return True
    else:
        return False
    
def game():
    streak = 0
    validGame = True
    optionA = random.choice(dataSet)
    optionB = random.choice(dataSet)
    while optionA == optionB:
        optionB = random.choice(dataSet)

    while validGame == True:
        clear()
        title()
        if streak != 0:
            optionA = optionB
            optionB = random.choice(dataSet)
            while optionA == optionB:
                optionB = random.choice(dataSet)
            print(f"Correct! Current Streak: {streak}")
        
        print(f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}")
        vs()
        print(f"Against B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}")
        
        userAns = input("Who has more followers? Type 'a' or 'b': ")
        while userAns != 'a' and userAns != 'b':
            userAns = input("Invalid Input! Type 'a' or 'b': ")

        validGame = validateAns(userAns, optionA, optionB)
        if validGame == False:
            clear()
            title()
            print(f"Incorrect! Gameover! Final Score: {streak}")
        else:
            streak += 1

"""Main"""
choice = input("Ready to Play? Type 'y' or 'n': ")
while choice != 'y' and choice != 'n':
    choice = input("Invalid Input! Type 'y' or 'n': ")
    
clear()
if choice == 'y':
    game()