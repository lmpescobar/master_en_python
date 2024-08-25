# Bucle while

"""
# BUCLE WHILE
Estructura de control que itera o repita la ejecución de una
serie de instrucciones tantas veces como sea necesario,
hasta que deje de cumplirse la condición

while condición:
    bloque de instrucciones
    actualización de contador
"""

contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1

contador = 1

print("------------------------------------------")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + " , " + str(contador)
    contador += 1

print(muestrame)