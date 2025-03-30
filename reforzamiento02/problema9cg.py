'''
 Elevar una base al exponente de 6 (que estará dentro una variable), este número el
cual su valor estará asignado a una variable y luego restar este mismo valor multiplicado
por dos (usar pow o **). Mostrar el resultado final en pantalla.
'''

base = 10
exponente = 6

resultado  = pow(base,exponente) -  (pow(base,exponente)*2)

print("El resultado de lo pedido es {}".format(resultado))


