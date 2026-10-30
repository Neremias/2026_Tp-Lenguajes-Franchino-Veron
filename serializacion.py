from normalizacion import preorder
import ast

def extraer_valor_nodo(nodo):
      if isinstance(nodo,ast.arg):
          return nodo.arg

      elif isinstance(nodo, ast.Name):
          return nodo.id

      elif isinstance(nodo, ast.Constant):
          return nodo.value
      
      elif isinstance(nodo, ast.expr_context):
        return None
      
      else:
          return type(nodo).__name__
      
      return None


def serializar(nodo_normalizado):
    lista_de_tokens = []
      
    for nodo in preorder(nodo_normalizado):
      token = extraer_valor_nodo(nodo)
      if token is not None:
        lista_de_tokens.append(token)
    return lista_de_tokens