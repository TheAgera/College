import csv
import time
import json
import os
import shutil

def read_csv_file(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # creating dictreader object
        csv_reader = csv.DictReader(file)

        # creating empty lists
        tps = []
        kB_readps = []
        kB_wrtnps = []
        kB_dscdps = []
        kB_read = []
        kB_wrtn = []
        kB_dscd = []

        # iterating over each row and append values to empty list
        for col in csv_reader:
            tps.append(col['tps'])
            kB_readps.append(col['kB_read/s'])
            kB_wrtnps.append(col['kB_wrtn/s'])
            kB_dscdps.append(col['kB_dscd/s'])
            kB_read.append(col['kB_read'])
            kB_wrtn.append(col['kB_wrtn'])
            kB_dscd.append(col['kB_dscd'])

        return tps, kB_readps, kB_wrtnps, kB_dscdps, kB_read, kB_wrtn, kB_dscd


def extract_float_values(values):
    # Remove commas between values in each column and convert to float
    return [float(value) for value in values if value.replace('.', '', 1).isdigit()]


def calculate_average(values):
    # Calculates average if there are elements within the array
    return sum(values) / len(values) if values else 0


def calculate_max(values):
    # Calculates max if there are elements within the array
    return max(values) if values else 0


def print_results(averages, max_values):
    # Print results
    print("Averages:")
    print(f"Average of tps: {averages['tps']}")
    print(f"Average of kB_read/s: {averages['kB_readps']}")
    print(f"Average of kB_wrtn/s: {averages['kB_wrtnps']}")
    print(f"Average of kB_dscd/s: {averages['kB_dscdps']}")
    print(f"Average of kB_read: {averages['kB_read']}")
    print(f"Average of kB_wrtn: {averages['kB_wrtn']}")
    print(f"Average of kB_dscd: {averages['kB_dscd']}")
    print("")

    print("Max Values:")
    print(f"Maximum value of tps: {max_values['tps']}")
    print(f"Maximum value of kB_read/s: {max_values['kB_readps']}")
    print(f"Maximum value of kB_wrtn/s: {max_values['kB_wrtnps']}")
    print(f"Maximum value of kB_dscd/s: {max_values['kB_dscdps']}")
    print(f"Maximum value of kB_read: {max_values['kB_read']}")
    print(f"Maximum value of kB_wrtn: {max_values['kB_wrtn']}")
    print(f"Maximum value of kB_dscd: {max_values['kB_dscd']}")


def process_csv_file(file_path):
    while True:
        tps, kB_readps, kB_wrtnps, kB_dscdps, kB_read, kB_wrtn, kB_dscd = read_csv_file(file_path)

        # Extract float values
        tps = extract_float_values(tps)
        kB_readps = extract_float_values(kB_readps)
        kB_wrtnps = extract_float_values(kB_wrtnps)
        kB_dscdps = extract_float_values(kB_dscdps)
        kB_read = extract_float_values(kB_read)
        kB_wrtn = extract_float_values(kB_wrtn)
        kB_dscd = extract_float_values(kB_dscd)

        # Calculate averages
        averages = {
            'tps': calculate_average(tps),
            'kB_readps': calculate_average(kB_readps),
            'kB_wrtnps': calculate_average(kB_wrtnps),
            'kB_dscdps': calculate_average(kB_dscdps),
            'kB_read': calculate_average(kB_read),
            'kB_wrtn': calculate_average(kB_wrtn),
            'kB_dscd': calculate_average(kB_dscd)
        }

        # Calculate max values
        max_values = {
            'tps': calculate_max(tps),
            'kB_readps': calculate_max(kB_readps),
            'kB_wrtnps': calculate_max(kB_wrtnps),
            'kB_dscdps': calculate_max(kB_dscdps),
            'kB_read': calculate_max(kB_read),
            'kB_wrtn': calculate_max(kB_wrtn),
            'kB_dscd': calculate_max(kB_dscd)
        }

        # Print results
        print_results(averages, max_values)

        # Create new CSV file
        create_new_json(averages, max_values)

        # Save original CSV with a timestamp
        save_csv_with_timestamp(file_path)

        #Delay for 60 seconds
        time.sleep(60)

def save_csv_with_timestamp(file_path):
    timestamp = time.strftime("%Y%m%d - %H%M%S")
    file_name, file_extension = os.path.splitext(file_path)
    new_file_path = f"{file_name}_{timestamp}{file_extension}"
    shutil.copy2(file_path, new_file_path)

def create_new_json(averages, max_values, file_path='iostat.json'):
    data = {
        'averages': averages,
        'max_values': max_values
    }
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)


# Example usage
file_path = 'iostat.csv'
process_csv_file(file_path)
