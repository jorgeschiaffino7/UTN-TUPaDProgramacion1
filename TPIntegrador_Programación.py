# TP Integrador - Gestión de Datos de Países
# Autor: [Nombre del estudiante]
# Descripción: Sistema para gestionar información de países con filtros, ordenamientos y estadísticas

import csv
import os

# Función para leer datos desde archivo CSV
def leer_paises_desde_csv(archivo_csv):
    """
    Lee los datos de países desde un archivo CSV y los convierte en una lista de diccionarios.
    
    Args:
        archivo_csv (str): Ruta del archivo CSV
        
    Returns:
        list: Lista de diccionarios con información de países
    """
    paises = []
    
    try:
        if not os.path.exists(archivo_csv):
            print(f"Error: El archivo {archivo_csv} no existe.")
            return []
            
        with open(archivo_csv, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            
            for fila in lector_csv:
                # Verificar que la fila no esté vacía y tenga todos los campos
                if (fila.get("nombre") and fila.get("poblacion") and 
                    fila.get("superficie") and fila.get("continente")):
                    
                    try:
                        # Convertir población y superficie a enteros
                        pais = {
                            "nombre": fila["nombre"].strip(),
                            "poblacion": int(fila["poblacion"]),
                            "superficie": int(fila["superficie"]),
                            "continente": fila["continente"].strip()
                        }
                        paises.append(pais)
                    except ValueError as e:
                        print(f"Error al procesar la fila {fila}: {e}")
                        continue
                    
        print(f"Se cargaron {len(paises)} países desde {archivo_csv}")
        return paises
        
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {archivo_csv}")
        return []
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return []

# Cargar datos desde CSV
paises = leer_paises_desde_csv("paises.csv")

# Funciones principales del sistema

def buscar_pais(paises):
    """
    Busca países por nombre con coincidencia parcial (insensible a mayúsculas/minúsculas).
    
    Args:
        paises (list): Lista de diccionarios con información de países
    """
    if not paises:
        print("No hay datos de países cargados.")
        return
        
    nombre_pais = input("Ingrese el país que desea buscar: ").strip()
    
    if not nombre_pais:
        print("Debe ingresar un nombre de país.")
        return
    
    paises_encontrados = []
    
    for pais in paises:
        if nombre_pais.lower() in pais["nombre"].lower():
            paises_encontrados.append(pais)
    
    if paises_encontrados:
        print(f"\nSe encontraron {len(paises_encontrados)} país(es) que coinciden con '{nombre_pais}':")
        print("-" * 50)
        for pais in paises_encontrados:
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']:,}")
            print(f"Superficie: {pais['superficie']:,} km²")
            print(f"Continente: {pais['continente']}")
            print("-" * 50)
    else:
        print(f"No se encontraron países que coincidan con '{nombre_pais}'.")


def filtrar_paises(paises):
    """
    Filtra países por continente, rango poblacional o rango de superficie.
    
    Args:
        paises (list): Lista de diccionarios con información de países
    """
    if not paises:
        print("No hay datos de países cargados.")
        return
    
    print("\nOpciones de filtrado:")
    print("c - Filtrar por continente")
    print("p - Filtrar por rango poblacional")
    print("s - Filtrar por rango de superficie")
    
    caracteristica_filtro = input("\nSeleccione el tipo de filtro (c/p/s): ").lower().strip()
    
    if caracteristica_filtro == "c":
        continente = input("Ingrese el continente: ").strip()
        
        if not continente:
            print("Debe ingresar un continente.")
            return
            
        paises_filtrados = []
        for pais in paises:
            if continente.lower() in pais["continente"].lower():
                paises_filtrados.append(pais)
        
        if paises_filtrados:
            print(f"\nPaíses del continente '{continente}' ({len(paises_filtrados)} encontrados):")
            print("-" * 60)
            for pais in paises_filtrados:
                print(f"Nombre: {pais['nombre']}")
                print(f"Población: {pais['poblacion']:,}")
                print(f"Superficie: {pais['superficie']:,} km²")
                print("-" * 60)
        else:
            print(f"No se encontraron países del continente '{continente}'.")

    elif caracteristica_filtro == "p":
        try:
            print("\nIngrese el rango poblacional:")
            poblacion_min = int(input("Población mínima: "))
            poblacion_max = int(input("Población máxima: "))
            
            if poblacion_min > poblacion_max:
                print("Error: La población mínima no puede ser mayor que la máxima.")
                return
                
            paises_filtrados = []
            for pais in paises:
                if poblacion_min <= pais["poblacion"] <= poblacion_max:
                    paises_filtrados.append(pais)
            
            if paises_filtrados:
                print(f"\nPaíses con población entre {poblacion_min:,} y {poblacion_max:,} ({len(paises_filtrados)} encontrados):")
                print("-" * 60)
                for pais in paises_filtrados:
                    print(f"Nombre: {pais['nombre']}")
                    print(f"Población: {pais['poblacion']:,}")
                    print(f"Superficie: {pais['superficie']:,} km²")
                    print(f"Continente: {pais['continente']}")
                    print("-" * 60)
            else:
                print(f"No se encontraron países con población entre {poblacion_min:,} y {poblacion_max:,}.")
                
        except ValueError:
            print("Error: Debe ingresar números válidos para el rango poblacional.")

    elif caracteristica_filtro == "s":
        try:
            print("\nIngrese el rango de superficie:")
            superficie_min = int(input("Superficie mínima (km²): "))
            superficie_max = int(input("Superficie máxima (km²): "))
            
            if superficie_min > superficie_max:
                print("Error: La superficie mínima no puede ser mayor que la máxima.")
                return
                
            paises_filtrados = []
            for pais in paises:
                if superficie_min <= pais["superficie"] <= superficie_max:
                    paises_filtrados.append(pais)
            
            if paises_filtrados:
                print(f"\nPaíses con superficie entre {superficie_min:,} y {superficie_max:,} km² ({len(paises_filtrados)} encontrados):")
                print("-" * 60)
                for pais in paises_filtrados:
                    print(f"Nombre: {pais['nombre']}")
                    print(f"Población: {pais['poblacion']:,}")
                    print(f"Superficie: {pais['superficie']:,} km²")
                    print(f"Continente: {pais['continente']}")
                    print("-" * 60)
            else:
                print(f"No se encontraron países con superficie entre {superficie_min:,} y {superficie_max:,} km².")
                
        except ValueError:
            print("Error: Debe ingresar números válidos para el rango de superficie.")
    else:
        print("Error: Debe seleccionar una opción válida (c/p/s).")


def ordenar_paises(paises):
    """
    Ordena países por nombre, población o superficie (ascendente o descendente).
    
    Args:
        paises (list): Lista de diccionarios con información de países
    """
    if not paises:
        print("No hay datos de países cargados.")
        return
    
    print("\nOpciones de ordenamiento:")
    print("n - Ordenar por nombre")
    print("p - Ordenar por población")
    print("s - Ordenar por superficie")
    
    caracteristica_orden = input("\nSeleccione el criterio de ordenamiento (n/p/s): ").lower().strip()
    
    if caracteristica_orden == "n":
        paises_ordenados = sorted(paises, key=lambda p: p["nombre"].lower())
        print("\nPaíses ordenados por nombre (A-Z):")
        print("-" * 60)
        for pais in paises_ordenados:
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']:,}")
            print(f"Superficie: {pais['superficie']:,} km²")
            print(f"Continente: {pais['continente']}")
            print("-" * 60)

    elif caracteristica_orden == "p":
        paises_ordenados = sorted(paises, key=lambda p: p["poblacion"])
        print("\nPaíses ordenados por población (menor a mayor):")
        print("-" * 60)
        for pais in paises_ordenados:
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']:,}")
            print(f"Superficie: {pais['superficie']:,} km²")
            print(f"Continente: {pais['continente']}")
            print("-" * 60)
            
    elif caracteristica_orden == "s":
        print("\nOpciones de ordenamiento por superficie:")
        print("a - Ascendente (menor a mayor)")
        print("d - Descendente (mayor a menor)")
        
        orden_superficie = input("Seleccione el orden (a/d): ").lower().strip()
        
        if orden_superficie == "a":
            paises_ordenados = sorted(paises, key=lambda p: p["superficie"])
            print("\nPaíses ordenados por superficie (menor a mayor):")
            print("-" * 60)
            for pais in paises_ordenados:
                print(f"Nombre: {pais['nombre']}")
                print(f"Población: {pais['poblacion']:,}")
                print(f"Superficie: {pais['superficie']:,} km²")
                print(f"Continente: {pais['continente']}")
                print("-" * 60)

        elif orden_superficie == "d":
            paises_ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=True)
            print("\nPaíses ordenados por superficie (mayor a menor):")
            print("-" * 60)
            for pais in paises_ordenados:
                print(f"Nombre: {pais['nombre']}")
                print(f"Población: {pais['poblacion']:,}")
                print(f"Superficie: {pais['superficie']:,} km²")
                print(f"Continente: {pais['continente']}")
                print("-" * 60)
        else:
            print("Error: Debe seleccionar una opción válida (a/d).")
    else:
        print("Error: Debe seleccionar una opción válida (n/p/s).")


