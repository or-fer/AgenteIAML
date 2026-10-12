"""Preprocesamiento de la entrada del usuario, compartido por main.py y probar.py.

PyAIML hace coincidir PATRONES en MAYUSCULAS y solo limpia puntuacion ASCII, por lo que:
  * 'CÓMO' no coincide con el patron 'COMO' entonces se quitan tildes
  * '¿' y '¡' no se eliminan, se quitan todos los signos
Todos los patrones de archivos_aiml/ estan escritos en MAYUSCULAS, sin tildes ni signos.
"""
import re
import unicodedata


def normalizar_entrada(texto):
    nfkd = unicodedata.normalize("NFD", texto)
    sin_acentos = "".join(c for c in nfkd if unicodedata.category(c) != "Mn")
    solo_alfanum = re.sub(r"[^A-Za-z0-9\s]", " ", sin_acentos)   # quita signos (¿?¡!,.' ...)
    return " ".join(solo_alfanum.upper().split())
