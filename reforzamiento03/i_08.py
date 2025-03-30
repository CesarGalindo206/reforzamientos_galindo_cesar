# Lista con 8 países
paises = ["Brasil", "Colombia", "Chile", "Paraguay", "Canadá", "Italia", "Francia", "Japón"]
print("La lista de países es: {}".format(paises))
print("El tamaño de la lista es: {}".format(len(paises)))
print("_________________________________________________________________")

# Copiando la lista
paises_2 = paises.copy()

# Eliminando el primer y penúltimo valor
print("El primer término a eliminar es: {}".format(paises_2[0]))
print("El penúltimo término a eliminar es: {}".format(paises_2[6]))
print("_____________________________________________________________________")

# Quitando los datos
paises_2.pop(0)  # Valor inicial, en listas se empieza a contar desde el 0
paises_2.pop(5)  # Dado que se ha eliminado el primer elemento, el penúltimo término pasa a ser el 5

print("La lista actualizada es: {}".format(paises_2))
print("El tamaño de la lista actualizada es: {}".format(len(paises_2)))
