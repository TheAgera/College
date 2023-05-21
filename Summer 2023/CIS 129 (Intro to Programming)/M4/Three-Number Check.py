def check_sum(numbers):
    a, b, c = numbers
    
    if a + b == c:
        print(f"{a} + {b} = {c}")
    elif b + c == a:
        print(f"{b} + {c} = {a}")
    elif c + a == b:
        print(f"{c} + {a} = {b}")
    else:
        print("No pair of numbers sums up to the third.")

# Accept input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the check_sum function with the input numbers
check_sum([num1, num2, num3])