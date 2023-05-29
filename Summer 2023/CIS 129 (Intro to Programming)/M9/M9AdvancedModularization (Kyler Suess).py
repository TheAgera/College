# Create the flowchart and pseudocode for a program that accepts a user’s birth month and year
# and passes them to a method that calculates the user’s age in the current month 
# and returns the value to the main program to be displayed.

# Built in python module that can grab the current date, along with assiting in calculations
# See the documentation for more information ---> https://docs.python.org/3/library/datetime.html
import datetime

# Function to grab the current date, and then calculate age_in_months
def calculate_age_in_months(birth_month, birth_year):
    current_date = datetime.datetime.now().date()
    birth_date = datetime.date(birth_year, birth_month, 1)
    
    age_in_months = (current_date.year - birth_date.year) * 12 + (current_date.month - birth_date.month)
    
    return age_in_months

# Main logic of the program, ask for user input for birth month and year. The calculation module
# is called once the inputs are accepted.
def main():
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_year = int(input("Enter your birth year (YYYY): "))
    
    age_in_months = calculate_age_in_months(birth_month, birth_year)
    
    print("Your age in months is:", age_in_months)

# Ensures the main function is only ran once the program is started.
main()
