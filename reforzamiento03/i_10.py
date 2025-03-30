# Lista de BD con 7 diferentes nombres de BD relacionales con 3 repetidas
bd_list = ["MongoDB", "MariaDB", "SQLite", "MongoDB", "IBM Db2", "MariaDB", "SQLite"]
print("Mi lista de base de datos es: {}.".format(bd_list))

# Eliminando las bases de datos repetidas por valor
bd_list.remove("MongoDB")
bd_list.remove("MariaDB")
bd_list.remove("SQLite")
print("Mi lista de base de datos luego de eliminar por valor es: {}.".format(bd_list))
print("_________________________________________________________")

# Sacando las bases de datos repetidas por índice
bd_list_1 = ["MongoDB", "MariaDB", "SQLite", "MongoDB", "IBM Db2", "MariaDB", "SQLite"]
print("Mi lista de base de datos es: {}.".format(bd_list_1))

del bd_list_1[3]
del bd_list_1[4]
del bd_list_1[2]

print("La lista de base de datos luego de eliminar por índice es: {}.".format(bd_list_1))
