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
filename = 'data.csv'

while True:
    name = input("Enter name (or 'quit' to exit): ")
    if name.lower() == 'quit':
        break

    address = input("Enter home address: ")
    birth_year = input("Enter birth year: ")

    add_to_csv(filename, name, address, birth_year)

create_sorted_csv(filename)
