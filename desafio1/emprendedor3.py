#Advertencia al usuario
print("Advertencia! Ingresar solo valores numericos para un correcto funcionamiento del programa.")

# Solicitar Datos
P =float(input("Ingrese el precio de suscripción: ")) 
U =float(input("Ingrese el numero de usuarios: ")) 
Gt =float(input("Ingrese gastos totales: ")) 

#Formula para calcular utilidades
Utilidades_año_actual = P * U - Gt

#Solicitar utilidades año anterior
utilidades_año_anterior =float(input("Ingrese las utilidades del año anterior: ")) 

#calcular razon
razon = Utilidades_año_actual / utilidades_año_anterior

#Mostrar resultado
print(f"Las utilidades de este año son: {Utilidades_año_actual}")

#Mostrar utilidades y razon
print(f"La razon de las utilidades del año actual y año anterior es: {razon:.2f} ")

