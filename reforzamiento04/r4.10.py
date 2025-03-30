num1 = input("Introduce un numero: ")
num2 = input("Introduce otro numero: ")
num3 = input("Introduce nuevamente otro numero: ")
num4 = input("Introduce el último numero: ")

numeros = {}

numeros["numero1"] = int(num1)**3
numeros["numero2"] = int(num2)**3
numeros["numero3"] = int(num3)**3
numeros["numero4"] = int(num4)**3

print("El diccionario con los cubos de los números ingresados es",numeros)