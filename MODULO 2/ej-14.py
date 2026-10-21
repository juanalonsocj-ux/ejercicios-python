try:
    archivo = open("archivo_inexistente.txt", "r")
    print(archivo.read())
    archivo.close()
except FileNotFoundError:
    print("Error: el archivo no existe")
finally:
    print("El programa ha terminado")
