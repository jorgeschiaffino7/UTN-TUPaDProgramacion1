# --- Ejercicio 1: Números del 0 al 100: ---
for i in range(101):
    print(i)

# --- Ejercicio 2: Cantidad de dígitos: ---

num = abs(int(input("Número: ")))
print(len(str(num)) if num != 0 else 1)

# --- Ejercicio 3: Suma entre dos números (excluyéndolos): ---

a, b = int(input()), int(input())
inicio, fin = sorted([a, b])
print(sum(range(inicio + 1, fin)))

# --- Ejercicio 4: Suma hasta ingresar 0: ---

total = 0
while True:
    n = int(input())
    if n == 0: break
    total += n
print(total)


# --- Ejercicio 5: Adivinar número aleatorio: ---

import random
num = random.randint(0,9)
intentos = 0
while int(input("Adivina (0-9): ")) != num:
    intentos += 1
print("¡Acertaste! Intentos:", intentos + 1)

# --- Ejercicio 6: Pares del 100 al 0 (decreciente): ---

for i in range(100, -1, -2):
    print(i)

# --- Ejercicio 7: Suma de 0 a N: ---

n = int(input("N: "))
print(sum(range(n + 1)))

# --- Ejercicio 8:  Estadísticas de 100 números: ---

pares = impares = negativos = positivos = 0
for _ in range(100):
    n = int(input())
    if n % 2 == 0: pares += 1
    else: impares += 1
    if n > 0: positivos += 1
    elif n < 0: negativos += 1
print(pares, impares, negativos, positivos)


# --- Ejercicio 9: Media de 100 números: ---

total = 0
for _ in range(100):
    total += int(input())
print(total / 100)

# --- Ejercicio 10: Invertir dígitos: ---

num = input("Número: ")
print(int(num[::-1]))





