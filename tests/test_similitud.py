"""
test_similitud.py
-----------------
Suite mínima exigida por el enunciado (sección 5):
    - 2 casos POSITIVOS: funciones clonadas (variables renombradas / líneas reordenadas).
    - 2 casos NEGATIVOS: funciones claramente distintas.

Los tests están marcados como 'skip' hasta que se implementen los módulos.
Cuando el pipeline funcione, quitar el decorador @pendiente de cada test.
"""

import pytest

pendiente = pytest.mark.skip(reason="pendiente: implementar el pipeline")

# --- Funciones de ejemplo (código fuente como string) -----------------------

ORIGINAL = '''
def total(items, rate):
    s = 0
    for i in items:
        s += i.price
    return s * rate
'''

# Clon tipo 2: mismo cuerpo, variables y nombre de función renombrados.
RENOMBRADO = '''
def calcular(productos, factor):
    r = 0
    for p in productos:
        r += p.price
    return r * factor
'''

ORIGINAL_DOS_SENTENCIAS = '''
def resumen(datos):
    a = len(datos)
    b = sum(datos)
    return b / a
'''

# Clon con dos sentencias independientes intercambiadas.
REORDENADO = '''
def resumen(datos):
    b = sum(datos)
    a = len(datos)
    return b / a
'''

# Funciones claramente distintas entre sí.
SUMA = '''
def sumar(lista):
    total = 0
    for x in lista:
        total += x
    return total
'''

PARSEO = '''
def parsear(texto):
    partes = texto.split(",")
    resultado = {}
    for p in partes:
        clave, valor = p.split("=")
        resultado[clave.strip()] = valor.strip()
    return resultado
'''

RECURSIVA = '''
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
'''


def puntaje(codigo_a, codigo_b):
    """Calcula la similitud entre dos funciones dadas como código.

    TODO: encadenar extraer_funciones_de_codigo -> normalizar -> serializar
    -> jaccard y devolver el puntaje.
    """
    raise NotImplementedError


# --- Positivos --------------------------------------------------------------

@pendiente
def test_positivo_variables_renombradas():
    """Clon con variables y nombre de función renombrados: score ~ 1.0."""
    assert puntaje(ORIGINAL, RENOMBRADO) == pytest.approx(1.0)


@pendiente
def test_positivo_lineas_reordenadas():
    """Dos sentencias independientes intercambiadas: score alto pero < 1.0."""
    p = puntaje(ORIGINAL_DOS_SENTENCIAS, REORDENADO)
    assert 0.6 <= p < 1.0  # TODO: ajustar el piso con los resultados reales


# --- Negativos --------------------------------------------------------------

@pendiente
def test_negativo_suma_vs_parseo():
    """Una suma con for y un parseo de strings no deben parecerse."""
    assert puntaje(SUMA, PARSEO) < 0.5  # TODO: ajustar con el umbral elegido


@pendiente
def test_negativo_iterativa_vs_recursiva():
    """Un for acumulador y una recursión no deben parecerse."""
    assert puntaje(SUMA, RECURSIVA) < 0.5  # TODO: ajustar con el umbral elegido
