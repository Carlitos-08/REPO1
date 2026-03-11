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



def pares_cant():
    cont = 0
    n= int(input("ingrese tu numero: "))

    while n > 0:
        if n % 2 == 0:
            cont+=1
        n= int(input("ingrese numero: "))
    return cont


def impares_cant():
    cont = 0
    n= int(input("ingrese tu numero: "))

    while n > 0:
        if n % 2 != 0:
            cont+=1
        n= int(input("ingrese numero: "))
    return cont

def mult3():
    cont = 0
    n= int(input("ingrese su numero: "))

    while n > 0:
        if n % 3 == 0:
            cont+=1
        n= (int(input("ingrese su numero: ")))
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


def main():

    impares = list_impares()
    pares = list_pares()

    print("suma impares:", sum_impa(impares))
    print("promedio impares:", promedio_impares(impares))
    print("mayor par:", mayor_par(pares))
    print("menor impar:", menor_impar(impares))
    print("cantidad numeros:", cantidad(impares + pares))

    tabla_multiplo4(pares)

    print("factorial:", factorial_3_7(impares + pares))

main()