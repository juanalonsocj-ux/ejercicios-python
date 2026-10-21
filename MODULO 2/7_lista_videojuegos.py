videojuegos = ["minecraft", "fortnite", "roblox", "fifa", "gta"]

buscar = input("Introduce un videojuego: ").lower()

if buscar in videojuegos:
    print("Videojuego encontrado")
else:
    print("Videojuego no encontrado")