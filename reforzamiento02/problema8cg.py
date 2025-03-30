'''
Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con
una lista vacía y otra con una lista no vacía.
'''

lista_vacia = []
lista = [1,2,3,4,5]

if len(lista_vacia) == 0:
    print("La lista 1 es vacia")
else:
    print("La lista 2 no es vacia")

if len(lista) == 0:
    print("La lista 2 es vacia")
else:
    print("La lista 2 no es vacia")