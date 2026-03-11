def promedio():

    num = int(input("Ingrese un numero: "))
    suma = 0
    cont = 0
    while num > 0:
        suma+=num
        cont+=1
        num = int(input("Ingrese un numero: "))
    return suma/cont


print(promedio())
