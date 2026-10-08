def get_nombre_completo(nombre: str, apellido: str):
	nombre_completo = nombre.title() + " " + apellido.title() 
	#devuelve la concatenacíon de nombre y apellido 
	return nombre_completo

def get_nombre_y_edad(nombre: str, edad: int):	
	nombre_y_edad = nombre.title() + " tiene " + str(edad) + " años."
	#devuelve la concatenación de nobre y edad
	return nombre_y_edad