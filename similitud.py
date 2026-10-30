TAMANO_NGRAMA = 3
UMBRAL_SIMILITUD = 0.70

#

def obtener_ngramas(secuencia, n=TAMANO_NGRAMA):
    # Corta la lista en grupos de tamaño 'n' y los guarda en un set (sin repetidos)
    return set(tuple(secuencia[i : i + n]) for i in range(len(secuencia) - n + 1))


def similitud_jaccard(secuencia_a, secuencia_b, n=TAMANO_NGRAMA):
    ngramas_a = obtener_ngramas(secuencia_a, n)
    ngramas_b = obtener_ngramas(secuencia_b, n)

    # Si ambas quedan vacías (por ejemplo, listas más cortas que n), son iguales (1.0)
    if not ngramas_a and not ngramas_b:
        return 1.0

    interseccion = ngramas_a & ngramas_b  # Grupos que están en A y en B
    union = ngramas_a | ngramas_b         # Todos los grupos sumados sin repetir

    return len(interseccion) / len(union)


def similitud_levenshtein(seq_a, seq_b):
    if not seq_a and not seq_b:
        return 1.0
    
    filas = len(seq_a) + 1
    cols = len(seq_b) + 1
    
    # Crea la tabla de distancias
    dist = [[0] * cols for _ in range(filas)]
    for i in range(filas):
        dist[i][0] = i
    for j in range(cols):
        dist[0][j] = j

    # Calcula el mínimo de cambios (insertar, borrar o reemplazar)
    for i in range(1, filas):
        for j in range(1, cols):
            costo = 0 if seq_a[i - 1] == seq_b[j - 1] else 1
            dist[i][j] = min(
                dist[i - 1][j] + 1,      # Borrar
                dist[i][j - 1] + 1,      # Insertar
                dist[i - 1][j - 1] + costo  # Reemplazar
            )

    cambios = dist[-1][-1]
    largo_max = max(len(seq_a), len(seq_b))
    return 1.0 - (cambios / largo_max)


def similitud_hibrida(seq_a, seq_b, n=TAMANO_NGRAMA):
    jaccard = similitud_jaccard(seq_a, seq_b, n)
    levenshtein = similitud_levenshtein(seq_a, seq_b)
    promedio = (jaccard + levenshtein) / 2
    
    return {
        "jaccard": jaccard,
        "levenshtein": levenshtein,
        "promedio": promedio,
        "es_clon": promedio >= UMBRAL_SIMILITUD
    }
