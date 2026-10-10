"""
similitud.py
------------

Qué hace:
    Mide qué tan parecidas son dos secuencias de tokens. Devuelve un puntaje
    entre 0.0 (nada en común) y 1.0 (idénticas).

Entrada:  dos listas de tokens (salida de serializacion.serializar).
Salida:   float en [0, 1].

Métricas (el enunciado pide al menos una):
    - Jaccard sobre n-gramas: |A ∩ B| / |A ∪ B| sobre los conjuntos de n-gramas.
      Tolera mejor las líneas reordenadas (solo se rompen los n-gramas de la
      "costura").
    - Levenshtein normalizado: 1 - distancia / max(len(a), len(b)).
      Penaliza más el reordenamiento.

Decisiones de diseño (completar con DATOS de las pruebas, no "porque sí"):
    - Valor de n elegido: ____  (probamos n = 2, 3, 4; resultados: ____)
    - Umbral de "candidato a duplicado": ____  (justificación: ____)
    - Tratamiento de secuencias muy cortas (getters de 2 líneas): ____
    - Casos borde: secuencias vacías o más cortas que n.

"""

UMBRAL_DUPLICADO = 0.80  # TODO: ajustar y justificar con casos reales
N_GRAMA = 3              # TODO: justificar la elección de n


def n_gramas(tokens, n=N_GRAMA):
    """Devuelve el conjunto de n-gramas (tuplas de n tokens consecutivos).

    TODO: ventana deslizante; decidir qué hacer si len(tokens) < n.
    """
    raise NotImplementedError


def jaccard(tokens_a, tokens_b, n=N_GRAMA):
    """Similitud de Jaccard entre los n-gramas de dos secuencias.

    TODO: |A ∩ B| / |A ∪ B|; cuidar la división por cero si ambos conjuntos
    son vacíos.
    """
    raise NotImplementedError


def levenshtein_normalizada(tokens_a, tokens_b):
    """Similitud basada en distancia de edición (opcional).

    TODO: programación dinámica sobre las dos listas; devolver
    1 - distancia / max(len(a), len(b)).
    """
    raise NotImplementedError


def es_candidato_duplicado(puntaje, umbral=UMBRAL_DUPLICADO):
    """True si el puntaje alcanza el umbral de 'candidato a duplicado'."""
    return puntaje >= umbral
