import csv



def file_reader(route):
    with open(route, 'r', encoding="utf-8") as file:
        try:
            reader = csv.DictReader(file)
            return list(reader)
        except FileNotFoundError:
            print("The route provided is invalid")



def student_saver(student, file):
    try:
        with open(file, 'a', encoding="utf-8") as f:
            columns = ["grade", "name", "spanish", "english", "history", "sciences"]
            content = csv.DictWriter(f, fieldnames=columns)
            content.writerow(student)
    except FileNotFoundError as error:
        print("The file indicated does not exist")
    return content



def file_saver(file_to_modify, route):
    try:
        with open(file_to_modify, "w", encoding="utf-8") as file:
            content = csv.DictWriter(file, fieldnames="")
            content.writeheader()
            content.writerows(file_to_modify)
    except FileNotFoundError as oops:
        print("Looks like this file is not foundable right now...")
    return content
