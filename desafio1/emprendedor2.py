#Advertencia al usuario
print("Advertencia! Ingresar solo valores numericos para un correcto funcionamiento del programa.")

#Solicitar datos
p_normal =float(input("Ingrese el precio de suscripción usuario normal: ")) 
u_normal =float(input("Ingrese el numero de usuarios normal: ")) 
u_premium = float(input("Ingrese el numero de usuarios premium: "))
gt =float(input("Ingrese gastos totales: "))

#valor de la suscripcion de usuarios premium
p_upremium = p_normal * 1.5
print(f"suscripcion usuario premium: {p_upremium} ")

#calcular utilidades
utilidades_total = ((p_upremium * u_premium) + (p_normal * u_normal)) - gt

#Mostrar resultado de utilidades
print(f"Las utilidades de usuarios normal y premium es: {utilidades_total} ")

