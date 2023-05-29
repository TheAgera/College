# Design a class named AutomobileLoan that holds a loan number, make and model of automobile, and balance.
# Include methods to set values for each data field and a method that displays all the loan information.
# Create the class diagram and write the pseudocode that defines the class.

# The class has three variables that represent the loan information. The four methods are are called in the while True loop, the methods are populated with the inputs entered there.
class AutomobileLoan:
    def __init__(customer):
        customer.loan_number = ""
        customer.make_and_model = ""
        customer.loan_balance = 0.0

    def set_loan_number(customer, loan_number):
        customer.loan_number = loan_number

    def set_make_and_model(customer, make_and_model):
        customer.make_and_model = make_and_model

    def set_loan_balance(customer, loan_balance):
        customer.loan_balance = loan_balance

    def display_loan_info(customer):
        print("Loan Number:", customer.loan_number)
        print("Make and Model:", customer.make_and_model)
        print("Balance:", customer.loan_balance)

while True:
    # This variable calls the automobile class, so the inputs can be applied.
    loan = AutomobileLoan()

    # Prompts the user for loan information
    loan_number = input("Enter the loan number: ")
    make_and_model = input("Enter the make and model of the automobile: ")
    loan_balance = float(input("Enter the loan balance: "))

    # This sets the values for loan information
    loan.set_loan_number(loan_number)
    loan.set_make_and_model(make_and_model)
    loan.set_loan_balance(loan_balance)

    # Displays the loan information
    loan.display_loan_info()

    # Prompt to ask if user wants to calculate another loan or stop the program
    another_loan = input("Do you want to see another loan? (yes/no): ")
    if another_loan.lower() != "yes":
        break