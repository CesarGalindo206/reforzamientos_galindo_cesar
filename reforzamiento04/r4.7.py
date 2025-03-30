datosdic= {"nombre" : "cesar", "edad" : 20, "salario" : 1234}

print("El diccionario es: {}".format(datosdic))

datoslist = list(datosdic)

print("El diccionario convertido en lista es : {}".format(datoslist))

datosdic["dni"] = "71928833"

#__________________________________________________________________

print("El salario es de {} y el dni de la persona es {}".format(datosdic["salario"], datosdic["dni"]))

del datosdic["edad"]

print("El diccionario actualizado es : {}".format(datosdic))

#__________________________________________________________________

nombre, salario, dni = datoslist

print("Los valores de los elementos de la lista son ", type(nombre), type(salario), type(dni))