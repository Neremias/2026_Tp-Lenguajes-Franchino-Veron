"""
test_similitud.py
-----------------
Suite mínima exigida por el enunciado (sección 5).

Qué se prueba:
    Se toman dos funciones escritas como texto, se pasan por TODO el pipeline
    (AST -> normalización -> serialización -> similitud) y se mira el puntaje.

    - Casos POSITIVOS: funciones clonadas (variables renombradas / líneas
      reordenadas). El puntaje tiene que ser MAYOR O IGUAL al umbral, es decir,
      el sistema las tiene que marcar como "candidato a duplicado".
    - Casos NEGATIVOS: funciones claramente distintas. El puntaje tiene que ser
      MENOR al umbral, es decir, el sistema NO las tiene que marcar como clon.

Cómo correrlos (desde la carpeta raíz del proyecto):
    pytest -v
"""

import ast

# Estos módulos están en la carpeta "Aprendizaje_modulo_extraccion".
# Python los encuentra porque conftest.py agrega esa carpeta al sys.path.
from normalizacion import normalizar_arbol
from serializacion import serializar
from similitud import similitud_hibrida, UMBRAL_SIMILITUD


# =============================================================================
# Funciones auxiliares
# =============================================================================

def convertir_a_tokens(codigo):
    """Recibe el código de UNA función (como texto) y devuelve su lista de tokens."""
    arbol = ast.parse(codigo)        # texto -> AST (el nodo raíz es un Module)
    funcion = arbol.body[0]          # la primera sentencia del Module es la función
    funcion_normalizada, _ = normalizar_arbol(funcion)   # variables -> Var1, Var2...
    return serializar(funcion_normalizada)               # AST -> lista de tokens


def puntaje(codigo_a, codigo_b):
    """Devuelve la similitud (entre 0.0 y 1.0) entre dos funciones."""
    tokens_a = convertir_a_tokens(codigo_a)
    tokens_b = convertir_a_tokens(codigo_b)
    resultado = similitud_hibrida(tokens_a, tokens_b)
    return resultado["promedio"]


# =============================================================================
# Funciones de ejemplo para los casos POSITIVOS (clones)
# =============================================================================

# Función original: suma los precios de una lista y aplica un factor.
TOTAL_ORIGINAL = '''
def total(items, rate):
    s = 0
    for i in items:
        s += i.price
    return s * rate
'''

# Clon: es EXACTAMENTE el mismo código, pero con otros nombres
# (la función, los parámetros y las variables cambiaron de nombre).
TOTAL_RENOMBRADO = '''
def calcular(productos, factor):
    r = 0
    for p in productos:
        r += p.price
    return r * factor
'''

# Función original: calcula el promedio y el máximo de una lista.
ESTADISTICAS_ORIGINAL = '''
def estadisticas(numeros):
    suma = 0
    cantidad = 0
    maximo = numeros[0]
    for n in numeros:
        suma += n
        cantidad += 1
        if n > maximo:
            maximo = n
    promedio = suma / cantidad
    return promedio, maximo
'''

# Clon: mismo código, pero DENTRO del for se cambió el orden de las líneas
# (el "if" pasó de estar al principio a estar al final).
ESTADISTICAS_REORDENADO = '''
def estadisticas(numeros):
    suma = 0
    cantidad = 0
    maximo = numeros[0]
    for n in numeros:
        cantidad += 1
        suma += n
        if n > maximo:
            maximo = n
    promedio = suma / cantidad
    return promedio, maximo
'''

# Clon: las dos cosas juntas -> líneas reordenadas Y variables renombradas.
ESTADISTICAS_REORDENADO_Y_RENOMBRADO = '''
def resumen(valores):
    acumulado = 0
    contador = 0
    mayor = valores[0]
    for v in valores:
        contador += 1
        acumulado += v
        if v > mayor:
            mayor = v
    media = acumulado / contador
    return media, mayor
'''


# =============================================================================
# Funciones de ejemplo para los casos NEGATIVOS (claramente distintas)
# =============================================================================

# Suma los elementos de una lista con un for.
SUMA = '''
def sumar(lista):
    total = 0
    for x in lista:
        total += x
    return total
'''

# Convierte un texto "a=1,b=2" en un diccionario. Trabaja con strings.
PARSEO = '''
def parsear(texto):
    partes = texto.split(",")
    resultado = {}
    for p in partes:
        clave, valor = p.split("=")
        resultado[clave.strip()] = valor.strip()
    return resultado
'''

# Calcula el factorial con recursión (sin for, se llama a sí misma).
FACTORIAL_RECURSIVO = '''
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
'''

# =============================================================================
# Casos POSITIVOS: el sistema TIENE que detectarlos como clones
# =============================================================================

def test_positivo_variables_renombradas():
    """Si solo cambian los nombres, después de normalizar quedan iguales.

    La normalización reemplaza todos los nombres por Var1, Var2, ... así que
    las dos funciones generan la misma lista de tokens -> puntaje 1.0 (100%).
    """
    resultado = puntaje(TOTAL_ORIGINAL, TOTAL_RENOMBRADO)

    assert resultado == 1.0


def test_positivo_lineas_reordenadas():
    """Si se cambia el orden de algunas líneas, el puntaje baja un poco,
    pero tiene que seguir superando el umbral (se detecta como clon)."""
    resultado = puntaje(ESTADISTICAS_ORIGINAL, ESTADISTICAS_REORDENADO)

    assert resultado >= UMBRAL_SIMILITUD   # se detecta como clon...
    assert resultado < 1.0                 # ...pero no son idénticas


def test_positivo_reordenado_y_renombrado():
    """Combinando los dos cambios (renombrar + reordenar) también se detecta.

    Da el mismo puntaje que solo reordenar, porque renombrar no afecta nada.
    """
    resultado = puntaje(ESTADISTICAS_ORIGINAL, ESTADISTICAS_REORDENADO_Y_RENOMBRADO)
    solo_reordenado = puntaje(ESTADISTICAS_ORIGINAL, ESTADISTICAS_REORDENADO)

    assert resultado >= UMBRAL_SIMILITUD
    assert resultado == solo_reordenado


# =============================================================================
# Casos NEGATIVOS: el sistema NO tiene que detectarlos como clones
# =============================================================================

def test_negativo_suma_vs_parseo():
    """Una suma de números y un parseo de strings no se parecen en nada."""
    resultado = puntaje(SUMA, PARSEO)

    assert resultado < UMBRAL_SIMILITUD


def test_negativo_iterativa_vs_recursiva():
    """Un for que acumula y una función recursiva tienen estructuras distintas."""
    resultado = puntaje(SUMA, FACTORIAL_RECURSIVO)

    assert resultado < UMBRAL_SIMILITUD
