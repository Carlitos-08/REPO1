#Ejercicio Campaña electoral
#a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el
#mensaje: Estimado <nombre>;, vote por mí.

def vote(nombres):

    for i in range(0,len(nombres)):
        print(f"Estimado {nombres[i]} , vote por mí.")

def main():

    nombres = ("Julieta", "Marcos", "Sofía")

    vote(nombres)



#b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
#cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir
#de la posición p.

def a(nombres,p,n):
    sub_tupla= nombres[p:p+n]

    for nombre in sub_tupla:
        print(f"Estimado {nombre}, vote por mí.")

def main():
    nombres = ("Julieta", "Marcos", "Sofía")
    p = 1
    n = 1
    a(nombres,p,n)




#c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
#para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.


def vote(nombres):
    j = 0
    for i in range(0,len(nombres)):
        print("Estimado", nombres[i][0] , nombres[i][1], "vote por mí.")

def main():
    usuarios = (
    ("Julieta", "Femenino"),
    ("Marcos", "Masculino"),
    ("Alex", "No binario"),
    ("Sofía", "Femenino")
)

    vote(usuarios)



def saludos(nombres,p,n):
    sub_tupla= nombres[p:p+n]

    for i in range(0,len(sub_tupla)):
        print("Estimado", nombres[i][0] , nombres[i][1], "vote por mí.")

def main():
    usuarios = (
    ("Julieta", "Femenino"),
    ("Marcos", "Masculino"),
    ("Alex", "No binario"),
    ("Sofía", "Femenino")
)
    p = 1
    n = 1
    saludos(usuarios,p,n)



def saludos(nombres, p, n):
    
    sub_tupla = nombres[p : p + n]

    for persona in sub_tupla:
        nombre = persona[0]
        genero = persona[1]
        
        prefijo = "Estimada" if genero == "Femenino" else "Estimado"
        
        print(f"{prefijo} {nombre}, vote por mí.")

def main():
    usuarios = (
        ("Julieta", "Femenino"),
        ("Marcos", "Masculino"),
        ("BOCHA", "No binario wtf"),
        ("Sofía", "Femenino")
    )
    saludos(usuarios, 1, 10)

main()
