"""
buscar_similares.py
-------------------
TP Lenguajes Formales y Autómatas 2026 - Motor de búsqueda de funciones similares.
Integrantes: Verón, Franchino, Quiroga

Qué hace:
    Interfaz de línea de comandos (CLI) y motor de búsqueda. Dada una función
    objetivo, compara contra todas las funciones del repositorio
    (todos-contra-todos, O(n^2), aceptable según el enunciado) y devuelve las
    top-K más similares con su puntaje.

Pipeline:
    extraccion -> normalizacion -> serializacion -> similitud -> ranking top-K

Uso (ejemplos):
    python buscar_similares.py --dir ./mi_repo --funcion archivo.py:mi_funcion --top 5
    python buscar_similares.py --dir ./mi_repo --codigo-archivo mi_funcion.txt --top 5

Argumentos:
    --dir      directorio a analizar (recursivo).
    --funcion  función objetivo en formato archivo.py:nombre.
    --codigo-archivo  alternativa: archivo con el código de la función pegado.
    --top      cantidad K de resultados (default: 5).
    --umbral   umbral de 'candidato a duplicado' (default: ver similitud.py).

Decisiones de diseño (completar a medida que se toman):
    - Qué hacer si el nombre de función es ambiguo (misma función en dos archivos).
    - Si la función objetivo se excluye de sus propios resultados.
    - Formato de salida: archivo, línea, nombre, puntaje, marca de duplicado.

Relación con el enunciado: requisito 4.4 (Motor de búsqueda / interfaz).
"""

import argparse


def construir_parser():
    """Arma el parser de argumentos (argparse).

    TODO: definir --dir, --funcion, --codigo-archivo, --top, --umbral.
    """
    raise NotImplementedError


def buscar_top_k(funcion_objetivo, funciones, k=5):
    """Devuelve las k funciones más similares a la objetivo, con su puntaje.

    TODO: para cada función del repo -> normalizar -> serializar -> jaccard;
    ordenar de mayor a menor puntaje y cortar en k.
    """
    raise NotImplementedError


def main():
    """Punto de entrada de la CLI."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
