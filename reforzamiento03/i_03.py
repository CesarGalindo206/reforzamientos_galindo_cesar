# Lista creada con anterioridad en el ejercicio 2
materias_universidad = ["Cálculo Diferencial", "Álgebra Lineal", "Probabilidad y Estadística", "Programación", "Ecuaciones Diferenciales"]

# Creando lista vacía
lista_extra = []

# Creando variables
num_entero1, num_entero2, num_entero3 = 10, 20, 30
texto1, texto2, texto3 = "Universidad", "Python", "Laptop"
decimal1, decimal2, decimal3 = 4.7, 5.8, 6.9

# Agregando datos a la lista_extra
lista_extra.append(num_entero1)
lista_extra.append(num_entero2)
lista_extra.append(num_entero3)
lista_extra.append(decimal1)
lista_extra.append(decimal2)
lista_extra.append(decimal3)
lista_extra.append(texto1)
lista_extra.append(texto2)
lista_extra.append(texto3)

# Sumando las dos listas
lista_combinada = lista_extra + materias_universidad

print("La suma de las listas es: {}".format(lista_combinada))
print("La lista tiene {} datos.".format(len(lista_combinada)))
