''' 
	Pedir 2 numeros al usuario denominador y nominador dividir si metes un 0 dar error
	controlar 2 excepciones si metes letras dar error y la del 0

'''

try:

	numerador = float(input("Introduce el numero para el numerador: "))
	denominador = float(input("Introduce el numero para el denominador: "))

	resultado = numerador / denominador

	print(f"Resultado:  {resultado:.2f} " )

except ValueError:
	print("Error tienes que introducir numeros no letras")

except ZeroDivisionError:
	print("Error no se puede dividir entre 0")