print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
      ''')

print("Welcome to the secret auction program!")
moreBids = "yes"
bids = {}
while moreBids == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    moreBids = input("Are there any more bidders? Type 'yes' or 'no': ")
    print("\n"*20)

nameMax = ""
maxBid = 0
for name in bids:
    if bids[name] > maxBid:
        maxBid = bids[name]
        nameMax = name

print(f"Congrats {nameMax} holds the final bid of ${bids[nameMax]}")