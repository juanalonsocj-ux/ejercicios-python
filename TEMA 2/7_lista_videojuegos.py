videojuegos = ["Minecraft", "Fortnite", "Roblox", "FIFA", "GTA-VI"]

buscar = input("Ingresa el videojuego que buscas: ").lower()

if buscar in videojuegos:
    print("Encontrado")
else:
    print("No encontrado")