# Operadores lógicos y múltiples condiciones

# Operadores lógicos
"""
and = y

or = o

! = negación

not = no 
"""

# Ejemplo 5
print("########## Ejemplo 5 ##########")

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("Tienes edad de trabajar? Introduce tu edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar !!")
else:
    print("No esta en edad de trabajar")