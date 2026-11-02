import ast
from normalizacion import normalizar_arbol
from serializacion import serializar
from similitud import similitud_hibrida, UMBRAL_SIMILITUD



# Funciones auxiliares
#Convierte texto a arbol de ast, le aplica normalizacion y luego serializa
def convertir_a_tokens(codigo):
    
    arbol = ast.parse(codigo)        
    funcion = arbol.body[0]          
    funcion_normalizada, _ = normalizar_arbol(funcion)   
    return serializar(funcion_normalizada)               

#Devuelve la similitud
def puntaje(codigo_a, codigo_b):
    tokens_a = convertir_a_tokens(codigo_a)
    tokens_b = convertir_a_tokens(codigo_b)
    resultado = similitud_hibrida(tokens_a, tokens_b)
    return resultado["promedio"]


# Funciones de ejemplo para los casos POSITIVOS

TOTAL_ORIGINAL = '''
def total(items, rate):
    s = 0
    for i in items:
        s += i.price
    return s * rate
'''

# Clon
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

# Clon
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

PROCESAR_ORIGINAL = '''
def procesar(valores):
    suma = 0
    cantidad = 0
    positivos = 0
    maximo = valores[0]
    for valor in valores:
        suma += valor
        cantidad += 1
        if valor > 0:
            positivos += 1
        if valor > maximo:
            maximo = valor
    promedio = suma / cantidad
    return promedio, positivos, maximo
'''

PROCESAR_REORDENADO = '''
def procesar(valores):
    suma = 0
    cantidad = 0
    positivos = 0
    maximo = valores[0]
    for valor in valores:
        cantidad += 1
        if valor > maximo:
            maximo = valor
        suma += valor
        if valor > 0:
            positivos += 1
    promedio = suma / cantidad
    return promedio, positivos, maximo
'''

FUNCION_CORTA_ORIGINAL = '''
def doble(numero):
    return numero * 2
'''

FUNCION_CORTA_REORDENADA = '''
def doble(numero):
    return 2 * numero
'''

RESUMEN_ORIGINAL = '''
def resumen(d):
    a = len(d)
    b = sum(d)
    return b / a
'''

RESUMEN_VARIABLES_REORDENADAS = '''
def resumen(d):
    b = sum(d)
    a = len(d)
    return b / a
'''


# Funciones de ejemplo para los casos NEGATIVOS (claramente distintas)

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

# Casos POSITIVOS: el sistema TIENE que detectarlos como clones

def test_positivo_variables_renombradas():
    resultado = puntaje(TOTAL_ORIGINAL, TOTAL_RENOMBRADO)

    assert resultado == 1.0


def test_positivo_lineas_reordenadas():
    resultado = puntaje(ESTADISTICAS_ORIGINAL, ESTADISTICAS_REORDENADO)

    assert resultado >= UMBRAL_SIMILITUD   
    assert resultado < 1.0                 


def test_positivo_reordenado_y_renombrado():
    resultado = puntaje(ESTADISTICAS_ORIGINAL, ESTADISTICAS_REORDENADO_Y_RENOMBRADO)
    solo_reordenado = puntaje(ESTADISTICAS_ORIGINAL, ESTADISTICAS_REORDENADO)

    assert resultado >= UMBRAL_SIMILITUD
    assert resultado == solo_reordenado


def test_positivo_funciones_con_varias_lineas_reordenadas():
    resultado = puntaje(PROCESAR_ORIGINAL, PROCESAR_REORDENADO)

    assert resultado >= UMBRAL_SIMILITUD
    assert resultado < 1.0


# Casos NEGATIVOS: el sistema NO tiene que detectarlos como clones

def test_negativo_suma_vs_parseo():
    resultado = puntaje(SUMA, PARSEO)

    assert resultado < UMBRAL_SIMILITUD


def test_negativo_iterativa_vs_recursiva():
    resultado = puntaje(SUMA, FACTORIAL_RECURSIVO)

    assert resultado < UMBRAL_SIMILITUD


def test_limitacion_funciones_cortas_equivalentes():
    resultado = puntaje(FUNCION_CORTA_ORIGINAL, FUNCION_CORTA_REORDENADA)

    assert resultado < UMBRAL_SIMILITUD


def test_limitacion_orden_de_variables_reordenadas():
    resultado = puntaje(RESUMEN_ORIGINAL, RESUMEN_VARIABLES_REORDENADAS)

    assert resultado < UMBRAL_SIMILITUD
