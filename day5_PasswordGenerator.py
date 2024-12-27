import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
numLetters = int(input("How many letters would you like in your password?\n"))
numSymbols = int(input("How many symbols would you like in your password?\n"))
numNumbers = int(input("How many numbers would you like in your password?\n"))

passwordLen = numLetters + numSymbols + numNumbers
password = ""

for iteration in range(0, passwordLen):
    decision = random.randint(1,3)
    
    if numLetters == 0 and numNumbers == 0 and numSymbols == 0:
        decision = 4
    elif numLetters == 0 and numNumbers == 0:
        decision = 3
    elif numLetters == 0 and numSymbols == 0:
        decision = 2
    elif numNumbers == 0 and numSymbols == 0:
        decision = 1
    elif decision == 1 and numLetters == 0:
        decision = random.randint(2,3)
    elif decision == 3 and numSymbols == 0:
        decision = random.randint(1,2)
    elif decision == 2 and numNumbers == 0:
        decision = random.randint(1,2)
        if decision == 2:
            decision += 1

    if numLetters > 0 and decision == 1:
        password += letters[random.randint(0,51)]
        numLetters -= 1

    elif numNumbers > 0 and decision == 2:
        password += numbers[random.randint(0,9)]
        numNumbers -= 1

    elif numSymbols > 0 and decision == 3:
        password += symbols[random.randint(0,7)]
        numSymbols -= 1

print("Here is your password: " + password)