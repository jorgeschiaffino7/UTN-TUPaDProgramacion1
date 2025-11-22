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

#### 5. Agregar País
- Inserción de nuevos registros con validación integral
- Verificación de campos obligatorios y unicidad
- Validación de tipos de datos y rangos positivos

#### 6. Actualizar País
- Modificación selectiva de registros existentes
- Actualización parcial (mantiene valores actuales si no se ingresan nuevos)
- Búsqueda case-insensitive con normalización

#### 7. Guardar Datos
- Persistencia de datos en formato CSV
- Serialización con codificación UTF-8
- Manejo seguro de archivos con context managers

#### 8. Salir
- Confirmación para guardar cambios pendientes
- Terminación controlada del programa

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

1. El archivo `paises.csv` tiene que estar en el mismo directorio
2. Ejecuta el programa:
   ```bash
   python TPIntegrador_Programación.py
   ```
3. Seguir las instrucciones del menú interactivo

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
5. ➕ Agregar país
6. ✏️ Actualizar país
7. 💾 Guardar datos
8. ❌ Salir del programa
==============================================

Seleccione una opción (1-8): 1
```

## Informe Técnico

### Módulo de Estadísticas (Opción 4)
**Función**: `mostrar_estadisticas(paises)`

- **Algoritmos**: `max()` y `min()` con funciones `lambda` para comparación
- **Cálculos**: `sum()` para totalizaciones y operaciones aritméticas para promedios
- **Agrupamiento**: Diccionario para conteo por continente mediante iteración condicional
- **Complejidad**: O(n) donde n es el número de países
- **Métricas**: Extremos poblacionales/territoriales, promedios, densidad poblacional promedio, distribución por continente

### Módulo de Inserción (Opción 5)
**Función**: `agregar_pais(paises)`

- **Validaciones**: Campos obligatorios (strings no vacíos), unicidad mediante búsqueda lineal case-insensitive, tipado numérico con `int()`, valores positivos (población > 0, superficie > 0)
- **Manejo de excepciones**: Captura de `ValueError` para errores de conversión
- **Retorno**: Booleano indicando éxito/fallo de la operación

### Módulo de Actualización (Opción 6)
**Función**: `actualizar_pais(paises)`

- **Búsqueda**: Algoritmo lineal con normalización lowercase
- **Actualización parcial**: Permite mantener valores actuales si no se ingresa dato nuevo
- **Modificación**: Cambios directos sobre el diccionario en memoria
- **Flujo**: Búsqueda → Visualización → Solicitud opcional → Validación → Confirmación

### Módulo de Persistencia (Opción 7)
**Función**: `guardar_datos(paises, archivo_csv)`

- **Tecnología**: `csv.DictWriter` con codificación UTF-8
- **Gestión de recursos**: Context manager (`with`) para cierre automático
- **Estructura**: Columnas `nombre,poblacion,superficie,continente`
- **Manejo de errores**: Captura de excepciones genéricas, validación de lista no vacía

### Módulo de Control Principal
**Función**: `main()`

- **Arquitectura**: Bucle infinito con menú interactivo
- **Control de flujo**: Estructura `if-elif-else` para enrutamiento
- **Validación**: Verificación de opciones válidas (1-8)
- **Salida**: Confirmación para guardar cambios, mensajes de despedida, terminación con `break`
- **Punto de entrada**: `if __name__ == "__main__": main()`

## Autor - Grupo  125
Jorge Schiaffino 
Juan Arrúa