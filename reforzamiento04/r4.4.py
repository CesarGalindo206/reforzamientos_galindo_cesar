
listti = []

length = input("Ingrese el tamaño de la lista : ")

empresa1 = input("Ingrese la primera empresa : ")
empresa2 = input("Ingrese la segunda empresa : ")
empresa3 = input("Ingrese la tercera empresa : ")
empresa4 = input("Ingrese la cuarta empresa : ")
empresa5 = input("Ingrese la quinta empresa : ")

listti.append(empresa1)
listti.append(empresa2)
listti.append(empresa3)
listti.append(empresa4)
listti.append(empresa5)

listti2 = listti.copy()

empresa6 = input("Ingrese la sexta empresa : ")
empresa7 = input("Ingrese la séptima empresa : ")
empresa8 = input("Ingrese la octava empresa : ")
empresa9 = input("Ingrese la novena empresa : ")

listti2.append(empresa6)
listti2.append(empresa7)
listti2.append(empresa8)
listti2.append(empresa9)

if empresa6 in listti:
    del listti2[listti2.index(empresa6)]

if empresa7 in listti:
    del listti2[listti2.index(empresa7)]

if empresa8 in listti:
    del listti2[listti2.index(empresa8)]

if empresa9 in listti:
    del listti2[listti2.index(empresa9)]

print("La lista inicial con las 5 empresas de Tecnología de la Información es: {}".format(listti))
print("La lista con los nombres no repetidos de las empresas que ingresó es : {}".format(listti2))



