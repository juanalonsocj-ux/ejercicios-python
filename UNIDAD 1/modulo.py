

def suma(a, b):
	return a + b
 
def resta(a, b):
	return a - b

def producto(a, b):
	return a * b

def division_entera(a, b):
	return int(a / b)

def modulo(a, b):
	return a % b

def es_par(numero :int):
	if numero % 2 == 0:
		return f"{numero} es Par"
	else:
		return f"{numero} es Impar"

def aplicar_IVA(precio_bruto: float, porcentaje: float =21.0):
	return precio_bruto + (precio_bruto *  porcentaje / 100) 
