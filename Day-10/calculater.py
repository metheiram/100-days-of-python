calculator = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''

print(calculator)

# Define operations as functions
def add(n1, n2):
    return n1 + n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2

def sub(n1, n2):
    return n1 - n2

# Create a dictionary of operations
dictionary = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mul
}

# Initial calculation
f_no = float(input("Write your first number: "))

while True:
    print("Available operations: +, -, *, /")
    op = input("Select the mathematical operation: ")
    
    if op in dictionary:
        s_no = float(input("Write your second number: "))
        ans = dictionary[op](f_no, s_no)  # Call the operation function
        
        print(f"{f_no} {op} {s_no} = {ans}")
        
        # Ask user if they want to continue using the result or start a new calculation
        choice = input(f"Type 'y' to continue calculating with the {ans} or type 'n' to start a new calculation: ").lower()
        
        if choice == "y":
            f_no = ans  # Continue with the result
        elif choice == "n":
            f_no = float(input("Write your first number: "))  # Start a new calculation
        else:
            print("Invalid choice. Please type 'y' or 'n'.")
    else:
        print("Invalid operation. Please choose a valid operator: +, -, *, /.")
