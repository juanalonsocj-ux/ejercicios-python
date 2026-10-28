from ej13_operaciones import sumar, restar, multiplicar, dividir
 
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
 
print(f"El resultado de {a} + {b} es {sumar(a,b)}")
print(f"El resultado de {a} - {b} es {restar(a,b)}")
print(f"El resultado de {a} * {b} es {multiplicar(a,b)}")
print(f"El resultado de {a} / {b} es {dividir(a,b)}")