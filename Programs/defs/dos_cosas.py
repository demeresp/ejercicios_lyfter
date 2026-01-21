def my_cocodrilo():
    print("Drilo Cocodrilo")
    the_coco = "La variable exprimental"


inmut_variable = "Exprimental!!!"


def my_sheep():
    global inmut_variable
    try:
        inmut_variable = 3
        print("Ya se pudo con global jj:", inmut_variable)
    except ValueError as error:
        print(f"Errorsillo!")

my_sheep()

