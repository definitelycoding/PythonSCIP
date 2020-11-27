"""
Hello, this is a mathematical program which calculates addition, subtraction, division, multiplication and
remainder/modulus.
It only takes 2 numbers from the user.
It is a naive program in the sense that it assumes that the user will comply to what is being asked, i.e
inputting text or numbers where required and nothing else.
"""

# In the main method I used an if, elif and else statement so that the user has a variety of options.
# I have used a variable "choice" as a way to connect the user to the program, add -> num_add().
# The program will find the code block to execute the chosen command word from the user.


def main():
    print("-------------------------------------------------------------------------------------------")
    print("Please choose one function between these to begin: add, subtract, divide, multiply, modulus")

    choice = input("Enter the function you want to use: ")
    choice = str(choice)

    if choice == "add":
        num_add()
    elif choice == "subtract":
        num_subtract()
    elif choice == "divide":
        num_divide()
    elif choice == "multiply":
        num_multiply()
    else:
        num_modulus()

# This function asks the user for 2 numbers and prints their total.


def num_add():
    num1 = input("Enter first number here: ")
    num1 = int(num1)
    num2 = input("Enter second number here: ")
    num2 = int(num2)
    total = num1 + num2
    print("The total is: " + str(total) + ".")


# This function asks the user for 2 numbers and prints their subtraction.


def num_subtract():
    num1 = input("Enter first number here: ")
    num1 = int(num1)
    num2 = input("Enter second number here: ")
    num2 = int(num2)
    sub_result = num1 - num2
    print("The subtraction is: " + str(sub_result) + ".")


# This function asks the user for 2 numbers and prints their division.


def num_divide():
    num1 = input("Enter first number here: ")
    num1 = int(num1)
    num2 = input("Enter second number here: ")
    num2 = int(num2)
    div_result = num1 / num2
    print("The division is: " + str(div_result) + ".")

# This function asks the user for 2 numbers and prints their multiplication.


def num_multiply():
    num1 = input("Enter first number here: ")
    num1 = int(num1)
    num2 = input("Enter second number here: ")
    num2 = int(num2)
    mul_result = num1 * num2
    print("The multiplication is: " + str(mul_result) + ".")


# This function asks the user for 2 numbers and prints their modulus.


def num_modulus():
    num1 = input("Enter first number here: ")
    num1 = int(num1)
    num2 = input("Enter second number here: ")
    num2 = int(num2)
    mod_result = num1 % num2
    print("The modulus/remainder is: " + str(mod_result) + ".")




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()


