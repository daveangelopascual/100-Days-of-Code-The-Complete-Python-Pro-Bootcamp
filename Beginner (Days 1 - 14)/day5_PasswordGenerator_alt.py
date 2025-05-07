import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
numLetters = int(input("How many letters would you like in your password?\n"))
numSymbols = int(input("How many symbols would you like in your password?\n"))
numNumbers = int(input("How many numbers would you like in your password?\n"))

passwordList = []

for iteration in range(0, numLetters):
    passwordList.append(letters[random.randint(0,51)])

for iteration in range(0, numNumbers):
    passwordList.append(numbers[random.randint(0,9)])

for iteration in range(0, numSymbols):
    passwordList.append(symbols[random.randint(0,7)])

random.shuffle(passwordList)

password = ""
for char in passwordList:
    password += char

print(f"Here is your password: {password}")