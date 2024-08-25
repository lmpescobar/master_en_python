# Ejemplo con el bucle while

# Ejemplo

print("########## Ejemplo ##########")
numero_usuario = int(input("De que numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla del {numero_usuario} ###")

contador = 1
while contador <= 100:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador += 1
else:
    ("Tabla terminada.")