import math

# Ejercicio 1
def imprimir_hola_mundo():

    print("Hola Mundo!")

# Ejercicio 2
def saludar_usuario(nombre):

    return f"Hola {nombre}!"

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):

    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
def calcular_area_circulo(radio):

    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):

    return 2 * math.pi * radio

# Ejercicio 5
def segundos_a_horas(segundos):

    return segundos / 3600

# Ejercicio 6
def tabla_multiplicar(numero):

    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
def operaciones_basicas(a, b):

    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

# Ejercicio 8
def calcular_imc(peso, altura):

    return peso / (altura ** 2)

# Ejercicio 9
def celsius_a_fahrenheit(celsius):

    return (celsius * 9/5) + 32

# Ejercicio 10
def calcular_promedio(a, b, c):

    return (a + b + c) / 3

# Programa principal
def main():
    """Función principal que ejecuta el menú de opciones."""
    while True:
        print("\n" + "="*50)
        print("PRÁCTICO 2: FUNCIONES EN PYTHON")
        print("="*50)
        print("1.  Imprimir Hola Mundo")
        print("2.  Saludar Usuario")
        print("3.  Información Personal")
        print("4.  Calcular Área y Perímetro de Círculo")
        print("5.  Convertir Segundos a Horas")
        print("6.  Tabla de Multiplicar")
        print("7.  Operaciones Básicas")
        print("8.  Calcular IMC")
        print("9.  Celsius a Fahrenheit")
        print("10. Calcular Promedio")
        print("0.  Salir")
        print("="*50)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("\n--- Ejercicio 1: Hola Mundo ---")
            imprimir_hola_mundo()
        
        elif opcion == "2":
            print("\n--- Ejercicio 2: Saludar Usuario ---")
            nombre = input("Ingresa tu nombre: ")
            saludo = saludar_usuario(nombre)
            print(saludo)
        
        elif opcion == "3":
            print("\n--- Ejercicio 3: Información Personal ---")
            nombre = input("Ingresa tu nombre: ")
            apellido = input("Ingresa tu apellido: ")
            edad = int(input("Ingresa tu edad: "))
            residencia = input("Ingresa tu lugar de residencia: ")
            informacion_personal(nombre, apellido, edad, residencia)
        
        elif opcion == "4":
            print("\n--- Ejercicio 4: Área y Perímetro de Círculo ---")
            radio = float(input("Ingresa el radio del círculo: "))
            area = calcular_area_circulo(radio)
            perimetro = calcular_perimetro_circulo(radio)
            print(f"Área del círculo: {area:.2f}")
            print(f"Perímetro del círculo: {perimetro:.2f}")
        
        elif opcion == "5":
            print("\n--- Ejercicio 5: Segundos a Horas ---")
            segundos = int(input("Ingresa la cantidad de segundos: "))
            horas = segundos_a_horas(segundos)
            print(f"{segundos} segundos equivalen a {horas:.2f} horas")
        
        elif opcion == "6":
            print("\n--- Ejercicio 6: Tabla de Multiplicar ---")
            numero = int(input("Ingresa un número: "))
            tabla_multiplicar(numero)
        
        elif opcion == "7":
            print("\n--- Ejercicio 7: Operaciones Básicas ---")
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            suma, resta, mult, div = operaciones_basicas(a, b)
            print(f"\nResultados:")
            print(f"Suma: {a} + {b} = {suma}")
            print(f"Resta: {a} - {b} = {resta}")
            print(f"Multiplicación: {a} × {b} = {mult}")
            print(f"División: {a} ÷ {b} = {div}")
        
        elif opcion == "8":
            print("\n--- Ejercicio 8: Calcular IMC ---")
            peso = float(input("Ingresa tu peso en kg: "))
            altura = float(input("Ingresa tu altura en metros: "))
            imc = calcular_imc(peso, altura)
            print(f"Tu IMC es: {imc:.2f}")
        
        elif opcion == "9":
            print("\n--- Ejercicio 9: Celsius a Fahrenheit ---")
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
        
        elif opcion == "10":
            print("\n--- Ejercicio 10: Calcular Promedio ---")
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            c = float(input("Ingresa el tercer número: "))
            promedio = calcular_promedio(a, b, c)
            print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")
        
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        
        else:
            print("\nOpción inválida. Por favor, selecciona una opción del menú.")
        
        input("\nPresiona ENTER para continuar...")

if __name__ == "__main__":
    main()
