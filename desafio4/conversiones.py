import sys

#solicitar tasas de conversion
print("\nIngresar tasas de conversion en este orden: Sol, Peso Argentino, Dolar Americano y Peso Chileno\n")

sol_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3]) 
peso_chileno = int(sys.argv[4])

#convertir peso chileno a distintas tasas
resultado_sol = peso_chileno * sol_peruano
resultado_arg = peso_chileno * peso_argentino
resultado_dolar = peso_chileno * dolar_americano

#mostrar resultados
print(f"""Los {peso_chileno} Pesos Chilenos equivalen a \n
       {resultado_sol:.1f} Soles Peruanos \n
       {resultado_arg:.1f} Pesos Argentinos \n
       {resultado_dolar:.1f} Dolar Americano.""")