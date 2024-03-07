from string import ascii_lowercase

contraseña = input("Ingrese contraseña: ") #contraseña a buscar
contador = 0
alfabeto = ascii_lowercase


for letra in contraseña:
    for elemento in alfabeto:
        contador += 1
        if letra == elemento:
            break
print(f"La contraseña fue forzada en {contador} intentos")
    

