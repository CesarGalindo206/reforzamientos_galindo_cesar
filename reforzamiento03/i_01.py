dispositivos = ["iPhone", "Samsung Galaxy", "iPad"]  # 3 datos iniciales

# Agregando 5 objetos a la lista
dispositivos.append("MacBook")
dispositivos.append("Surface Pro")
dispositivos.append("Kindle")
dispositivos.append("Apple Watch")
dispositivos.append("Huawei Tablet")

print("Mi lista es: {}".format(dispositivos))
print("Mi lista tiene {} datos.".format(len(dispositivos)))
print("_______________________________________________________")

# Quitando valores de la lista por valor
dispositivos.remove("Kindle")
dispositivos.remove("Apple Watch")

print("Mi lista actualizada es: {}".format(dispositivos))

# Cantidad total
print("Mi lista actualizada tiene {} datos.".format(len(dispositivos)))
print("_______________________________________________________")

# Agregando la cantidad de datos que tiene mi lista a la lista
cantidad_total = len(dispositivos)
dispositivos.append(cantidad_total)

print("Mi lista actualizada con la cantidad de valores es: {}".format(dispositivos))
print("Mi lista tiene {} datos.".format(len(dispositivos)))
