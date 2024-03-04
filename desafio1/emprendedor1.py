#Advertencia al usuario
print("Advertencia! Ingresar solo valores numericos para un correcto funcionamiento del programa.")

# Solicitar Datos
p =float(input("Ingrese el precio de suscripción: ")) 
u =float(input("Ingrese el numero de usuarios: ")) 
gt =float(input("Ingrese gastos totales: ")) 


#Formula para calcular utilidades
utilidades = p * u - gt

#Mostrar resultado
print(f"Las utilidades del proyecto son: {utilidades}")

