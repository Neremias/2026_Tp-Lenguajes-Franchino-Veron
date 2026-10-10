"""
serializacion.py
----------------

Qué hace:
    Convierte un AST normalizado en una secuencia lineal de tokens mediante
    un recorrido pre-order (visito el nodo, emito su token, bajo a los hijos).

Entrada:  AST normalizado (salida de normalizacion.normalizar).
Salida:   lista de strings, p. ej. ['FunctionDef', 'arguments', 'arg', 'VAR1', ...]

Decisiones de diseño (completar a medida que se toman):
    - Por qué pre-order (lo exige el enunciado) y cómo se ordenan los hijos
      (ast.iter_child_nodes respeta el orden de los campos del nodo).
    - Qué emite cada tipo de nodo: nombre de clase del nodo (For, Assign,
      BinOp, Add...) o el token normalizado (VARn / LIT).
    - Si se agregan marcadores de fin de bloque (no necesarios en pre-order
      simple, pero pueden ayudar a distinguir estructuras).

"""

import ast


def serializar(nodo_normalizado):
    """Devuelve la lista de tokens del recorrido pre-order del AST.

    TODO: función recursiva (o con pila) que emita el token del nodo y luego
    recorra ast.iter_child_nodes(nodo).
    """
    raise NotImplementedError
