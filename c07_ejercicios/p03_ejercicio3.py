# Ejercicio 3

"""
Ejercicio 3. Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros números naturales.
Resolverlo con for y con while
"""
"""
# WHILE

contador = 1
while contador <= 60:
    
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    
    contador += 1
"""
# FOR

for contador in range(0, 61):
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")