import csv
import datetime

# Example CSV data
csv_file = 'iostat.csv'

# Initialize variables
current_timestamp = None
current_interval_values = []
averages = []

# Process the CSV data
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        # Extract timestamp and values
        timestamp_str = row[1]
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        tps = float(row[2])
        kb_read = float(row[3])
        kb_wrtn = float(row[4])

        # Check if a new interval has started
        if current_timestamp is None:
            current_timestamp = timestamp
        elif (timestamp - current_timestamp).total_seconds() >= 60:
            # Calculate the averages for the previous interval
            average_tps = sum(current_interval_values) / len(current_interval_values)
            average_kb_read = sum(current_interval_values) / len(current_interval_values)
            average_kb_wrtn = sum(current_interval_values) / len(current_interval_values)
            averages.append((current_timestamp, average_tps, average_kb_read, average_kb_wrtn))

            # Reset for the new interval
            current_timestamp = timestamp
            current_interval_values = []

        # Add the current values to the interval
        current_interval_values.append(tps)

    # Calculate the averages for the last interval
    if current_interval_values:
        average_tps = sum(current_interval_values) / len(current_interval_values)
        average_kb_read = sum(current_interval_values) / len(current_interval_values)
        average_kb_wrtn = sum(current_interval_values) / len(current_interval_values)
        averages.append((current_timestamp, average_tps, average_kb_read, average_kb_wrtn))

# Display the averages
for timestamp, average_tps, average_kb_read, average_kb_wrtn in averages:
    print(f"Timestamp: {timestamp}, Average TPS: {average_tps}, Average kB_read: {average_kb_read}, Average kB_wrtn: {average_kb_wrtn}")
