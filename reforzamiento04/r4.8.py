departamentos = {"Dep1" : "Ayacucho", "Dep2" : "Puno", "Dep3" : "Lima", "Dep4" : "Tacna", "Dep5" : "Piura", "Dep6" : "Tumbes"}

del departamentos["Dep5"]

departamentos["Dep4"] = "San Martin"

if "Dep5" in departamentos:
    print("Existe el departamento de Piura en el diccionario")
else:
    print("No existe el departamento de Piura")

    print(departamentos)