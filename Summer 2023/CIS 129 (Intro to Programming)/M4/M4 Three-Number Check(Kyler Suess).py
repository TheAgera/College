 # Draw a flowchart and pseudocode that accepts three numbers from a user and displays a 
 # message if the sum of any two numbers equals the third. Make a working version of this program in Python.

# Calculation function starts after user inputs
def check_sum(numbers):
    # num1, num2, and num3 are bypassed as a parameter to check_sum
    a, b, c = numbers
    
    if a + b == c:
        print("A pair of numbers sums up to the third.")
    else:
        print("The pair of numbers does not sum up to the third.")

# User Input for each number
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the check_sum function with the input numbers
check_sum([num1, num2, num3])