import csv


def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

read_csv_file(r'C:\Users\demer\OneDrive\Desktop\Lyfter\cvs\ventas.csv')