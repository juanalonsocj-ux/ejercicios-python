
frutas = ["manzana", "pera", "plátano", "naranja", "uva"]


print("Primera fruta:", frutas[0])
print("Última fruta:", frutas[-1])
print("Número de frutas:", len(frutas))

frutas.append("fresa")

print("Lista actualizada:", frutas)

for fruta in frutas:
    print(fruta)
    
print(*frutas, sep=" , ")