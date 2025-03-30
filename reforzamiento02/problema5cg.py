'''
Crear un programa que parte creando un sueldo en una variable, sepamos si es par
o impar mediante un mensaje. Utilizar módulo y condicional (if)
'''

sueldoact = 1234
mod = sueldoact % 2

if mod == 0:
    print("{} es par".format(sueldoact))
else:
    print("{} es impar".format(sueldoact))

