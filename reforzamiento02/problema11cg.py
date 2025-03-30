'''
Identificar qué tipo de dato se obtiene al elevar tu edad con exponente 5 y luego
dividirlo por 10. Mostrar el resultado de su módulo con 3 en pantalla
'''

operacion = (edad ** 5) / 10
print(operacion % 3,"El resultado de lo pedido es {}".format(type(operacion % 3)))