'''
	Estructuras de control

'''

nombre = input("Introduce tu nombre: ")

edad = int(input("Introduce tu edad: "))

lugar_nacimiento = input("Introduce tu lugar de nacimiento: ")


print("\nDatos introducidos:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Lugar de nacimiento:", lugar_nacimiento)

if edad < 20:
	print("¡Qué joven!")
elif edad >= 21 and edad <= 35:
	print("No eres tan joven...")

elif edad > 35:
	print("¡Hay que empezar a cuidarse!")