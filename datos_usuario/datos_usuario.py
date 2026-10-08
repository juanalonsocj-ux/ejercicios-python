from nombres import get_nombre_completo, get_nombre_y_edad

nombre = str(input("introduce tu nombre: "))

apellido = str(input("introduce apellido: "))

edad = int(input("introduce tu edad: "))

print(f"Tu nombre completo es: {get_nombre_completo(nombre,apellido)}")
print(get_nombre_y_edad(get_nombre_completo(nombre,apellido),edad))
