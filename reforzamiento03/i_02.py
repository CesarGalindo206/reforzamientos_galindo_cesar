materias_universidad = ["Cálculo Diferencial", "Álgebra Lineal", "Probabilidad y Estadística", "Programación", "Ecuaciones Diferenciales"]

# Agregando materias para que se repitan
materias_universidad.append("Cálculo Diferencial")
materias_universidad.append("Cálculo Diferencial")
materias_universidad.append("Cálculo Diferencial")
materias_universidad.append("Programación")
materias_universidad.append("Programación")
materias_universidad.append("Probabilidad y Estadística")

# Mostrando mi lista de materias
print(materias_universidad)
print("La cantidad de materias que tiene la lista es de: {}".format(len(materias_universidad)))
print("_____________________________________________________________________________")

# Mostrando las materias que se repiten
print("La cantidad de veces que se repite Cálculo Diferencial es: {}".format(materias_universidad.count("Cálculo Diferencial")))
print("La cantidad de veces que se repite Probabilidad y Estadística es: {}".format(materias_universidad.count("Probabilidad y Estadística")))
print("La cantidad de veces que se repite Programación es: {}".format(materias_universidad.count("Programación")))
print("_____________________________________________________________________________")

# Eliminando el segundo ítem de la lista
del materias_universidad[1]  # El segundo ítem tiene el índice 1

print("Mi lista actualizada es: {}".format(materias_universidad))
print("Mi lista tiene {} materias".format(len(materias_universidad)))
