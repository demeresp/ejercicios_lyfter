import csv

line_of_games = (
{
    "game":"Plants vs Zombies",
    "gender":"Shooter",
    "developer":"EA",
    "clasification":"T",
},
{
    "game":"Sekiro",
    "gender":"Aventure",
    "developer":"Fromsoftware",
    "clasification":"M",
},
{
    "game":"Bloodborne",
    "gender":"Aventure",
    "developer":"Fromsoftware",
    "clasification":"M",
},)


headers_by_name = (
    "game",
    "gender",
    "developer",
    "clasification",
)


def games_per_order(location, first_line, second_line):
        with open(location, 'w', encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=first_line)
            writer.writeheader()
            writer.writerows(second_line)


games_per_order(r"C:\Users\demer\OneDrive\Desktop\Lyfter\cvs\games_list_2.csv", headers_by_name, line_of_games)