def agregar_pais(paises):
    """
    Permite agregar un nuevo país al sistema con validación de campos obligatorios.
    
    Args:
        paises (list): Lista de diccionarios con información de países
        
    Returns:
        bool: True si se agregó exitosamente, False en caso contrario
    """
    if not paises:
        print("No hay datos de países cargados.")
        return False
    
    print("\n" + "="*50)
    print("           AGREGAR NUEVO PAÍS")
    print("="*50)
    
    # Solicitar datos del país
    nombre = input("Ingrese el nombre del país: ").strip()
    if not nombre:
        print("❌ Error: El nombre del país es obligatorio.")
        return False
    
    # Verificar si el país ya existe
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"❌ Error: El país '{nombre}' ya existe en el sistema.")
            return False
    
    try:
        poblacion = int(input("Ingrese la población: "))
        if poblacion <= 0:
            print("❌ Error: La población debe ser un número positivo.")
            return False
    except ValueError:
        print("❌ Error: Debe ingresar un número válido para la población.")
        return False
    
    try:
        superficie = int(input("Ingrese la superficie en km²: "))
        if superficie <= 0:
            print("❌ Error: La superficie debe ser un número positivo.")
            return False
    except ValueError:
        print("❌ Error: Debe ingresar un número válido para la superficie.")
        return False
    
    continente = input("Ingrese el continente: ").strip()
    if not continente:
        print("❌ Error: El continente es obligatorio.")
        return False
    
    # Crear el nuevo país
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    # Agregar a la lista
    paises.append(nuevo_pais)
    
    print(f"\n✅ País '{nombre}' agregado exitosamente al sistema.")
    print(f"   Población: {poblacion:,} habitantes")
    print(f"   Superficie: {superficie:,} km²")
    print(f"   Continente: {continente}")
    
    return True


