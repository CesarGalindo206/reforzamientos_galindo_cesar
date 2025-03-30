datosdic= {"nombre" : "cesar", "edad" : 20, "salario" : 1234}

print("El diccionario es: {}".format(datosdic))

datoslist = list(datosdic)

print("El diccionario convertido en lista es : {}".format(datoslist))

#__________________________________________________________________

datosdic["dni"] = "71928833"

print("El salario es de {} y el dni de la persona es {}".format(datosdic["salario"], datosdic["dni"]))

del datosdic["edad"]

print("El diccionario actualizado es : {}".format(datosdic))

#__________________________________________________________________