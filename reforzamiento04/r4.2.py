

departamentos = ["Lima", "Puno", "Ayacucho", "Junin", "Loreto"]

depar_1 = input("Ingrese un departamento :")
depar_2 = input("Ingrese un departamento :")

departamentos.append(depar_1)
del departamentos[0]
departamentos.insert(0, depar_2)


print("Los departamentos son : {}".format(departamentos))