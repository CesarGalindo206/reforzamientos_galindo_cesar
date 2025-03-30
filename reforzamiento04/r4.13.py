facturas = {"00054": 1232}

new_fac = input("Ingrese una nueva factura: ")
new_cost = float(input("Ingrese el coste de la factura: "))  # Convertir a número

facturas[new_fac] = new_cost

confirmacion = input("¿Desea pagar una factura? Escriba y o n: ")

if confirmacion == "y":
    new_fac = input("Ingrese una factura a pagar: ")
    if new_fac in facturas:
        print("La factura ha sido pagada exitosamente")
        del facturas[new_fac]  # Eliminar la factura pagada
    else:
        print("La factura no se encontraba pendiente")

print("Las facturas pendientes son:", facturas)  # Este print se ejecutará siempre





