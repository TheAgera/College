# The Apgar Medical group keeps a patient file for each doctor in the office. 
# Each record contains the patient’s first and last name, home address, and birth year.
# The records are sorted in ascending birth year order. Two doctors, Dr. Best and Dr. Cushing, have formed a partnership.
# Create the flowchart and pseudocode that produces a merged list of patients’ names in ascending order by birth year.

import csv

# Takes data, name, address, and birth_year as parameters
def add_to_list(data, name, address, birth_year):
    data.append([name, address, birth_year])

# Uses the lambda function built into python to sort the data . View documentation here ---> https://docs.python.org/3/howto/sorting.html
def create_sorted_csv(data, filename):
    sorted_data = sorted(data, key=lambda row: int(row[2]))

    # Creates new CSV file and stores the sorted_data as inputs. The 'w' stands for write mode.
    with open(filename, 'w', newline='') as sorted_csvfile:
        writer = csv.writer(sorted_csvfile)
        writer.writerows(sorted_data)

# Creates an empty array so it can be filled with data from module add_to_list
data = []

# This loop will continously add to the variables, that will be fed into def add_to_list. Loop will break if user enters 'quit' for the patient name
while True:
    name = input("Enter name (or 'quit' to exit): ")
    if name.lower() == 'quit':
        break

    address = input("Enter home address: ")
    birth_year = input("Enter birth year: ")

    add_to_list(data, name, address, birth_year)

filename = input("Please enter the filename for sorted patients: ")

create_sorted_csv(data, filename + '.csv')
