''' 
	El programa pide al usuario (username) y una contraseña (password)
	El nombre de usuario debe ser una palabra de 5 a 10 caracteres, todos alfabéticos
	La contraseña debe ser una palbra con una logintud minima de 8 caracteres
'''
while True:
    nombre = input("Introduce tu nombre: ")

    if len(nombre) in range(5, 11) and nombre.isalpha():
        print("Nombre completado correctamente")
        break
    else:
        print("Nombre incorrecto, debe tener entre 5 y 10 caracteres y solo letras")


while True:
    contrasenia = input("Password: ")

    if len(contrasenia) >= 8 and contrasenia.isalnum():
        print("Contraseña completada correctamente")
        break
    else:
        print("Contraseña incorrecta, debe tener mínimo 8 caracteres y ser alfanumérica")