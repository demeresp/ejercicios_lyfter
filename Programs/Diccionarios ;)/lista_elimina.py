information = {
    "Favorite meal": "pizza",      
    "favorite animal": "lion", 
    "favorite color": "green"
}

delete = ["hamburger", "lion", "green"]

for key in list(information):
    if information[key] in delete:
        del information[key]

print(information)



