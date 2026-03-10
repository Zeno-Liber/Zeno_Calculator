# Greeting message so user knows program is running
print("Starting program...")

# Function definitions to perform arithmetic
def addition(a, b):
    print(a + b)

def subtraction(a, b):
    print(a - b)

def multiplication(a, b):
    print(a * b)

def division(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
    else:
        print(a /b)

# Loop to keep the program prompting the user until selecting the exit option
while True:

    # Two variables to be used for arguments for arithmetic functions
    num1 = int(input("First number to operate on?: "))
    num2 = int(input("Second number to operate on?: "))

    # Displaying a list of options for the user to select from
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit the program
    """)

    # Prompting the user to select from the list of options before
    choice = int(input("Select an option 1 - 5:  "))

    # Control flow to match the choice from before to the appropriate arithmetic function with error handling
    if choice == 1:
        addition(num1, num2)
        continue
    elif choice == 2:
        subtraction(num1, num2)
        continue
    elif choice == 3:
        multiplication(num1, num2)
        continue
    elif choice == 4:
        division(num1, num2)
        continue
    elif choice == 5:
        break
    else:
        print("Error: Invalid selection, please try again.")


