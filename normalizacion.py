"""
normalizacion.py
----------------

Qué hace:
    Convierte el AST de una función en una versión normalizada, donde los
    identificadores de variables y parámetros pasan a VAR1, VAR2... y los
    literales (números, strings) pasan a LIT. Así dos funciones con la misma
    estructura pero distintos nombres quedan idénticas.

Entrada:  nodo ast.FunctionDef (o AsyncFunctionDef).
Salida:   AST normalizado (sin modificar el original: trabajar sobre una copia
          con copy.deepcopy).

Decisiones de diseño (completar a medida que se toman):
    - VAR se numera por orden de primera aparición dentro de CADA función
      (un diccionario nombre -> VARn nuevo por función).
    - El nombre de la propia función NO influye en la comparación (req. 4.2).
    - Docstrings: (se descartan / se reemplazan por LIT, y por qué).
    - Nombres de funciones llamadas (len, range, print...) y atributos
      (.append): (se conservan / se normalizan, y por qué).
    - Literales: todos a LIT salvo que el grupo justifique lo contrario.
    - Casos borde: lambdas, comprensiones, *args/**kwargs, nombres globales.

Relación con el enunciado: requisito 4.2 (Normalización).
Herramienta sugerida: ast.NodeTransformer.
"""

import ast
import copy


def normalizar(nodo_funcion):
    """Devuelve una copia normalizada del AST de una función.

    TODO: implementar un NodeTransformer con visit_Name, visit_arg,
    visit_Constant, etc., usando un mapa nombre -> VARn por función.
    """
    raise NotImplementedError
