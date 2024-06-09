# Esto es un comentario de una sola línea
print("Hola")
print("Mundo")


# Ejemplo de comentarios

# Este es un comentario de una sola línea que explica lo que hace el siguiente bloque de código.

# Solicitar al usuario que ingrese el primer número.
num1 = input("Ingrese el primer número: ")

# Solicitar al usuario que ingrese el segundo número.
num2 = input("Ingrese el segundo número: ")

# Convertir las entradas a números flotantes (decimales).
num1 = float(num1)
num2 = float(num2)

# Sumar los dos números y almacenar el resultado en una variable llamada 'suma'.
suma = num1 + num2

# Mostrar el resultado de la suma al usuario.
print("La suma de los dos números es:", suma)


# Ejemplo de múltiples líneas

"""
Este programa calcula el promedio de tres números ingresados por el usuario.
Primero, solicita al usuario que ingrese tres números.
Luego, suma estos números y divide la suma por tres para obtener el promedio.
Finalmente, muestra el promedio al usuario.
"""

# Solicitar al usuario que ingrese el primer número.
num1 = input("Ingrese el primer número: ")

# Solicitar al usuario que ingrese el segundo número.
num2 = input("Ingrese el segundo número: ")

# Solicitar al usuario que ingrese el tercer número.
num3 = input("Ingrese el tercer número: ")

"""
Convertir las entradas de texto a números flotantes.
Esto es necesario porque los valores ingresados por el usuario se leen como cadenas de texto,
pero necesitamos realizar operaciones matemáticas con ellos.
"""
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

"""
Calcular la suma de los tres números.
La suma es necesaria para calcular el promedio.
"""
suma = num1 + num2 + num3

"""
Calcular el promedio dividiendo la suma entre el número de valores (en este caso, tres).
El promedio es una medida del valor central de un conjunto de números.
"""
promedio = suma / 3

# Mostrar el resultado del promedio al usuario.
print("El promedio de los tres números es:", promedio)

