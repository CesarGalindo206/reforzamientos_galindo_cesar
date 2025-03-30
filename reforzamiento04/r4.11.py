cantidad = input("Ingresa la cantidad de alumnos a ingresar en el diccionario : ")

alumnos = {}

alumno1 = input("Ingresa el nombre del alumno 1 : ")
nota1 = input("Ingresa el nota del alumno 1 : ")
alumno2 = input("Ingresa el nombre del alumno 2 : ")
nota2 = input("Ingresa el nota del alumno 2 : ")
alumno3 = input("Ingresa el nombre del alumno 3 : ")
nota3 = input("Ingresa el nota del alumno 3 : ")
alumno4 = input("Ingresa el nombre del alumno 4 : ")
nota4 = input("Ingresa el nota del alumno 4 : ")
alumno5 = input("Ingresa el nombre del alumno 5 : ")
nota5 = input("Ingresa el nota del alumno 5 : ")

alumnos[alumno1] = nota1
alumnos[alumno2] = nota2
alumnos[alumno3] = nota3
alumnos[alumno4] = nota4
alumnos[alumno5] = nota5

dato1, dato2, dato3, dato4, dato5 = alumnos.values()
print("El diccionario con la información de los alumnos es : {}".format(alumnos))

print("{} tiene la nota de {}.".format(alumno1, dato1))
print("{} tiene la nota de {}.".format(alumno2, dato2))
print("{} tiene la nota de {}.".format(alumno3, dato3))
print("{} tiene la nota de {}.".format(alumno4, dato4))
print("{} tiene la nota de {}.".format(alumno5, dato5))

print("La media de sus notas es : {}".format((int(dato1)+int(dato2)+int(dato3)+int(dato4)+int(dato5)) / int(cantidad)
))







