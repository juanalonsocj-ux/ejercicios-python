palabra = input("Introduce una palabra: ").lower()

contador = 0
for letra in palabra:
    if letra in "aeiouáéíóú":
        contador += 1
print("Número de vocales:", contador)
