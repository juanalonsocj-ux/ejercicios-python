texto_numeros = input("Introducir números separados por comas: ")

lista_texto = texto_numeros.split(",")

lista_numeros = []

for numero in lista_texto:
	lista_numeros.append(int(numero))

lista_numeros.sort()
print("Numeros ordenados: ", lista_numeros)