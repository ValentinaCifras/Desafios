import os
import math

#Advertencia al usuario
print("Advertencia! Ingresar solo valores numericos para un correcto funcionamiento del programa.")

#solicitar datos
r = float (input("Ingrese el radio en Kilómetros: ")) 
g = float (input("Ingrese la constante g: "))

#convertir kilometros en metros
r_m = r * 1000

#formula para calcular velocidad de escape
v_e = math.sqrt(2 * r_m * g)

#mostrar resultado
print(f"La velocidad de escape es: {v_e:.1f} [m/s]")