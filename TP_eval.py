def list_pares():
    pares= []

    n = int(input("ingrese un numero: "))
    while n > 0:
        if n%2 == 0:
            pares.append(n)
        
        n=int(input("ingrese un numero: "))
    return pares


def list_impares():
    impares=[]

    n = int(input("ingrese un numero: ")) 
    while n > 0:
        if not n%2 == 0:
            impares.append(n)
        
        n=int(input("ingrese un numero: "))
    return impares

def lista_t():
    lista = []

    n = int(input("ingrese un numero:"))

    while n > 0 :
        lista.append(n)
        n = int(input("ingrese un numero: "))
    return lista

##########################################################

def pares_cant():
    cont = 0
    n= int(input("ingrese un numero: "))

    while n > 0:
        if n % 2 == 0:
            cont+=1
        n= int(input("ingrese un numero: "))
    return cont


def impares_cant():
    cont = 0
    n= int(input("ingrese un numero: "))

    while n > 0:
        if n % 2 != 0:
            cont+=1
        n= int(input("ingrese un numero: "))
    return cont

def mult3():
    cont = 0
    n= int(input("ingrese un numero: "))

    while n > 0:
        if n % 3 == 0:
            cont+=1
        n= (int(input("ingrese un numero: ")))
    return cont


def sum_impa(lista):
    impares=0
    for i in lista:
        impares+=i
    return impares


def promedio_impares(lista):
    promedio = 0
    for i in lista:
        promedio+=i
    
    return promedio/len(lista)


def mayor_par(lista):
    mayor = lista[0]

    for i in lista:
        if i > mayor:
            mayor = i

    return mayor

def menor_impar(lista):
    menor = lista[0]

    for i in lista:
        if i < menor:
            menor = i

    return menor


def cantidad(lista):
    return len(lista)


def tabla_multiplo4(lista):

    for i in lista:
        if i % 4 == 0:

            for x in range(1,11):
                print(i, "x", x, "=", i*x)

            break


def factorial_3_7(lista):

    for i in lista:

        if i >= 3 and i <= 7:

            fact = 1

            for x in range(1, i+1):
                fact = fact * x

            return fact


def menu():

    opcion = -1

    while opcion != 0:

        print("1 - Cantidad de pares")
        print("2 - Cantidad de impares")
        print("3 - Multiplos de 3")
        print("4 - Suma de impares")
        print("5 - Promedio de impares")
        print("6 - Mayor par")
        print("7 - Menor impar")
        print("8 - Cantidad de pares")
        print("9 - Tabla de multiplicar de los multiplos de 4")
        print("10 - Factorial de los numeros entre 3 y 7")
        print("0 - Salir")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            print("Respuesta: ",pares_cant())

        elif opcion == 2:
            print("Respuesta: ",impares_cant())

        elif opcion == 3:
            print("Respuesta: ",mult3())

        elif opcion == 4:
            lista = list_impares()
            print("Respuesta: ",sum_impa(lista))

        elif opcion == 5:
            lista = list_impares()
            print("Respuesta: ",promedio_impares(lista))

        elif opcion == 6:
            lista = list_pares()
            print("Respuesta: ",mayor_par(lista))
        
        elif opcion == 7:
            lista = list_impares()
            print("Respuesta: ",menor_impar(lista))
        
        elif opcion == 8:
            lista = list_pares()
            print("Respuesta: ",cantidad(lista))
        
        elif opcion == 9:
            lista = list_pares()
            tabla_multiplo4(lista)  
        
        elif opcion == 10:
            lista = lista_t()
            print("Respuesta: ",factorial_3_7(lista))

        elif opcion == 0:
            print("Fin del programa")

        else:
            print("Opcion incorrecta")


def main():
    menu()

main()
