import datetime

def calculate_age_in_months(birth_month, birth_year):
    current_date = datetime.datetime.now().date()
    birth_date = datetime.date(birth_year, birth_month, 1)
    
    age_in_months = (current_date.year - birth_date.year) * 12 + (current_date.month - birth_date.month)
    
    return age_in_months

def main():
    birth_month = int(input("Enter your birth month: "))
    birth_year = int(input("Enter your birth year: "))
    
    age_in_months = calculate_age_in_months(birth_month, birth_year)
    
    print("Your age in months is:", age_in_months)

main()