def actualizar_pais(paises):
    """
    Permite actualizar la población y superficie de un país existente.
    
    Args:
        paises (list): Lista de diccionarios con información de países
        
    Returns:
        bool: True si se actualizó exitosamente, False en caso contrario
    """
    if not paises:
        print("No hay datos de países cargados.")
        return False
    
    print("\n" + "="*50)
    print("           ACTUALIZAR DATOS DE PAÍS")
    print("="*50)
    
    nombre_pais = input("Ingrese el nombre del país a actualizar: ").strip()
    if not nombre_pais:
        print("❌ Error: Debe ingresar un nombre de país.")
        return False
    
    # Buscar el país
    pais_encontrado = None
    for pais in paises:
        if pais["nombre"].lower() == nombre_pais.lower():
            pais_encontrado = pais
            break
    
    if not pais_encontrado:
        print(f"❌ Error: No se encontró el país '{nombre_pais}'.")
        return False
    
    print(f"\n📋 Datos actuales de {pais_encontrado['nombre']}:")
    print(f"   Población: {pais_encontrado['poblacion']:,} habitantes")
    print(f"   Superficie: {pais_encontrado['superficie']:,} km²")
    print(f"   Continente: {pais_encontrado['continente']}")
    
    print("\nIngrese los nuevos datos (presione Enter para mantener el valor actual):")
    
    # Actualizar población
    nueva_poblacion = input(f"Nueva población (actual: {pais_encontrado['poblacion']:,}): ").strip()
    if nueva_poblacion:
        try:
            poblacion = int(nueva_poblacion)
            if poblacion <= 0:
                print("❌ Error: La población debe ser un número positivo.")
                return False
            pais_encontrado["poblacion"] = poblacion
        except ValueError:
            print("❌ Error: Debe ingresar un número válido para la población.")
            return False
    
    # Actualizar superficie
    nueva_superficie = input(f"Nueva superficie en km² (actual: {pais_encontrado['superficie']:,}): ").strip()
    if nueva_superficie:
        try:
            superficie = int(nueva_superficie)
            if superficie <= 0:
                print("❌ Error: La superficie debe ser un número positivo.")
                return False
            pais_encontrado["superficie"] = superficie
        except ValueError:
            print("❌ Error: Debe ingresar un número válido para la superficie.")
            return False
    
    print(f"\n✅ Datos de '{pais_encontrado['nombre']}' actualizados exitosamente:")
    print(f"   Población: {pais_encontrado['poblacion']:,} habitantes")
    print(f"   Superficie: {pais_encontrado['superficie']:,} km²")
    print(f"   Continente: {pais_encontrado['continente']}")
    
    return True


