# IFs anidados

# Ejemplo 3
print("########## Ejemplo 3 ##########")

nombre = "Luis Escobar"
ciudad = "Barcelona"
continente = "Europa"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")
    
    if continente != "Europa":
        print("El usuario No es Europeo")
    else:
        print(f"Es Europeo y de {ciudad}")

else:
    print(f"{nombre} No es mayor de edad")