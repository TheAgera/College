import csv

# Read patient file for Dr. Best
dr_best_patients = []
with open("dr_best_patients.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        dr_best_patients.append(row)

# Read patient file for Dr. Cushing
dr_cushing_patients = []
with open("dr_cushing_patients.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        dr_cushing_patients.append(row)

# Merge the two lists
merged_patients = dr_best_patients + dr_cushing_patients

# Sort the merged list by birth year in ascending order
sorted_patients = sorted(merged_patients, key=lambda x: int(x[2]))

# Display the sorted list of patients' names
for patient in sorted_patients:
    name = patient[0] + " " + patient[1]
    print(name)
