# Ejercicio 7

"""
Ejercicio 7. Hacer un programa que muestre todos los números 
impares entre dos números que decida el usuario.
"""

# Pedir al usuario que introduzca dos números
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Identificar el número menor y mayor
menor = min(numero1, numero2)
mayor = max(numero1, numero2)

# Mostrar todos los números entre los dos números dados
print(f"Los números entre {menor} y {mayor} son:")

for x in range(menor, (mayor + 1)):
    if x % 2 == 0:
        print(f"{x} es PAR")
    else:
        print(f"{x} es IMPAR")