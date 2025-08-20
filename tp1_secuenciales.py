import math

# 1) "Hola Mundo!".

print("Hola Mundo!")

# 2) Saludo

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# 3) Pedir nombre, apellido, edad y lugar de residencia

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# 4) Pedir el radio de un círculo e imprima área y perímetro

radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

# 5) Convertir segundos a horas

segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# 6) Imprimir la tabla de multiplicar de un número

numero = int(input("Ingresa un número para su tabla de multiplicar: "))
print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 7) Operar con dos números enteros

num1 = int(input("Ingresa el primer número entero (distinto de 0): "))
num2 = int(input("Ingresa el segundo número entero (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"\nResultados:")
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} × {num2} = {multiplicacion}")
print(f"{num1} ÷ {num2} = {division:.2f}")

# 8) Calcular el índice de masa corporal (IMC)

altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

# 9) Convertir Celsius a Fahrenheit

celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# 10) Calcular el promedio de 3 números

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")