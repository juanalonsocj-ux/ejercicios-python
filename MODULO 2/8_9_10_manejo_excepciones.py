# Ejercicio 8
try:
    numero = float(input("Introduce un numero: "))
    resultado = numero / 0
    print(resultado)

except ValueError:
    print("Tipo incorrecto")

except ZeroDivisionError:
    print("No se puede dividir entre 0")


# Ejercicio 9
try:
    numero = float(input("Introduce un numero: "))
    print("Numero correcto:", numero)

except ValueError:
    print("Tipo incorrecto")


# Ejercicio 10
try:
    numero = float(input("Introduce un numero: "))
    print(numero / 0)

except ValueError:
    print("Tipo incorrecto")

except ZeroDivisionError:
    print("No se puede dividir entre 0")


try:
    archivo = open("archivo_inexistente.txt", "r")
    archivo.close()

except FileNotFoundError:
    print("El archivo no existe")