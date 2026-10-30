import argparse
from extraccion import extraer_funciones
from similitud import similitud_hibrida, TAMANO_NGRAMA
from normalizacion import normalizar_arbol
from serializacion import serializar

def construir_parser():
    """Arma el parser de argumentos (argparse)."""
    parser = argparse.ArgumentParser(description="Buscador de funciones similares por AST")
    parser.add_argument("--dir", required=True, help="Ruta a la carpeta a analizar (ej: utilidades o \"C:\\Mi Carpeta\")")
    parser.add_argument("--funcion", help="Formato archivo.py:nombre (ej: matematica.py:sumar - sin corchetes)")
    parser.add_argument("--codigo", help="Código directo entre comillas dobles (ej: \"def f(x): return x + 1\")")
    parser.add_argument("--top", type=int, default=5, help="Cantidad de resultados a mostrar (ej: --top 5)")
    parser.add_argument("--umbral", type=float, default=0.70, help="Umbral de similitud entre 0.0 y 1.0 (ej: --umbral 0.75)")
    parser.add_argument("--formato", choices=["tabla", "json"], default="tabla")

    return parser.parse_args()


def buscar_top_k(nombre_objetivo, funciones, k=5):
    if nombre_objetivo not in funciones:
        print(f"Error: La función '{nombre_objetivo}' no fue encontrada en el repositorio.")
        return []

    tokens_objetivo = funciones[nombre_objetivo]
    ranking = []

    for nombre, tokens in funciones.items():
        # Excluimos la propia función objetivo de la comparación
        if nombre == nombre_objetivo:
            continue

        res = similitud_hibrida(tokens_objetivo, tokens)
        ranking.append(( res["promedio"],nombre, res["es_clon"]))

    

    # Ordenamos de mayor a menor según el puntaje
    ranking.sort(reverse=True)

    return ranking[:k]


def main():
    args = construir_parser()
    # Paso 1: Extraccion.
    diccionario_de_funciones_ast = extraer_funciones(args.dir)
    if not isinstance(diccionario_de_funciones_ast, dict):
        print(f"Error: {diccionario_de_funciones_ast}")
        return

    # Paso 2: Normalizamos y serializamos cada función del repositorio
    funciones_tokens = {}

    for _,func_extraida in diccionario_de_funciones_ast.items():
        nodo_ast = func_extraida.nodo
        nodo_normalizado, _ = normalizar_arbol(nodo_ast)
        tokens = serializar(nodo_normalizado)
        funciones_tokens[func_extraida.nombre] = tokens

    if not args.funcion:
        print("Error: Debes especificar --funcion archivo.py:nombre")
        return
    # Paso 3: Similitud y Top K
    _, nombre_objetivo = args.funcion.split(":")
    resultados = buscar_top_k(nombre_objetivo, funciones_tokens, args.top)

    #Paso 4: Imprimimos el top
    print(f"\n--- Top {args.top} funciones más similares a '{nombre_objetivo}' ---")
    

    if not resultados:
        print("  No se encontraron otras funciones para comparar.")
        return

    # Encabezado de la tabla
    print("+-----+-----------------+------------+-------------+")
    print("|  #  | Función         | Similitud  | ¿Duplicado? |")
    print("+-----+-----------------+------------+-------------+")

    # Una fila por cada resultado
    posicion = 1
    for promedio_hibrido, nombre, es_clon in resultados:
        duplicado = "SI" if es_clon else "NO"
        print(f"| {posicion:^3} | {nombre:<15} | {promedio_hibrido:>9.2%}  | {duplicado:^11} |")
        posicion += 1

    # Cierre de la tabla
    print("+-----+-----------------+------------+-------------+")

if __name__ == "__main__":
    main()
