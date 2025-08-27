import random
from statistics import mode, median, mean

# --- Ejercicio 1 ---
print("=== Ejercicio 1 ===")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")


# --- Ejercicio 2 ---
print("\n=== Ejercicio 2 ===")
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# --- Ejercicio 3 ---
print("\n=== Ejercicio 3 ===")
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# --- Ejercicio 4 ---
print("\n=== Ejercicio 4 ===")
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# --- Ejercicio 5 ---
print("\n=== Ejercicio 5 ===")
contrasena = input("Ingrese una contraseña: ")
longitud = len(contrasena)
if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# --- Ejercicio 6 ---
print("\n=== Ejercicio 6 ===")
# Generar 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
try:
    moda = mode(numeros_aleatorios)
except:
    moda = None
    print("No se puede determinar la moda (sin repetición única).")

if moda is not None:
    if media > mediana > moda:
        print("Sesgo positivo o a la derecha")
    elif media < mediana < moda:
        print("Sesgo negativo o a la izquierda")
    elif abs(media - mediana) < 0.1 and abs(mediana - moda) < 0.1:
        print("Sin sesgo")
    else:
        print("La distribución no cumple claramente con ninguno de los criterios.")
else:
    print("No se puede determinar el sesgo sin moda.")


# --- Ejercicio 7 ---
print("\n=== Ejercicio 7 ===")
frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"
if frase and frase[-1] in vocales:
    print(frase + "!")
else:
    print(frase)


# --- Ejercicio 8 ---
print("\n=== Ejercicio 8 ===")
nombre = input("Ingrese su nombre: ")
opcion = input("Elija una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Primera en mayúscula): ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")


# --- Ejercicio 9 ---
print("\n=== Ejercicio 9 ===")
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


# --- Ejercicio 10 ---
print("\n=== Ejercicio 10 ===")
hemisferio = input("Ingrese su hemisferio (N/S): ").strip().upper()
if hemisferio not in ["N", "S"]:
    print("Hemisferio no válido. Ingrese N o S.")
else:
    try:
        mes = int(input("Ingrese el mes (1-12): "))
        dia = int(input("Ingrese el día (1-31): "))
        if mes < 1 or mes > 12 or dia < 1 or dia > 31:
            print("Fecha no válida")
        else:
            # Días acumulados por mes (sin año bisiesto)
            dias_acumulados = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            dia_del_año = dias_acumulados[mes - 1] + dia

            # Ajuste aproximado para fechas de estaciones
            if hemisferio == "N":
                if (dia_del_año >= 355) or (dia_del_año <= 79):       # 21 dic - 20 mar
                    estacion = "Invierno"
                elif 80 <= dia_del_año <= 171:                        # 21 mar - 20 jun
                    estacion = "Primavera"
                elif 172 <= dia_del_año <= 264:                       # 21 jun - 20 sep
                    estacion = "Verano"
                else:                                                 # 21 sep - 20 dic
                    estacion = "Otoño"
            else:  # Hemisferio Sur
                if (dia_del_año >= 355) or (dia_del_año <= 79):       # 21 dic - 20 mar
                    estacion = "Verano"
                elif 80 <= dia_del_año <= 171:                        # 21 mar - 20 jun
                    estacion = "Otoño"
                elif 172 <= dia_del_año <= 264:                       # 21 jun - 20 sep
                    estacion = "Invierno"
                else:                                                 # 21 sep - 20 dic
                    estacion = "Primavera"
            print(f"Usted se encuentra en la estación: {estacion}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos para mes y día.")


