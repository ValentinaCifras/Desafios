with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

#convierto el archivo .txt en set para ver los caracteres distintos
caracteres_distintos = set(texto)

# con len cuento el numero de caracteres distintos
numero_caracteres_distintos = len(caracteres_distintos)

print(f"El numero de caracteres distintos es: {numero_caracteres_distintos}")

#separo .txt en palabras
separar_palabras = texto.split()
#con set identifico las palabras unicas, se eliminan las palabras repetidas
palabras_distintas = set(separar_palabras)
#con len cuento el numero de palabras distintas
numero_palabras_distintas = len(palabras_distintas)

print(f"El numero de palabras distintas es {numero_palabras_distintas}")





