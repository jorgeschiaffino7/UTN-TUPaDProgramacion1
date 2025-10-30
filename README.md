# TP Integrador - Gestión de Datos de Países

## Descripción
Sistema desarrollado en Python para gestionar información sobre países, aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas.

## Características Principales

### 📁 Lectura de Datos
- **Archivo CSV**: El sistema lee datos desde `paises.csv`
- **Validación**: Control de errores de formato y archivos faltantes
- **Codificación**: Soporte UTF-8 para caracteres especiales

### 🔍 Funcionalidades Implementadas

#### 1. Búsqueda de Países
- **Coincidencia parcial**: Busca países que contengan el texto ingresado
- **Insensible a mayúsculas/minúsculas**
- **Múltiples resultados**: Muestra todos los países que coincidan

#### 2. Filtrado de Países
- **Por continente**: Filtra países de un continente específico
- **Por rango poblacional**: Filtra por población mínima y máxima
- **Por rango de superficie**: Filtra por superficie mínima y máxima

#### 3. Ordenamiento
- **Por nombre**: Ordenamiento alfabético (A-Z)
- **Por población**: Ordenamiento ascendente
- **Por superficie**: Opción ascendente o descendente

#### 4. Estadísticas
- País con mayor y menor población
- País con mayor y menor superficie
- Promedio de población y superficie
- Distribución de países por continente
- Densidad poblacional promedio

## Estructura de Datos

Cada país está representado con:
- **Nombre** (string)
- **Población** (int)
- **Superficie** (int) - en km²
- **Continente** (string)

## Archivos del Proyecto

- `TPIntegrador_Programación.py` - Código principal del sistema
- `paises.csv` - Archivo de datos con información de países
- `README.md` - Documentación del proyecto

## Requisitos Técnicos

- **Python 3.x**
- **Módulos utilizados**: `csv`, `os`
- **Estructuras**: listas, diccionarios, funciones
- **Validaciones**: Control de errores y entradas inválidas

## Cómo Ejecutar

1. Asegúrate de que el archivo `paises.csv` esté en el mismo directorio
2. Ejecuta el programa:
   ```bash
   python TPIntegrador_Programación.py
   ```
3. Sigue las instrucciones del menú interactivo

## Conceptos Aplicados

### Listas
- Almacenamiento de datos de países
- Manipulación y filtrado de elementos
- Ordenamiento con `sorted()`

### Diccionarios
- Estructura de datos para cada país
- Acceso por claves (nombre, población, superficie, continente)
- Agrupación por continente

### Funciones
- **Modularización**: Cada función tiene una responsabilidad específica
- **Reutilización**: Funciones independientes y reutilizables
- **Documentación**: Docstrings explicativos

### Estructuras Condicionales
- Validación de opciones del menú
- Control de flujo en filtros y búsquedas
- Manejo de errores

### Estructuras Repetitivas
- Menú principal con bucle `while`
- Iteración sobre listas de países
- Procesamiento de datos CSV

### Ordenamientos
- Ordenamiento por diferentes criterios
- Uso de `lambda` para funciones de ordenamiento
- Opciones ascendente/descendente

### Estadísticas Básicas
- Cálculo de promedios
- Encontrar valores máximos y mínimos
- Agrupación y conteo por categorías

### Archivos CSV
- Lectura con `csv.DictReader`
- Manejo de errores de formato
- Validación de datos numéricos

## Validaciones Implementadas

- ✅ Control de archivos CSV faltantes
- ✅ Validación de formato de datos numéricos
- ✅ Verificación de rangos válidos (min ≤ max)
- ✅ Manejo de entradas vacías
- ✅ Mensajes claros de error y éxito
- ✅ Validación de opciones del menú

## Ejemplo de Uso

```
==============================================
                MENÚ PRINCIPAL
==============================================
1. 🔍 Buscar un país
2. 🔎 Filtrar países
3. 📊 Ordenar países
4. 📈 Mostrar estadísticas
5. ❌ Salir del programa
==============================================

Seleccione una opción (1-5): 1
```

## Autor
[Nombre del estudiante] - Programación 1 - UTN

## Fecha
[Fecha de entrega]