import csv
import os



def file_reader(route):
    with open(route, 'r', encoding="utf-8") as file:
        try:
            reader = csv.DictReader(file)
            return list(reader)
        except FileNotFoundError:
            print("The route provided is invalid")



def student_saver(file, student):
    try:
        with open(file, 'a', newline="", encoding="utf-8") as f:
            columns = ["grade", "name", "spanish", "english", "history", "sciences"]
            content = csv.DictWriter(f, fieldnames=columns)
            content.writeheader()
            content.writerow(student)
    except FileNotFoundError as error:
        print("The file indicated does not exist")
    return content



def file_saver(route, content):
    columns = ["grade", "name", "spanish", "english", "history", "sciences"]
    try:
        with open(route, "w", newline="", encoding="utf-8") as file:
            content_writer = csv.DictWriter(file, fieldnames=columns) 
            content_writer.writeheader()
            content_writer.writerows(content)
    except FileNotFoundError as oops:
        print("Looks like this file is not foundable right now...")
    return content



def route_validator(route=None):

    while True:
        route = input("Please, provide the route to the file where you want to work with: ").strip()
        

        if not route.endswith(".csv"):
            print("The file should be a .csv")
            continue
        elif os.path.isdir(route):
            print("The route provided is a directory, not a file")
            continue

        try:
            with open(route, 'r', encoding="utf-8") as file:
                return route
        except PermissionError as permission_error:
            print(f"Permission error: {permission_error}. Please check your permissions for the file.")
        except IsADirectoryError as is_a_directory_error:
            print(f"Error: {is_a_directory_error}. The provided route is a directory, not a file.")
        except OSError as os_error:
            print(f"OS error: {os_error}. Please provide a valid route.")
            continue