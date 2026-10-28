def calcular_media(*numeros):
    return sum(numeros) / len(numeros)


lista = []

for numero in [5, 10, 15, 20]:
    lista.append(numero)

try:
    if len(lista) < 2:
        print("Debes tener al menos 2 números")
    else:
        print("La media es:", calcular_media(*lista))

except TypeError:
    print("Error: los valores deben ser números")