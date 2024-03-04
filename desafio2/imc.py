#solicitar los datos al usuario
peso = float (input ("Ingrese su peso en Kg: "))
altura_cm = float (input ("Ingrese su altura en centimetros: "))

#convertir centimetros a metros
altura_m = altura_cm * 0.01

#calcular imc
imc = (peso / altura_m**2)

#mostrar imc
print(f"Su IMC es {imc:.2f} Kg/m2")

#mostrar clasificacion OMS
if imc < 18.5:
    print("La clasificación OMS es Bajo peso")
elif  18.5 <= imc < 25: 
    print("La clasificación OMS es Adecuado")
elif  25 <= imc < 30: 
    print("La clasificación OMS es Sobrepeso")
elif  30 <= imc < 35: 
    print("La clasificación OMS es Obesidad Grado I")
elif  35 <= imc < 40: 
    print("La clasificación OMS es Obesidad Grado II")
elif imc >= 40: 
    print("La clasificación OMS es Obesidad Grado III")


