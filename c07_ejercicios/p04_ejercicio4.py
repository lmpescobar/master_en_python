# Ejercicio 4

"""
Ejercicio 4. Pedir dos números al usuario y hacer todas las operaciones básicas 
de una calculadora y mostrarlo por pantalla
"""

numero1 = int(input("Introduce el número 1: "))
numero2 = int(input("Introduce el número 2: "))

print("########## CALCULADORA ##########")

if numero1 >= 1 and numero2 >= 1:
    print(f"{numero1} + {numero2} = {numero1 + numero2}")
    print(f"{numero1} - {numero2} = {numero1 - numero2}")
    print(f"{numero1} * {numero2} = {numero1 * numero2}")
    
    if numero2 != 0:  # Verificación para evitar la división por cero
        print(f"{numero1} / {numero2} = {numero1 / numero2}")
    else:
        print("No se puede dividir entre cero.")
else:
    print("Ambos números deben ser mayores o iguales a 1.")