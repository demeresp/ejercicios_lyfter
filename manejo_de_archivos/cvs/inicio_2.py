import csv 

countries_list = [
    {
    "name":"Costa rica",
    "capital":"San Jose",
    "currency":"Colon",
    "area_km2":"51,100"
    },
    {

    "name":"Colombia",
    "capital":"Bogota",
    "currency":"Peso colombiano",
    "area_km2":"1,141,748",

    },
    {
    "name":"Mexico",
    "capital":"Ciudad de Mexico",
    "currency":"Peso Mexicano",
    "area_km2":"1,972,550"
}
]

country_headers = (
    "name",
    "capital",
    "currency",
    "area_km2",
)

def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


write_csv_file(r"C:\Users\demer\OneDrive\Desktop\Lyfter\cvs\countries.csv", countries_list, country_headers)