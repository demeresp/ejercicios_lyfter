import csv

def file_reader(route):
    with open(route, 'r', 'utf-8') as file:
        reader = csv.DictReader(file)
        return reader
    

def file_editor(new_route):
    with open(new_route, 'w', newline='') as file:
        for line in file:
            new_file = line.write()
        return new_file