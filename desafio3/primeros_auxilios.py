#Pasos a seguir de Primeros auxilios
#respuestas del usuario
si = "si"
no = "no"
#Preguntas
print("Responda las siguientes preguntas con las opciones si y no.")


estimulos = str(input("¿El paciente responde a estímulos?: ")).lower()#Pregunta1
if estimulos == "si":
    print("Valora la necesidad de llevarlo al hospital más cercano.") 
else:
    print("Abrir la vía aérea.")
    respira = str(input("¿El paciente respira? : ")).lower()#Pregunta2

    if respira == "si":
        print("Permitirle posicion de suficiente ventilacion.")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia.")
        signos_de_vida = str(input("¿El paciente tiene signos de vida?: ")).lower()#Pregunta3
        if signos_de_vida == "no":
            print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
            while signos_de_vida == "no":
                ambulancia = str(input("¿Llego la ambulancia?: ")).lower()#Pregunta4
                if ambulancia == "si":
                    print("fin")
                    break
                
        elif signos_de_vida == "si":
            print("Reevaluar a la espera de la ambulancia.")
            ambulancia = str(input("¿Llego la ambulancia?: ")).lower()
            if ambulancia == "si:":
                print("fin")

