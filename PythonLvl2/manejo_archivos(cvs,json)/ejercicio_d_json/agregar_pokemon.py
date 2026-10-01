import json

def file_reader(route):
    try:
        with open(route, 'r', encoding='utf-8') as file:
            f_list = json.load(file)
            if isinstance(f_list, list):
                return f_list
    except FileNotFoundError:
        ("No se ha encontrado esta ruta, por favor prube otra")




def new_pokemon():
        new_name = input("Introduzca el nombre del pokemon:",)
        new_type = input("Introduzca el tipo del pokemon:",)
        hp, attack, defense, spattack, spdefense, speed = [int(input(f"{stat}: ")) 
        for stat in ["HP", "Attack", "Defense", "Sp. Attack", "Sp. Defense", "Speed"]]

        new_pokemon = {
            "name": {"english": new_name},
            "type":[new_type],
            "base":{
                "HP": hp,
                "Attack":attack, 
                "Defense":defense,
                "Sp. Attack":spattack,
                "Sp .Defense":spdefense,
                "Speed":speed
            },
            }
        return new_pokemon


def file_saver(new_file):
    my_pokemon_list = file_reader(r"C:\Users\demer\OneDrive\Desktop\Lyfter\manejo_de_archivos\json_intr\pokemon_list.json")
    new = new_pokemon()
    my_pokemon_list.append(new)

    with open(new_file, 'w', encoding="utf-8") as file:
        json.dump(my_pokemon_list, file, indent=4, ensure_ascii=False) #Aqui guardo el nuevo archivo


file_saver(r"C:\Users\demer\OneDrive\Desktop\Lyfter\manejo_de_archivos\json_intr\pokemon_list.json")
