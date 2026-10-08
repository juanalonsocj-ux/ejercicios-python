producto = input("Introduce el nombre del producto: ")


precio = float(input("Introduce el precio unitario: "))

cantidad = int(input("Introduce la cantidad: "))

importe_inicial = precio * cantidad


if cantidad >= 5:
   
    descuento = importe_inicial * 0.10
else:
    
    descuento = 0


precio_final = importe_inicial - descuento

print("Producto:", producto)
print("Importe inicial:", importe_inicial)
print("Descuento aplicado:", descuento)


print("Total a pagar:", precio_final)