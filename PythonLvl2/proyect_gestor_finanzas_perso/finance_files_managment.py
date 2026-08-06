from logic_src_main import Movement as mv

import json 
import os


class DataManager:

    def load_movements(self, route):
        try:
            with open(route, "r", encoding='utf-8') as file:
                reader = json.load(file)
                if isinstance(reader, list):
                    return [mv.from_dict_to_object(item) for item in reader]#retornar lista de mvs 
                else:
                    return []
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return [] #si el archivoe sta corrupto


    def save_movements(self, movements, route):

        movements_dict = [mv.movements_to_dict() for mov in movements]

        os.makedirs(os.path.dirname(route), exist_ok=True)#si no hay carpeta crear una
        with open(route, 'w', encoding="utf-8") as file:
            json.dump(movements_dict, file, indent=4, ensure_ascii=False)
