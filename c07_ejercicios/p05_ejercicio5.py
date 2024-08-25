# Ejercicio 5

"""
Ejercicio 5. Hacer un programa que muestre todos los 
números entre dos números que diga el usuario
"""
# Pedir al usuario que introduzca dos números
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Identificar el número menor y mayor
menor = min(numero1, numero2)
mayor = max(numero1, numero2)

# Mostrar todos los números entre los dos números dados
print(f"Los números entre {menor} y {mayor} son:")

for num in range(menor , mayor + 1):
    print(num)

# Pedir al usuario que introduzca dos números
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):
        print(contador)
else:
    print("El número 1 debe ser menor al numero 2")