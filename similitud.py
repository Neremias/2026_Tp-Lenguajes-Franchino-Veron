UMBRAL_DUPLICADO = 0.80  # TODO: ajustar y justificar con casos reales
N_GRAMA = 3              # TODO: justificar la elección de n


def n_gramas(tokens, n=N_GRAMA):
    raise NotImplementedError


def jaccard(tokens_a, tokens_b, n=N_GRAMA):
    raise NotImplementedError


def levenshtein_normalizada(tokens_a, tokens_b):
    raise NotImplementedError


def es_candidato_duplicado(puntaje, umbral=UMBRAL_DUPLICADO):
    return puntaje >= umbral
