# import csv
# import time

# # Example CSV data
# input_csv_file = 'iostat.csv'

# # Define column names to calculate averages for
# columns = ['tps', 'kB_read/s', 'kB_wrtn/s', 'kB_dscd/s', 'kB_read', 'kB_wrtn', 'kB_dscd']

# # Define the output file prefix
# output_file_prefix = 'averages_'

# # Define the interval in seconds
# interval = 60

# def calculate_column_averages(data):
#     averages = []
#     for column in columns:
#         values = [float(row[column]) for row in data]
#         average = sum(values) / len(values)
#         averages.append(average)
#     return averages

# def write_averages_to_csv(averages, output_csv_file):
#     with open(output_csv_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(columns)
#         writer.writerow(averages)

# # Read the CSV data
# with open(input_csv_file, 'r') as file:
#     csv_reader = csv.DictReader(file)
#     data = list(csv_reader)

# # Process the data in intervals and write averages to CSV files
# start_time = time.time()
# current_interval = 1

# while True:
#     # Check if the time interval has passed
#     elapsed_time = time.time() - start_time
#     if elapsed_time >= (current_interval * interval):
#         # Calculate averages for the current interval
#         current_data = data[:current_interval]
#         averages = calculate_column_averages(current_data)

#         # Write averages to a new CSV file
#         output_csv_file = f'{output_file_prefix}{current_interval}.csv'
#         write_averages_to_csv(averages, output_csv_file)

#         # Move to the next interval
#         current_interval += 1

#     # Check if all data has been processed
#     if current_interval > len(data):
#         break

#     # Sleep for a short duration to avoid excessive CPU usage
#     time.sleep(1)

# print('Averages calculation and CSV writing completed!')

# import csv

# def read_column(csv_file, column_index):
#     with open(csv_file, 'r') as file:
#         reader = csv.reader(file)
#         column = []
#         for row in reader:
#             if len(row) > column_index:
#                 column.append(row[column_index])
#     return column

# def caclulate_max()
    
# def caclulate_average()
    
# def calculate_count()
    
    


# csv_file = 'iostat.csv'
# column_index = 3  # Read the third column, column one being sda (index 2)

# column = read_column(csv_file, column_index)
# print(column)

import csv

csv_file_path = 'iostat.csv'
num_rows = 60

# Initialize arrays for each column
column_a = []
column_b = []
column_c = []
column_d = []
column_e = []
column_f = []
column_g = []

# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Iterate through each row with row count
    for count, row in enumerate(reader, start=1):
        # Break the loop if the desired number of rows is reached
        if count > num_rows:
            break

        # Assign values to variables based on positions
        for column_index, value in enumerate(row[1:], start=2):
            variable_name = chr(ord('A') + column_index - 2) + str(count)
            globals()[variable_name] = value

            # Store values in respective column arrays
            if column_index == 2:
                column_a.append(value)
            elif column_index == 3:
                column_b.append(value)
            elif column_index == 4:
                column_c.append(value)
            elif column_index == 5:
                column_d.append(value)
            elif column_index == 6:
                column_e.append(value)
            elif column_index == 7:
                column_f.append(value)
            elif column_index == 8:
                column_g.append(value)

# Filter out non-numeric values from column arrays
column_a = [float(value) for value in column_a if value.replace('.', '', 1).isdigit()]
column_b = [float(value) for value in column_b if value.replace('.', '', 1).isdigit()]
column_c = [float(value) for value in column_c if value.replace('.', '', 1).isdigit()]
column_d = [float(value) for value in column_d if value.replace('.', '', 1).isdigit()]
column_e = [float(value) for value in column_e if value.replace('.', '', 1).isdigit()]
column_f = [float(value) for value in column_f if value.replace('.', '', 1).isdigit()]
column_g = [float(value) for value in column_g if value.replace('.', '', 1).isdigit()]

# Calculate the average of each column
average_a = sum(column_a) / len(column_a) if column_a else 0
average_b = sum(column_b) / len(column_b) if column_b else 0
average_c = sum(column_c) / len(column_c) if column_c else 0
average_d = sum(column_d) / len(column_d) if column_d else 0
average_e = sum(column_e) / len(column_e) if column_e else 0
average_f = sum(column_f) / len(column_f) if column_f else 0
average_g = sum(column_g) / len(column_g) if column_g else 0

# Find the maximum value in each column
max_a = max(column_a) if column_a else 0
max_b = max(column_b) if column_b else 0
max_c = max(column_c) if column_c else 0
max_d = max(column_d) if column_d else 0
max_e = max(column_e) if column_e else 0
max_f = max(column_f) if column_f else 0
max_g = max(column_g) if column_g else 0

# Print the results
print(f"Average of column A: {average_a}")
print(f"Average of column B: {average_b}")
print(f"Average of column C: {average_c}")
print(f"Average of column D: {average_d}")
print(f"Average of column E: {average_e}")
print(f"Average of column F: {average_f}")
print(f"Average of column G: {average_g}")

print(f"Maximum value in column A: {max_a}")
print(f"Maximum value in column B: {max_b}")
print(f"Maximum value in column C: {max_c}")
print(f"Maximum value in column D: {max_d}")
print(f"Maximum value in column E: {max_e}")
print(f"Maximum value in column F: {max_f}")
print(f"Maximum value in column G: {max_g}")




























