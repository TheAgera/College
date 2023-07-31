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
        rps = []
        rkBps = []
        wps = []
        wkBps = []
        dps = []
        dkBps = []
      
        # iterating over each row and append values to empty list
        for col in csv_reader:
            rps.append(col['r/s'])
            rkBps.append(col['rkB/s'])
            wps.append(col['w/s'])
            wkBps.append(col['wkB/s'])
            dps.append(col['d/s'])
            dkBps.append(col['dkB/s'])

        return rps, rkBps, wps, wkBps, dps, dkBps


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
    print(f"Average of r/s: {averages['rps']}")
    print(f"Average of rkB/s: {averages['rkBps']}")
    print(f"Average of w/s: {averages['wps']}")
    print(f"Average of wkB/s: {averages['wkBps']}")
    print(f"Average of d/s: {averages['dps']}")
    print(f"Average of dkB/s: {averages['dkBps']}")
    print("")

    print("Max Values:")
    print(f"Maximum value of rps: {max_values['rps']}")
    print(f"Maximum value of rkB/s: {max_values['rkBps']}")
    print(f"Maximum value of w/s: {max_values['wps']}")
    print(f"Maximum value of wkB/s: {max_values['wkBps']}")
    print(f"Maximum value of d/s: {max_values['dps']}")
    print(f"Maximum value of dkB/s: {max_values['dkBps']}")


def process_csv_file(file_path):
        rps, rkBps, wps, wkBps, dps, dkBps = read_csv_file(file_path)

        # Extract float values
        rps = extract_float_values(rps)
        rkBps = extract_float_values(rkBps)
        wps = extract_float_values(wps)
        wkBps = extract_float_values(wkBps)
        dps = extract_float_values(dps)
        dkBps = extract_float_values(dkBps)

        # Calculate averages
        averages = {
            'rps': calculate_average(rps),
            'rkBps': calculate_average(rkBps),
            'wps': calculate_average(wps),
            'wkBps': calculate_average(wkBps),
            'dps': calculate_average(dps),
            'dkBps': calculate_average(dkBps),
        }

        # Calculate max values
        max_values = {
            'rps': calculate_max(rps),
            'rkBps': calculate_max(rkBps),
            'wps': calculate_max(wps),
            'wkBps': calculate_max(wkBps),
            'dps': calculate_max(dps),
            'dkBps': calculate_max(dkBps),
        }

        # Print results
        print_results(averages, max_values)

        # Create new CSV file
        create_new_json(averages, max_values)

        # Save original CSV with a timestamp
        save_csv_with_timestamp(file_path)

        #Delay for 60 seconds
        # time.sleep(60)

def save_csv_with_timestamp(file_path):
    timestamp = time.strftime("%Y%m%d - %H%M%S")
    file_name, file_extension = os.path.splitext(file_path)
    new_file_path = f"{file_name}_{timestamp}{file_extension}"
    shutil.copy2(file_path, new_file_path)

def create_new_json(averages, max_values, file_path='iostatx.json'):
    data = {
        'averages': averages,
        'max_values': max_values
    }
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)


# Example usage
file_path = 'iostatx.csv'
process_csv_file(file_path)
