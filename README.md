# TP Lenguajes Formales y Autómatas 2026 — Motor de búsqueda de funciones similares

**Integrantes:** Verón, Franchino, Quiroga
**Defensa oral individual:** 4/11/2026

## Qué hace

Dada una carpeta con archivos `.py`, extrae todas las funciones, las normaliza
(variables → `VAR1, VAR2...`, literales → `LIT`), las convierte en una secuencia
de tokens (recorrido pre-order del AST) y, dada una función objetivo, devuelve las
top-K más similares con su puntaje.

## Estructura

| Archivo | Rol |
|---|---|
| `extraccion.py` | Recorre el directorio y extrae las funciones (req. 4.1) |
| `normalizacion.py` | Normaliza el AST de cada función (req. 4.2) |
| `serializacion.py` | AST normalizado → secuencia de tokens pre-order (req. 4.3) |
| `similitud.py` | Jaccard sobre n-gramas / Levenshtein, y umbral (req. 4.3) |
| `buscar_similares.py` | CLI y ranking top-K (req. 4.4) |
| `tests/` | Suite pytest: 2 positivos + 2 negativos mínimo |
| `informe.md` | Informe breve (máx. 2 páginas) |

## Uso

```bash
python buscar_similares.py --dir ./mi_repo --funcion archivo.py:mi_funcion --top 5
```

## Tests

```bash
pip install -r requirements.txt
pytest -v
```

## Estado

- [ ] Extracción
- [ ] Normalización
- [ ] Serialización
- [ ] Similitud y umbral
- [ ] CLI / top-K
- [ ] Tests (2 positivos + 2 negativos)
- [ ] Informe
