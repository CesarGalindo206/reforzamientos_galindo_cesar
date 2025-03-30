# Lista con 5 departamentos
departamentos = ["Cusco", "Piura", "Puno", "Madre de Dios", "Tacna"]

print("La lista de departamentos es: {}".format(departamentos))
print("_______________________________________________________________________________")

# Primer departamento adicionado
dep_1 = "Huancavelica"
# Segundo departamento adicionado
dep_2 = "Tumbes"

# Primer departamento en la penúltima posición
departamentos.insert(4, dep_1)
# Segundo departamento en la posición "1"
departamentos.insert(1, dep_2)

print("La lista actualizada de departamentos es: {}".format(departamentos))
