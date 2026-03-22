def nombr_compl():
 

    nombre = input("Ingrese su nombre completo: ")

    while nombre.strip() == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese su nombre completo: ")
     
    mayusculas = 0
    minusculas = 0

    for letra in nombre:
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
            minusculas += 1

    print("Cantidad de mayúsculas:", mayusculas)
    print("Cantidad de minúsculas:", minusculas)

nombr_compl()

