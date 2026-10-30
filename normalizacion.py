import ast

def preorder(nodo, lista_nodos=None):
    if(lista_nodos is None):
        lista_nodos = []

    lista_nodos.append(nodo)

    for hijo in ast.iter_child_nodes(nodo):
        preorder(hijo, lista_nodos)

    return lista_nodos

def normalizar_arbol(nodo_ast):
    dic_func = {}
    i = 0
    for nodo in ast.walk(nodo_ast): 
        # Argumentos
        if isinstance(nodo, ast.arg):
            if nodo.arg not in dic_func:
                i += 1
                dic_func[nodo.arg] = f"Var{i}"
            nodo.arg = dic_func[nodo.arg]

        # Variables
        elif isinstance(nodo, ast.Name):
            if isinstance(nodo.ctx, ast.Store):
                if nodo.id not in dic_func:
                    i += 1
                    dic_func[nodo.id] = f"Var{i}"
                nodo.id = dic_func[nodo.id]

            elif isinstance(nodo.ctx, ast.Load):
                if nodo.id in dic_func:
                    nodo.id = dic_func[nodo.id]

        # Constantes
        elif isinstance(nodo, ast.Constant):
            if isinstance(nodo.value, bool):
                nodo.value = "LIT_BOOL"
            elif isinstance(nodo.value, (int, float)):
                nodo.value = "LIT_NUM"
            elif isinstance(nodo.value, str):
                nodo.value = "LIT_STR"
            else:
                nodo.value = "LIT_OTRO"
            
    return nodo_ast, dic_func