# 1) Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("1)", precios_frutas)

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("2)", precios_frutas)

# 3) Lista solo con frutas
frutas = list(precios_frutas.keys())
print("3)", frutas)

# 4) Agenda telefónica
contactos = {}
print("\n4) Ingresa 5 contactos:")
for i in range(5):
    nombre = input(f"Nombre {i+1}: ")
    numero = input(f"Número {i+1}: ")
    contactos[nombre] = numero

buscar = input("¿Qué nombre buscas? ")
if buscar in contactos:
    print(f"El número de {buscar} es {contactos[buscar]}")
else:
    print("Contacto no encontrado")

# 5) Análisis de frase
frase = input("\n5) Ingresa una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador = {}
for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1
print("Frecuencia:", contador)

# 6) Promedios de alumnos
print("\n6) Ingresa 3 alumnos con sus notas:")
alumnos = {}
for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# 7) Sets de estudiantes
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {103, 104, 105, 106, 107}

print("\n7)")
print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# 8) Gestión de stock
stock = {}
while True:
    print("\n8) Stock de productos")
    producto = input("Producto (o 'salir'): ")
    if producto.lower() == 'salir':
        break
    
    if producto in stock:
        print(f"Stock actual: {stock[producto]}")
        agregar = int(input("Unidades a agregar: "))
        stock[producto] += agregar
    else:
        cantidad = int(input("Stock inicial: "))
        stock[producto] = cantidad
    
    print(f"Stock de {producto}: {stock[producto]}")

# 9) Agenda con tuplas
agenda = {
    ('Lunes', '09:00'): 'Reunión de equipo',
    ('Martes', '14:00'): 'Dentista',
    ('Miércoles', '10:00'): 'Clase de Python'
}

print("\n9) Agenda")
dia = input("Día: ")
hora = input("Hora: ")
evento = agenda.get((dia, hora), "No hay eventos")
print(f"Evento: {evento}")

# 10) Invertir diccionario país-capital
paises = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo'
}

capitales = {capital: pais for pais, capital in paises.items()}
print("\n10) Diccionario invertido:", capitales)