# Ejercicio 8

"""
Ejercicio 8. Cuanto es el x porciento de x numero?
20 % de 150
"""

# Pedir al usuario que introduzca dos números
numero1 = int(input("% Introduce el porcentaje a calcular %: "))
numero2 = int(input("Introduce el numero: "))

operacion = (numero2 * (numero1/100))

print(f"El {numero1}% de {numero2} es: {operacion}")