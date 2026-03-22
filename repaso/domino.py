#Ejercicio Dominó.
#a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
#recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)

def domino(ficha1, ficha2):

    for i in ficha1:
        for j in ficha2:
            if i == j:
                return 'las fichas encajan:',ficha1, ficha2
    return 'las fichas no encajan', ficha1, ficha2

def main():

    ficha1 = (1,3)
    ficha2 = (2,2)

    print(domino(ficha1,ficha2))




#b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
#recibidas en una cadena, por ejemplo: 3-4 2-5.

def fich_tupl(ficha1, ficha2):

    tupla1= tuple(ficha1.split("-"))
    tupla2= tuple(ficha2.split("-"))

    for i in tupla1:
        for j in tupla2:
            if i == j:
                return 'las fichas encajan:',tupla1, tupla2
    return 'las fichas no encajan', tupla1, tupla2

def main():

    ficha1 = "3-5"
    ficha2 = "2-5"

    print(fich_tupl(ficha1,ficha2))

main()




