import random
import re
import csv

def generate_account_number(name, purchase_price):
    name = name.lower().replace(" ", "")  # Convert name to lowercase and remove spaces
    random_number = random.randint(1000, 9999)  # Generate a random 4-digit number
    account_number = name[:3] + str(random_number) + str(int(purchase_price))
    return account_number

def calculate_monthly_payment(purchase_price):
    return purchase_price / 12

def validate_name(name):
    if not re.match("^[a-zA-Z ]+$", name):
        print("Invalid name. Please enter only alphabetical characters and spaces.")
        return False
    return True

def validate_price(price):
    if not re.match("^\d+(\.\d+)?$", price):
        print("Invalid price. Please enter a numeric value.")
        return False
    return True

def process_customer():
    customer_name = input("Enter customer name (or enter 'quit' to exit): ")

    if customer_name.lower() == "quit":
        return False

    if not validate_name(customer_name):
        return True

    while True:
        purchase_price = input("Enter purchase price: ")

        if validate_price(purchase_price):
            break

    purchase_price = float(purchase_price)

    account_number = generate_account_number(customer_name, purchase_price)

    print("Account Number:", account_number)
    print("Customer Name:", customer_name)

    monthly_payment = calculate_monthly_payment(purchase_price)
    print("Monthly Payments for the next 12 months:")

    for month in range(1, 13):
        print("Month {}: ${:.2f}".format(month, monthly_payment))

    print()

    # Write customer information to CSV file
    with open("customer_data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([account_number, customer_name, purchase_price])

    return True

def main():
    with open("customer_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Account Number", "Customer Name", "Purchase Price"])

    while True:
        if not process_customer():
            break

if __name__ == "__main__":
    main()

