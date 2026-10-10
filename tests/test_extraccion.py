"""
test_extraccion.py
------------------
Tests de la etapa de extracción (req. 4.1). Pendientes hasta implementar
extraccion.py.
"""

import pytest

pendiente = pytest.mark.skip(reason="pendiente: implementar extraccion.py")


@pendiente
def test_extrae_nombre_y_linea():
    """Debe devolver nombre original, archivo y línea de cada función."""
    raise NotImplementedError


@pendiente
def test_archivo_con_error_de_sintaxis_no_corta():
    """Un .py que no parsea se omite sin interrumpir el recorrido."""
    raise NotImplementedError
