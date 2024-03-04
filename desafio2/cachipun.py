from random import choice

#solicitar jugada usuario
usuario = input("Ingresa tu jugada: Piedra, Papel o Tijera: ")
usuario = usuario.capitalize()
print(f"Tu jugaste: {usuario}")

#jugada computador   
opciones = ['Piedra', 'Papel', 'Tijera']
computador = choice(opciones)
print(f"Computador jugó: {computador} ")

#validar jugada del usuario
if usuario != 'Piedra' and usuario != 'Papel' and usuario !='Tijera':
    print("Argumento inválido: Debe ser Piedra, Papel o Tijera.")
#comparando opciones
elif usuario == computador:
    print("Empate!")
elif usuario == 'Piedra' and computador == 'Tijera':
    print("Ganaste!")
elif usuario == 'Piedra' and computador == 'Papel':
    print("Perdiste!")
elif usuario == 'Papel' and computador == 'Piedra':
    print("Ganaste!")
elif usuario == 'Papel' and computador == 'Tijera':
    print("Perdiste!")
elif usuario == 'Tijera' and computador == 'Papel':
    print("Ganaste!")
elif usuario == 'Tijera' and computador == 'Piedra':
    print("Perdiste!")

