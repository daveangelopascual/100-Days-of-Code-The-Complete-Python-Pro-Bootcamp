def logo():
    print('''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
          ''')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Undefined"
    else:
        return x / y

def printOperations():
    print("+\n-\n*\n\\")

def printEquation(x, y, operation, answer):
    print(f"{x} {operation} {y} = {answer}")



def main():
    logo()
    input1 = float(input("What is the first number?: "))
    moreComputations = "y"
    while moreComputations == "y":
        printOperations()
        operations = {
            '+' : add,
            '-' : subtract,
            '*' : multiply,
            '\\' : divide,
        }
        operation = input("Pick an operation: ")
        calculate = operations[operation]
        input2 = float(input("What is the next number?: "))
        
        result = calculate(input1, input2)
        printEquation(input1, input2, operation, result)
    
        if result =="Undefined":
            moreComputations = "n"
        else:
            moreComputations = input(f"Type 'y' to continue with {result} or 'n' to start a new calculation: ")
            input1 = result
            if moreComputations == "n":
                print("\n"*20)
                main()

main()