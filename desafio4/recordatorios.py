recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#agregar evento 2 de Febrero de 2021 6:00 “Empezar el Año”
recordatorios.insert (1, ["2021-02-01","06:00","Empezar el año"])

#Cambiar fecha al 16 de Julio
recordatorios[3] = ['2021-07-16', "13:00", "No hacer nada es feriado"] 

#eliminar evento "no trabajar"
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])

# agregar cena de navidad
recordatorios.insert (4,["2021-12-24","22:00","Cena de Navidad"])

# agregar cena de año nuevo
recordatorios.insert (7,["2021-12-31","22:00","Cena de Año Nuevo"])

# Output
for i in recordatorios:
    print(i)
