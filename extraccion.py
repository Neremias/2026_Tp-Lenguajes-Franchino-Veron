import ast
from dataclasses import dataclass
from pathlib import Path

@dataclass
class FuncionExtraida:
    nombre: str          # nombre original (solo informativo, NO influye en la similitud)
    archivo: str         # ruta del archivo donde está definida
    linea: int           # línea donde empieza (node.lineno)
    nodo: ast.AST        # subárbol AST completo de la función

def extraer_funciones(directorio):
    funciones_extraidas = {}
    ruta = Path(directorio)
    contador = 1

    if not ruta.is_dir():
        return "El directorio no existe"
    
    for archivo in ruta.rglob("*.py"): #busco recursivamente en el directorio archivos con .py
        if not archivo.is_file():
            continue #verifico que sea un archivo. 
            
        try:
            cadena = archivo.read_text(encoding="utf-8") #lee el archivo y lo guarda en memoria. 
            arbol = ast.parse(cadena, filename=str(archivo)) #Nodo Raiz: Ast.Module
                    
        except (SyntaxError, UnicodeDecodeError) as e:
            print(f"No se pudo parsear {archivo}: {e}")
            continue  # Salta al siguiente archivo si falla

        #Ahora, recorremos el árbol parseado desde el nodo raiz. 
        for nodo in ast.walk(arbol):
            if type(nodo) == ast.FunctionDef or type(nodo) == ast.AsyncFunctionDef:
                funcion = FuncionExtraida(nodo.name, archivo,nodo.end_lineno - nodo.lineno,nodo)
                funciones_extraidas[f"F{contador}:"] = funcion 
                contador += 1
    return funciones_extraidas