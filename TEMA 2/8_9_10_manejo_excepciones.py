
try:
    numero = float(input("Introduce un número: "))
    resultado = numero / 0
    print(resultado)

except ValueError:
    print("Tipo incorrecto")

except ZeroDivisionError:
    print("No se puede dividir entre 0")

try:
    archivo = open("archivo.txt", "r")
    archivo.close()

except FileNotFoundError:
    print("El archivo no existe"