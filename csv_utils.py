import csv

def read_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader), reader.fieldnames  # Return rows and column names
    except FileNotFoundError:
        return [], []

def write_csv(file_path, rows, fieldnames):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write column headers
        writer.writerows(rows)  # Write data rows
