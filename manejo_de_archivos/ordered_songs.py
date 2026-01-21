def file_reader(route):
    with open(route, encoding='utf-8') as file:
        lines = file.readlines()
        return lines
songs_list = r"C:\Users\demer\OneDrive\Desktop\Lyfter\iterables_y_listas\archivos\songs_list.txt"


def my_songs():
    the_songs = {}
    file_reader(songs_list)
    lines = file_reader(songs_list)
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        song, artist = line.split(" - ", 1)
        the_songs[song] = artist
    return the_songs


def new_file():
    songs_to_order = my_songs()
    ordered_songs = dict(sorted(songs_to_order.items()))
    new_route = r"C:\Users\demer\OneDrive\Desktop\Lyfter\iterables_y_listas\archivos\songs_list_ordered.txt"

    with open(new_route, "w", encoding="utf-8") as new_file:
        for song, artist in ordered_songs.items():
            new_file.write(f"{song} - {artist}\n")
    print(f"Guardado en {new_route}")


new_file()
