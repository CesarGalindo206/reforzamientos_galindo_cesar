# Lista creada previamente
lista = [False, True, 5.6, 8.3, 11.2, False, 14.9, True]

# Eliminando los elementos de la lista previa
lista.clear()
print(lista)
print("La lista tiene {} elementos".format(len(lista)))
print("___________________________________________________")

# Agregando nuevos datos a la lista
lista.extend(["Cesar", "Ramos", "Rojas", 20])
print("La lista actualizada es: {}".format(lista))
