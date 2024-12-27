print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go?")
decisionA = input("      Type \"left\" or \"right\"\n")
if decisionA == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    decisionB = input(" Type \"swim\" to swim across. Type \"wait\" to wait for a boat.\n")
    if decisionB == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        decisionC = input("One red, one yellow and one blue. Which color do you choose?\n")
        
        if decisionC == "yellow":
            print("Congrats! You found the treasure!")
        
        elif decisionC == "red":
            print("Oh! You were burnt to a crisp")
            print("GAMEOVER")
        
        elif decisionC == "blue":
            print("You were eaten by beasts!")
            print("GAMEOVER")
        
        else:
            print("GAMEOVER")

    else:
        print("Oh No! You were attacked by a trout.")
        print("GAMEOVER")

else:
    print("Yikes! You fell into a hole.")
    print("GAMEOVER")