import sys

#calcular factorial
def factorial(numero):
    factorial = 1
    for n in range(1, (numero + 1)):
        factorial = factorial * n
    return factorial

#calcular productoria
def productoria(lista):
    productoria = 1
    for n in lista:
        productoria *= n
    return productoria

#funcion calcular
def calcular(**kwargs):
    for key, value in kwargs.items():
        if "fact" in key:
            print(f"El factorial de {value} es {factorial(value)}")
        elif "prod" in key:
            print(f"La productoria de {value} es {productoria(value)}")


calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6)
    
    
    


