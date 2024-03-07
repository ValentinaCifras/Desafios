import sys
# Obtener el umbral de ventas
umbral = int(sys.argv[1])

# Diccionario de ventas
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

# Obtener como diccinario meses de ventas mayores al umbral
informe = {}
for mes, valor in ventas.items():
    if valor > umbral:
        informe [mes] = valor

# Imprimir el resultado
print(informe)
