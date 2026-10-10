"""
extraccion.py
-------------

Qué hace:
    Recorre recursivamente un directorio, parsea cada archivo .py con
    ast.parse() y extrae todas las funciones definidas (FunctionDef y,
    opcionalmente, AsyncFunctionDef).

Entrada:  ruta de un directorio (str o Path).
Salida:   lista de FuncionExtraida con nombre original, archivo, línea y
          subárbol AST de cada función.

Decisiones de diseño (completar a medida que se toman):
    - Archivos con errores de sintaxis: (ej. se omiten y se avisa por stderr).
    - Funciones anidadas: (ej. se extraen como funciones independientes).
    - Métodos de clase: (ej. se extraen, el nombre queda como Clase.metodo).
    - AsyncFunctionDef: (incluida / excluida, y por qué).
    - Directorios ignorados: (ej. venv, .git, __pycache__).

"""

import ast
from dataclasses import dataclass
from pathlib import Path


@dataclass
class FuncionExtraida:
    """Una función encontrada en el repositorio."""

    nombre: str          # nombre original (solo informativo, NO influye en la similitud)
    archivo: str         # ruta del archivo donde está definida
    linea: int           # línea donde empieza (node.lineno)
    nodo: ast.AST        # subárbol AST completo de la función


def extraer_funciones(directorio):
    """Devuelve la lista de FuncionExtraida de todos los .py bajo `directorio`.

    TODO: recorrer con Path.rglob("*.py"), parsear con ast.parse y manejar
    SyntaxError sin cortar la ejecución.
    """
    raise NotImplementedError


def extraer_funciones_de_codigo(codigo, nombre_archivo="<pegado>"):
    """Igual que extraer_funciones pero sobre un string de código.

    Sirve para la opción de 'pegar el código' de la CLI (requisito 4.4).

    TODO: ast.parse(codigo) + NodeVisitor que junte los FunctionDef.
    """
    raise NotImplementedError
