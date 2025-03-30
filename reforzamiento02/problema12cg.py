'''
Crear una lista donde los primeros 2 datos serán, tu nombre y apellido paterno,
habrán también diferentes tipos de datos (enteros, flotantes, string y booleans - 9
datos, puede haber tipos de datos repetidos), crear otra lista con números pares (6
números) y sumarlo a la anterior lista en una variable para luego mostrar las 3 listas en
pantalla (observar y comentar que sucede al sumar listas)
'''

nombre = "Cesar"
apellido_pat = "Galindo"
val1 = 1
val2 = 2
val3 = 3.3
val4 = 3.5
val5 = "73"
val6 = "python"
val7 = True
val8 = False
val9 = False

lista1 = [nombre, apellido_pat,val1,val2,val3,val4,val5,val6,val7,val8,val9]
lista2 = [2,4,6,8,10,12]

lista3 = lista1 + lista2

print("La lista 3 es: {}".format(lista3))

#Al sumar las listas, se agregan los elementos de una a la otra.