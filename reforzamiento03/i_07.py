# Lista vacía
valores = []

# Agregando 10 valores numéricos
valores.append(15)
valores.append(22)
valores.append(38)
valores.append(41)
valores.append(57)
valores.append(63)
valores.append(72)
valores.append(89)
valores.append(94)
valores.append(100)
# También se puede hacer con valores.extend([15, 22, 38, 41, 57, 63, 72, 89, 94, 100])

print("Mi lista es: {}".format(valores))

# Suma de los números ingresados
suma_valores = sum(valores)

# Media aritmética de los números ingresados
media_valores = sum(valores) / len(valores)

print("La suma de los datos es: {}".format(suma_valores))
print("La media de los datos es: {}".format(media_valores))
