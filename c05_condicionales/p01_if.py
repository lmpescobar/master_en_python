# Condicional IF

"""
# Condicional if

SI se_cumple_esta_condicion:
    Ejecutar grupo de intrucciones
SI NO:
    se ejecutan otro grupo de intrucciones

if condicion:
    instrucciones
else:
    otras instrucciones
"""

# Ejemplo 1
print("########## Ejemplo 1 ##########")

# color = "rojo"
color = input("Adivina mi color favorito: ")

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("Color incorrecto !!")