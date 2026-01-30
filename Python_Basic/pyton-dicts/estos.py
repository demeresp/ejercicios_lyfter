europe_capitals_by_local = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for local in europe_capitals_by_local.keys():
  print(local)

file_name = "dos_listas.py"

with open(file_name) as file:
    print(file.read())