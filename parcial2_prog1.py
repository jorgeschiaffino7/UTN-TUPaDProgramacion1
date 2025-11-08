import csv
import os

ARCHIVO_CSV = "catalogo.csv"

def cargar_catalogo():
    catalogo = []
    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                catalogo.append({
                    "TITULO": fila["TITULO"],
                    "CANTIDAD": int(fila["CANTIDAD"])
                })
    return catalogo

def guardar_catalogo(catalogo):
    with open(ARCHIVO_CSV, 'w', encoding='utf-8', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
        escritor.writeheader()
        escritor.writerows(catalogo)

def normalizar_titulo(titulo):
    return titulo.strip().lower()

def buscar_libro(catalogo, titulo):
    titulo_norm = normalizar_titulo(titulo)
    for i, libro in enumerate(catalogo):
        if normalizar_titulo(libro["TITULO"]) == titulo_norm:
            return i
    return -1

def validar_entero_positivo(texto):
    if texto.isdigit():
        return int(texto)
    return -1

def ingresar_titulos(catalogo):
    cantidad_str = input("¿Cuántos libros desea cargar? ")
    cantidad = validar_entero_positivo(cantidad_str)
    
    if cantidad <= 0:
        print("Cantidad inválida.")
        return
    
    for i in range(cantidad):
        print(f"\nLibro {i + 1}:")
        while True:
            titulo = input("Título: ").strip()
            if not titulo:
                print("El título no puede estar vacío.")
                continue
            if buscar_libro(catalogo, titulo) != -1:
                print("El título ya existe en el catálogo.")
                continue
            break
        
        while True:
            cantidad_str = input("Cantidad de ejemplares: ")
            cantidad_ejem = validar_entero_positivo(cantidad_str)
            if cantidad_ejem < 0:
                print("La cantidad debe ser un número entero mayor o igual a 0.")
                continue
            break
        
        catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad_ejem})
    
    guardar_catalogo(catalogo)
    print(f"\n{cantidad} libro(s) ingresado(s) correctamente.")

def ingresar_ejemplares(catalogo):
    titulo = input("Título del libro: ").strip()
    indice = buscar_libro(catalogo, titulo)
    
    if indice == -1:
        print("El título no existe en el catálogo.")
        return
    
    while True:
        cantidad_str = input("Cantidad a agregar: ")
        cantidad = validar_entero_positivo(cantidad_str)
        if cantidad < 0:
            print("La cantidad debe ser un número entero mayor o igual a 0.")
            continue
        break
    
    catalogo[indice]["CANTIDAD"] += cantidad
    guardar_catalogo(catalogo)
    print(f"Se agregaron {cantidad} ejemplares. Total: {catalogo[indice]['CANTIDAD']}")

def mostrar_catalogo(catalogo):
    if not catalogo:
        print("El catálogo está vacío.")
        return
    
    print("\n--- CATÁLOGO COMPLETO ---")
    for libro in catalogo:
        print(f"{libro['TITULO']}: {libro['CANTIDAD']} ejemplares")

def consultar_disponibilidad(catalogo):
    titulo = input("Título a consultar: ").strip()
    indice = buscar_libro(catalogo, titulo)
    
    if indice == -1:
        print("El título no existe en el catálogo.")
        return
    
    print(f"'{catalogo[indice]['TITULO']}' tiene {catalogo[indice]['CANTIDAD']} ejemplares disponibles.")

def listar_agotados(catalogo):
    agotados = [libro for libro in catalogo if libro["CANTIDAD"] == 0]
    
    if not agotados:
        print("No hay libros agotados.")
        return
    
    print("\n--- LIBROS AGOTADOS ---")
    for libro in agotados:
        print(f"- {libro['TITULO']}")

def agregar_titulo(catalogo):
    while True:
        titulo = input("Título del nuevo libro: ").strip()
        if not titulo:
            print("El título no puede estar vacío.")
            continue
        if buscar_libro(catalogo, titulo) != -1:
            print("El título ya existe en el catálogo.")
            continue
        break
    
    while True:
        cantidad_str = input("Cantidad inicial de ejemplares: ")
        cantidad = validar_entero_positivo(cantidad_str)
        if cantidad < 0:
            print("La cantidad debe ser un número entero mayor o igual a 0.")
            continue
        break
    
    catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    guardar_catalogo(catalogo)
    print(f"Libro '{titulo}' agregado correctamente con {cantidad} ejemplares.")

def actualizar_ejemplares(catalogo):
    print("\n1. Préstamo")
    print("2. Devolución")
    opcion = input("Seleccione operación: ")
    
    titulo = input("Título del libro: ").strip()
    indice = buscar_libro(catalogo, titulo)
    
    if indice == -1:
        print("El título no existe en el catálogo.")
        return
    
    match opcion:
        case "1":
            if catalogo[indice]["CANTIDAD"] == 0:
                print("No hay ejemplares disponibles para préstamo.")
                return
            catalogo[indice]["CANTIDAD"] -= 1
            guardar_catalogo(catalogo)
            print(f"Préstamo realizado. Ejemplares restantes: {catalogo[indice]['CANTIDAD']}")
        case "2":
            catalogo[indice]["CANTIDAD"] += 1
            guardar_catalogo(catalogo)
            print(f"Devolución realizada. Ejemplares disponibles: {catalogo[indice]['CANTIDAD']}")
        case _:
            print("Opción inválida.")

def menu_principal():
    catalogo = cargar_catalogo()
    
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1. Ingresar títulos (múltiples)")
        print("2. Ingresar ejemplares")
        print("3. Mostrar catálogo")
        print("4. Consultar disponibilidad")
        print("5. Listar agotados")
        print("6. Agregar título")
        print("7. Actualizar ejemplares (préstamo/devolución)")
        print("8. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        match opcion:
            case "1":
                ingresar_titulos(catalogo)
            case "2":
                ingresar_ejemplares(catalogo)
            case "3":
                mostrar_catalogo(catalogo)
            case "4":
                consultar_disponibilidad(catalogo)
            case "5":
                listar_agotados(catalogo)
            case "6":
                agregar_titulo(catalogo)
            case "7":
                actualizar_ejemplares(catalogo)
            case "8":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()