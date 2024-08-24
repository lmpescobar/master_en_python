# Más ejemplos con los condicionales

# Ejemplo 6
print("########## Ejemplo 6 ##########")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana :(")

# Ejemplo 7
print("########## Ejemplo 7 ##########")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} No un pais de habla hispana !!")
else:
    print(f"{pais} Si es un pais de habla hispana :)")

# Ejemplo 8
print("########## Ejemplo 8 ##########")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} No un pais de habla hispana !!")
else:
    print(f"{pais} Si es un pais de habla hispana :)")