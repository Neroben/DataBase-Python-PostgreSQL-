import csv

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    print(data)
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
