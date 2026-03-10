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


def promedio_par(lista):
    promedio = 0
    for i in lista:
        promedio+=i
    
    return promedio/len(lista)


def main():

    print(sum_impa(list_impares()))
    print(mult3())
    print(pares_cant())
    print(pares_cant())

main()  