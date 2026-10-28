def calcular_media(num1, num2):
    media = (num1 + num2) / 2
    return media


try:
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el primer numero: "))
    
    resultado = calcular_media(num1, num2)
    
    print("La media es: ", resultado)
    
except ValueError:
    print("Error: debes introducir números validos")
    
    