def guardar_datos(paises, archivo_csv="paises.csv"):
    """
    Guarda los datos de países en un archivo CSV.
    
    Args:
        paises (list): Lista de diccionarios con información de países
        archivo_csv (str): Ruta del archivo CSV donde guardar los datos
        
    Returns:
        bool: True si se guardó exitosamente, False en caso contrario
    """
    if not paises:
        print("❌ Error: No hay datos para guardar.")
        return False
    
    try:
        with open(archivo_csv, 'w', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
            
            # Escribir encabezados
            escritor_csv.writeheader()
            
            # Escribir datos
            for pais in paises:
                escritor_csv.writerow(pais)
        
        print(f"✅ Datos guardados exitosamente en '{archivo_csv}'")
        print(f"   Total de países guardados: {len(paises)}")
        return True
        
    except Exception as e:
        print(f"❌ Error al guardar los datos: {e}")
        return False


def mostrar_estadisticas(paises):
    """
    Muestra estadísticas clave de los países: mayor/menor población, promedios y distribución por continente.
    
    Args:
        paises (list): Lista de diccionarios con información de países
    """
    if not paises:
        print("No hay datos de países cargados.")
        return
    
    print("\n" + "="*70)
    print("                    ESTADÍSTICAS DE PAÍSES")
    print("="*70)
    
    # País con mayor y menor población
    pais_mayor_poblacion = max(paises, key=lambda p: p["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda p: p["poblacion"])
    
    print(f"\n📊 POBLACIÓN:")
    print(f"   • País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']:,} habitantes)")
    print(f"   • País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']:,} habitantes)")
    
    # Promedio de población
    total_poblacion = sum(pais["poblacion"] for pais in paises)
    promedio_poblacion = total_poblacion / len(paises)
    print(f"   • Promedio de población: {promedio_poblacion:,.0f} habitantes")
    
    # Promedio de superficie
    total_superficie = sum(pais["superficie"] for pais in paises)
    promedio_superficie = total_superficie / len(paises)
    print(f"\n🌍 SUPERFICIE:")
    print(f"   • Promedio de superficie: {promedio_superficie:,.0f} km²")
    
    # País con mayor y menor superficie
    pais_mayor_superficie = max(paises, key=lambda p: p["superficie"])
    pais_menor_superficie = min(paises, key=lambda p: p["superficie"])
    print(f"   • País con mayor superficie: {pais_mayor_superficie['nombre']} ({pais_mayor_superficie['superficie']:,} km²)")
    print(f"   • País con menor superficie: {pais_menor_superficie['nombre']} ({pais_menor_superficie['superficie']:,} km²)")
    
    # Cantidad de países por continente
    print(f"\n🗺️  DISTRIBUCIÓN POR CONTINENTE:")
    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1
    
    for continente, cantidad in sorted(continentes.items()):
        print(f"   • {continente}: {cantidad} país(es)")
    
    # Densidad poblacional promedio
    print(f"\n📈 DENSIDAD POBLACIONAL:")
    densidad_total = sum(pais["poblacion"] / pais["superficie"] for pais in paises)
    densidad_promedio = densidad_total / len(paises)
    print(f"   • Densidad promedio: {densidad_promedio:.2f} habitantes/km²")
    
    print("\n" + "="*70)

# Función principal del programa
def main():
    """
    Función principal que ejecuta el menú interactivo del sistema de gestión de países.
    """
    print("="*70)
    print("           SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("="*70)
    
    if not paises:
        print("❌ Error: No se pudieron cargar los datos de países.")
        print("   Verifique que el archivo 'paises.csv' existe y tiene el formato correcto.")
        return
    
    print(f"✅ Sistema iniciado correctamente con {len(paises)} países cargados.")
    
    while True:
        print("\n" + "="*50)
        print("                MENÚ PRINCIPAL")
        print("="*50)
        print("1. 🔍 Buscar un país")
        print("2. 🔎 Filtrar países")
        print("3. 📊 Ordenar países")
        print("4. 📈 Mostrar estadísticas")
        print("5. ➕ Agregar país")
        print("6. ✏️  Actualizar país")
        print("7. 💾 Guardar datos")
        print("8. ❌ Salir del programa")
        print("="*50)
        
        opcion_elegida = input("\nSeleccione una opción (1-8): ").strip()
        
        if opcion_elegida == "1":
            print("\n" + "-"*50)
            print("           BÚSQUEDA DE PAÍSES")
            print("-"*50)
            buscar_pais(paises)
            
        elif opcion_elegida == "2":
            print("\n" + "-"*50)
            print("           FILTRADO DE PAÍSES")
            print("-"*50)
            filtrar_paises(paises)
            
        elif opcion_elegida == "3":
            print("\n" + "-"*50)
            print("           ORDENAMIENTO DE PAÍSES")
            print("-"*50)
            ordenar_paises(paises)
            
        elif opcion_elegida == "4":
            mostrar_estadisticas(paises)
            
        elif opcion_elegida == "5":
            print("\n" + "-"*50)
            print("           AGREGAR PAÍS")
            print("-"*50)
            agregar_pais(paises)
            
        elif opcion_elegida == "6":
            print("\n" + "-"*50)
            print("           ACTUALIZAR PAÍS")
            print("-"*50)
            actualizar_pais(paises)
            
        elif opcion_elegida == "7":
            print("\n" + "-"*50)
            print("           GUARDAR DATOS")
            print("-"*50)
            guardar_datos(paises)
            
        elif opcion_elegida == "8":
            print("\n" + "="*50)
            print("           SALIR DEL SISTEMA")
            print("="*50)
            
            # Preguntar si desea guardar los cambios
            guardar_cambios = input("¿Desea guardar los cambios antes de salir? (s/n): ").lower().strip()
            if guardar_cambios in ['s', 'si', 'sí', 'y', 'yes']:
                guardar_datos(paises)
            
            print("\n" + "="*50)
            print("           ¡GRACIAS POR USAR EL SISTEMA!")
            print("="*50)
            break
            
        else:
            print("\n❌ Error: Debe seleccionar una opción válida (1-8).")
            input("Presione Enter para continuar...")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()

