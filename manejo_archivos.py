# 1. Crear archivo inicial
with open('productos.txt', 'w') as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,250,15\n")
    archivo.write("Mochila,3500,8\n")

# 2. Leer y mostrar productos
print("=== PRODUCTOS ===")
with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        print(f"Producto: {datos[0]} | Precio: ${datos[1]} | Cantidad: {datos[2]}")

# 3. Agregar producto desde teclado
nombre = input("\nIngrese nombre del producto: ")
precio = input("Ingrese precio: ")
cantidad = input("Ingrese cantidad: ")

with open('productos.txt', 'a') as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

# 4. Cargar productos en lista de diccionarios
productos = []
with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        producto = {
            'nombre': datos[0],
            'precio': float(datos[1]),
            'cantidad': int(datos[2])
        }
        productos.append(producto)

# 5. Buscar producto por nombre
buscar = input("\nIngrese nombre del producto a buscar: ")
encontrado = False
for producto in productos:
    if producto['nombre'].lower() == buscar.lower():
        print(f"\nProducto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Error: Producto no encontrado")

# 6. Guardar productos actualizados
with open('productos.txt', 'w') as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

print("\nArchivo actualizado correctamente")