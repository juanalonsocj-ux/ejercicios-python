from modulo import aplicar_IVA

try: 
	p_bruto = float(input("Introduce el precio bruto: "))
except ValueError:
	print("ERROR: Valor no valido!")
	exit(1)
try: 
	porcentaje = float(input("Introduce porcentaje de IVA (Rango: [1-100]: )"))

	p_neto = 0.0

	if 0 <= porcentaje <= 100:
		p_neto = aplicar_IVA(p_bruto, porcentaje)
		print(f"Precio sin IVA: {p_bruto:.2f}")
		print(f"Precio con IVA: {p_neto:.2f} ({porcentaje}%)")

	else: 
		print("ERROR: Valor fuera de rango")

except ValueError:
	print("ERROR: Valor no valido!")
	exit(1)


p_neto = aplicar_IVA(p_bruto, porcentaje)


