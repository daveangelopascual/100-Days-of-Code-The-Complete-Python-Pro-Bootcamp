print("Welcome to the tip calculator!")
totalAmt = float(input("What was the total bill? $"))
tipPercent = float(input("What percentage tip would you like to give? 15, 18, or 20? ")) + 100
tipPercent /= 100
totalAmt *= tipPercent
numPeople = int(input("How many people to split the bill? "))
shareAmt = totalAmt / numPeople

print(f"Each person will pay ${round(shareAmt,2)}")