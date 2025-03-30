'''
De 3 números asignados (entre positivos y negativos tú los propones) a 3 variables, se
pide hallar la suma de los valores de los módulos con 3, 5, y 7 respectivamente, mostrar
en pantalla el valor de la suma.
'''

val1 = -3
val2 = 4
val3 = -5

sum  = val1 % 3 + val2 % 5 + val3 % 7

print("El valor de la suma es {}".format(sum))