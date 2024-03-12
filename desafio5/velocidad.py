# calcular la velocidad promedio
def promedio(velocidad):
    return sum(velocidad) / len(velocidad)

#indice de las velocidades sobre el promedio
def sobre_promedio(velocidad,promedio):
    indice_sobrepromedio = []
    for indice, vel in enumerate(velocidad):
        if vel > promedio:
            indice_sobrepromedio.append(indice)
        
    return indice_sobrepromedio
    

velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 
            6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18,
            1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 
            1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 
            18, 10, 14, 5, 23, 20, 23, 21]

promedio_velocidad = promedio(velocidad)
indice = sobre_promedio(velocidad, promedio_velocidad)

print(indice)




