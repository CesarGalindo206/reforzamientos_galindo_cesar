datosnumericos = {}

nombre1 = input("Ingrese un nombre: ")
numero1 = input("Ingrese su número: ")
nombre2 = input("Ingrese otro nombre: ")
numero2 = input("Ingrese su número: ")
nombre3 = input("Ingrese un nombre: ")
numero3 = input("Ingrese su número: ")

datosnumericos[nombre1] = numero1
datosnumericos[nombre2] = numero2
datosnumericos[nombre3] = numero3

print("El diccionario con los datos es: {}".format(datosnumericos))

namesearch = input("Ingrese un nombre a buscar en el diccionario para verificar si se encuentra: ")

if namesearch in datosnumericos:
    print("El nombre {} se encuentra en el diccionario".format(namesearch))
else:
    print("El nombre {} no se encuentra en el diccionario".format(namesearch))

print("Diccionario final:", datosnumericos)
