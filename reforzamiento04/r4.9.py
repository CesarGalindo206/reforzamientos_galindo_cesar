
carrera = input("Ingrese el nombre de su carrera para indexarlo al diccionario : ")

estudiante = {"Nombre": "Cesar", "Carrera": carrera}

carreravar, nombre = estudiante.values()

print("El diccionario del estudiante es: ", estudiante, "y sus valores son {} y {}".format(carreravar, nombre))
