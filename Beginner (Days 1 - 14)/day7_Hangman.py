import random
logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/'''
def hangmanArt(lives):
    if lives == 6:
        print(''' 
     __________
     |/      
     |      
     |      
     |       
     |      
     |
 ____|___''')
    elif lives == 5:
        print(''' 
     __________
     |/      |
     |      
     |      
     |      
     |      
     |
 ____|___''')
    elif lives == 4:
        print(''' 
     __________
     |/      |
     |      (_)
     |       
     |       
     |      
     |
 ____|___''')
    elif lives == 3:
        print(''' 
     __________
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 ____|___''')
    elif lives == 2:
        print(''' 
     __________
     |/      |
     |      (_)
     |      \\|/
     |       
     |      
     |
 ____|___''')
    elif lives == 1:
        print(''' 
     __________
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      
     |
 ____|___''')
    elif lives == 0:
        print(''' 
     __________
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      / \\
     |
 ____|___''')

wordList = ["apple", "banana", "kiwi", "dragonfruit", "avocado", "peach", "strawberry", "grape", "orange", "nectarine", "cantaloupe", "honeydew", "mango"]

chosenWord = random.choice(wordList)

placeholder = ""
for char in chosenWord:
    placeholder += "_"
print(logo)
print(placeholder)

tries = 6
guesses = ""
hangmanArt(tries)
while placeholder != chosenWord and tries > 0:
    if guesses != "":
        hangmanArt(tries)
        print(f"\nRemaining Guesses: {tries}")
        print(f"Already Guessed: {guesses}")

    guess = (input("Please enter a guess: ")).lower()

    display = ""
    for index in range(0,len(chosenWord)):
        if chosenWord[index] == guess:
            display += guess
        elif placeholder[index] != "_": 
            display += placeholder[index]
        else:
            display += "_"

    guesses += guess + " "
    if placeholder == display:
        tries -= 1
    else:
        placeholder = display
    print(display)
    

    if placeholder == chosenWord:
        print ("\nYay! You Guessed the Word!")
    elif tries == 0:
        hangmanArt(tries)
        print(f"\nSorry out of tries! The word was {chosenWord}!")
        print("GAMEOVER")