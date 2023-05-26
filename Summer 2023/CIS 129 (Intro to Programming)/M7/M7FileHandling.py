# The Apgar Medical group keeps a patient file for each doctor in the office. 
# Each record contains the patient’s first and last name, home address, and birth year.
# The records are sorted in ascending birth year order. Two doctors, Dr. Best and Dr. Cushing, have formed a partnership.
# Create the flowchart and pseudocode that produces a merged list of patients’ names in ascending order by birth year.

import csv

def add_to_csv(filename, name, address, birth_year):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, address, birth_year])

def create_sorted_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        sorted_data = sorted(reader, key=lambda row: int(row[2]))

    with open('sorted_' + filename, 'w', newline='') as sorted_csvfile:
        writer = csv.writer(sorted_csvfile)
        writer.writerows(sorted_data)

# Example usage
filename = input("Please enter the filename for sorted patients: ")

while True:
    name = input("Enter name (or 'quit' to exit): ")
    if name.lower() == 'quit':
        break

    address = input("Enter home address: ")
    birth_year = input("Enter birth year: ")

    add_to_csv(filename, name, address, birth_year)

create_sorted_csv(filename)
