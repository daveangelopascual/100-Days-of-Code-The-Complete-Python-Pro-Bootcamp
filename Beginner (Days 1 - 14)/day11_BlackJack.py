import random
def clear():
    print("\n"*20)

def logo():
    print('''
.------.------.------.------. _     _            _     _            _    .------.------.------.------.
|A_  _ |K /\  |Q _   |J .   || |   | |          | |   (_)          | |   |J_  _ |Q /\  |K _   |A .   |
|( \/ )| /  \ | ( )  | / \  || |__ | | __ _  ___| | __ _  __ _  ___| | __|( \/ )| /  \ | ( )  | / \  |
| \  / | \  / |(_x_) |(_,_) || '_ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /| \  / | \  / |(_x_) |(_,_) |
|  \/ A|  \/ K|  Y  Q|  I  J|| |_) | | (_| | (__|   < | | (_| | (__|   < |  \/ J|  \/ Q|  Y  K|  I  A|
`------^------'------'------'|_.__/|_|\__,_|\___|_|\_\| |\__,_|\___|_|\_|`------^------'------'------'
                                                     _/ |     
                                                    |__/ 
          ''')

def dealCard():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return cards[random.randint(0,12)]

def printHands(player, dealer, dealerTurn):
    if dealerTurn == False:
        print(f"\nYour Hand: {player} Your Score: {sum(player)}")
        print(f"Dealer's First Card: {dealer[0]}\n")
    else:
        print(f"\nYour Hand: {player} Your Score: {sum(player)}")
        print(f"Dealer's Hand: {dealer} Dealer's Score: {sum(dealer)}\n")

def blackjack():
    playerHand = []
    dealerHand = []

    for cards in range(2):
        playerHand.append(dealCard())
        dealerHand.append(dealCard())

    dealerTurn = False
    printHands(playerHand,dealerHand, dealerTurn)
    
    if sum(playerHand) == 21:
        print("\nYou got BLACKJACK!")
        choice = 's'
    else:
        choice = input("Type 'h' to Hit, or 's' to Stand: ")
        
    while choice != 'h' and choice != 's':
        choice = input("Sorry not a vaild input. Type 'h' to Hit, or 's' to Stand: ")

    playerBust = False
    while choice == 'h' and playerBust == False:
        playerHand.append(dealCard())
        printHands(playerHand,dealerHand,dealerTurn)
        
        if sum(playerHand) > 21:
            print("Sorry, You busted!")
            playerBust = True
        elif sum(playerHand) == 21:
            print("\nYou got BLACKJACK!")
            choice = 's'
        else:
            choice = input("Type 'h' to Hit, or 's' to Stand: ")
        

    dealerTurn = True
    numHits = 0
    if playerBust == False:
        while sum(dealerHand) < 17:
            dealerHand.append(dealCard())

        printHands(playerHand,dealerHand,dealerTurn)

        if sum(dealerHand) == 21:
            print("Dealer got BLACKJACK!")

        if sum(dealerHand) > 21:
            print("Dealer busted. You Win!")
        elif sum(dealerHand) == sum(playerHand):
            print("It's a push!")
        elif sum(dealerHand) > sum(playerHand):
            print("Dealer Wins!")
        elif sum(dealerHand) < sum(playerHand):
            print("You Win!")
    else:
        printHands(playerHand,dealerHand,dealerTurn)
        

"""Body"""
choice = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
while choice != 'y' and choice != 'n':
        choice = input("Sorry not a vaild input. Type 'y' or 'no': ")
while choice == 'y':
    clear()
    logo()
    blackjack()
    choice = input("Do you want to play another game of blackjack? Type 'y' or 'n': ")

clear()




                                                  
