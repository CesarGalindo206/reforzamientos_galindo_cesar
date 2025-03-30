
estudiantes = ["Aritz","Mathius","Alexis","Rosa","José"]

newstudent = input("Ingrese el estudiante que desea agregar a la lista : ")

if newstudent in estudiantes:
    estudiantes.remove(newstudent)
    print("{} Estaba en la lista y ha sido eliminado de ella".format(newstudent))
else:
    estudiantes.append(newstudent)
    print("{} ha sido agregado a la lista de estudiantes".format(newstudent))

print("La lista de estudiantes nueva es {}".format(estudiantes))
