# Ejercicio 10

"""
Ejercicio 10.  El programa tiene que pedir la nota de 15 alumnos 
y sacar por pantalla cuantos han aprobado y cuantos han suspendido.
"""

# Pedir al usuario el número de alumnos
num_alumnos = int(input("Ingrese el número de alumnos: "))

# Inicializar contadores para aprobados y suspendidos
aprobados = 0
suspendidos = 0

# Inicializar el contador de alumnos procesados
contador = 0

# Bucle while para ingresar notas hasta que se procese el número de alumnos especificado
while contador < num_alumnos:
    # Pedir al usuario que ingrese la nota de cada alumno
    nota = float(input(f"Ingrese la nota del alumno {contador + 1}: "))
    
    # Comprobar si la nota es mayor o igual a 10 para aprobar, si no, suspende
    if nota >= 10:
        aprobados += 1
    else:
        suspendidos += 1
    
    # Incrementar el contador de alumnos procesados
    contador += 1

# Imprimir los resultados
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")