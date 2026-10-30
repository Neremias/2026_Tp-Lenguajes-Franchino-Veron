"""Permite que pytest encuentre los módulos del proyecto."""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(RAIZ))
# Los módulos (normalizacion.py, serializacion.py, similitud.py...) están en esta carpeta:
sys.path.insert(0, str(RAIZ / "Aprendizaje_modulo_extraccion"))
