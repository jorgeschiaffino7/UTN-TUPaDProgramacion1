# 1) Crear una lista con las notas de 10 estudiantes.
notas = [8.5, 7.2, 9.0, 6.8, 8.0, 9.5, 7.0, 8.8, 6.5, 9.2]

# • Mostrar la lista completa.
print("Lista de notas:")
for nota in notas:
    print(nota)

# • Calcular y mostrar el promedio.
promedio = sum(notas) / len(notas)
print(f"\nEl promedio es: {promedio:.2f}")

# • Indicar la nota más alta y la más baja.
nota_max = max(notas)
nota_min = min(notas)
print(f"La nota más alta es: {nota_max}")
print(f"La nota más baja es: {nota_min}")


# 2) Pedir al usuario que cargue 5 productos en una lista.
productos = []
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)

# • Mostrar la lista ordenada alfabéticamente.
productos_ordenados = sorted(productos)
print("\nLista de productos ordenada:")
for prod in productos_ordenados:
    print(prod)

# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
producto_a_eliminar = input("\nIngrese el nombre del producto que desea eliminar: ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print(f"Producto '{producto_a_eliminar}' eliminado.")
else:
    print(f"El producto '{producto_a_eliminar}' no se encuentra en la lista.")

print("\nLista actualizada:")
for prod in productos:
    print(prod)

import random

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista original:")
for num in numeros:
    print(num)

# • Crear una lista con los pares y otra con los impares.
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

# • Mostrar cuántos números tiene cada lista.
print(f"\nLista de pares ({len(pares)} elementos):")
for par in pares:
    print(par)

print(f"\nLista de impares ({len(impares)} elementos):")
for impar in impares:
    print(impar)

# 4) Dada una lista con valores repetidos:
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 9, 1]

# • Crear una nueva lista sin elementos repetidos.
lista_sin_duplicados = []
for elemento in lista_con_duplicados:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)

# • Mostrar el resultado.
print("Lista sin duplicados:")
for elem in lista_sin_duplicados:
    print(elem)

# 5) Crear una lista con los nombres de 8 estudiantes.
estudiantes = ["Ana", "Carlos", "Beatriz", "David", "Elena", "Fernando", "Gabriela", "Hugo"]

print("Lista actual de estudiantes:")
for est in estudiantes:
    print(est)

# • Preguntar al usuario si quiere agregar o eliminar.
accion = input("\n¿Desea 'agregar' un estudiante o 'eliminar' uno? (escriba 'agregar' o 'eliminar'): ").lower()

if accion == 'agregar':
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print(f"Estudiante '{nuevo_estudiante}' agregado.")
elif accion == 'eliminar':
    estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
        print(f"Estudiante '{estudiante_a_eliminar}' eliminado.")
    else:
        print("El estudiante no se encuentra en la lista.")
else:
    print("Opción no válida.")

# • Mostrar la lista final actualizada.
print("\nLista final de estudiantes:")
for est in estudiantes:
    print(est)

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha.
lista = [1, 2, 3, 4, 5, 6, 7]
print("Lista original:", lista)

# Rotar hacia la derecha: el último elemento pasa a ser el primero.
ultimo_elemento = lista.pop()  # Quita el último elemento
lista.insert(0, ultimo_elemento)  # Lo inserta al principio

print("Lista rotada:", lista)

# 7) Crear una matriz de 7x2 con temperaturas mínimas y máximas.
# Cada sublista representa un día: [mínima, máxima]
temperaturas = [
    [10, 25], # Lunes
    [12, 27], # Martes
    [9, 23],  # Miércoles
    [11, 26], # Jueves
    [13, 28], # Viernes
    [15, 30], # Sábado
    [14, 29]  # Domingo
]

# • Calcular el promedio de las mínimas y el de las máximas.
minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]

promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)

print(f"Promedio de temperaturas mínimas: {promedio_min:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}°C")

# • Mostrar en qué día se registró la mayor amplitud térmica.
amplitudes = [dia[1] - dia[0] for dia in temperaturas]
dia_mayor_amplitud = amplitudes.index(max(amplitudes)) + 1  # +1 porque los días empiezan en 1

print(f"El día con mayor amplitud térmica fue el día {dia_mayor_amplitud}.")

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# Cada fila es un estudiante, cada columna una materia.
notas = [
    [8.5, 7.0, 9.0], # Estudiante 1
    [6.5, 8.0, 7.5], # Estudiante 2
    [9.0, 9.5, 8.5], # Estudiante 3
    [7.0, 6.5, 8.0], # Estudiante 4
    [8.0, 8.5, 9.0]  # Estudiante 5
]

# • Mostrar el promedio de cada estudiante.
print("Promedio por estudiante:")
for i, estudiante in enumerate(notas):
    promedio_est = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i+1}: {promedio_est:.2f}")

# • Mostrar el promedio de cada materia.
num_materias = len(notas[0])
print("\nPromedio por materia:")
for j in range(num_materias):
    suma_materia = sum(notas[i][j] for i in range(len(notas)))
    promedio_mat = suma_materia / len(notas)
    print(f"Materia {j+1}: {promedio_mat:.2f}")

# 9) Representar un tablero de Ta-Te-Ti (3x3).
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print()

# Inicializar
print("Tablero inicial:")
mostrar_tablero(tablero)

jugador_actual = "X"

for turno in range(9):  # Máximo 9 turnos
    print(f"Turno del jugador {jugador_actual}")
    fila = int(input("Ingrese la fila (0, 1, 2): "))
    columna = int(input("Ingrese la columna (0, 1, 2): "))

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador_actual
        mostrar_tablero(tablero)

        # Cambiar de jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"
    else:
        print("¡Esa posición ya está ocupada! Intente de nuevo.")
        turno -= 1  # Para que el mismo jugador intente de nuevo

print("Juego terminado.")

# 10) Matriz de 4 productos x 7 días.
# Valores inventados para el ejemplo.
ventas = [
    [10, 15, 12, 20, 18, 22, 25], # Producto 1
    [8, 12, 10, 15, 14, 18, 20],  # Producto 2
    [5, 8, 7, 10, 9, 12, 15],     # Producto 3
    [20, 25, 22, 30, 28, 35, 40]  # Producto 4
]

# • Mostrar el total vendido por cada producto.
print("Total vendido por producto:")
for i, producto in enumerate(ventas):
    total_producto = sum(producto)
    print(f"Producto {i+1}: {total_producto} unidades")

# • Mostrar el día con mayores ventas totales.
ventas_por_dia = [sum(ventas[i][j] for i in range(len(ventas))) for j in range(len(ventas[0]))]
dia_max_ventas = ventas_por_dia.index(max(ventas_por_dia)) + 1
print(f"\nEl día con mayores ventas totales fue el día {dia_max_ventas}.")

# • Indicar cuál fue el producto más vendido en la semana.
totales_productos = [sum(producto) for producto in ventas]
producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print(f"El producto más vendido en la semana fue el producto {producto_mas_vendido}.")

