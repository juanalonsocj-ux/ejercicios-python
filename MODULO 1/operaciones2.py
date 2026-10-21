from modulo import suma,resta,producto, division_entera

x = int(input("introduce 1er numero:"))

y = int(input("introduce 2do numero:"))

print(f"La suma {x} y {y} es = {suma(x,y)}")
print(f"El producto de {x} * {y} es = {producto(x,y)}")
print(f"La division entera  {x} y {y} es = {division_entera(x,y)}")
