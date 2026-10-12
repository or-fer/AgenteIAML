"""Ejecuta la batería de pruebas contra el bot REAL (python-aiml).

    python probar.py
"""
import os
import sys
import aiml
from normalizar import normalizar_entrada
from pruebas.casos import CASOS, FLUJOS


def nuevo_kernel():
    k = aiml.Kernel()
    k.learn(os.path.join("archivos_aiml", "startup.aiml"))
    k.respond("CARGAR BOT")
    return k


def es_fallback(r):
    return (not r.strip()) or any(s in r for s in ("no entendí", "No estoy seguro", "persona del equipo"))


def main(verbose):
    ok, fallas = 0, []
    for entrada, marcador in CASOS:
        r = nuevo_kernel().respond(normalizar_entrada(entrada))
        bien = (not es_fallback(r)) if marcador == "?" else (marcador in r)
        ok += bien
        if not bien:
            fallas.append((entrada, marcador, r[:80]))
    print(f"Casos de una entrada: {ok}/{len(CASOS)} ({100 * ok // len(CASOS)}%)")

    fl_ok = 0
    for nombre, pasos in FLUJOS.items():
        k, bien, traza = nuevo_kernel(), True, []
        for entrada, marcador in pasos:
            r = k.respond(normalizar_entrada(entrada))
            paso_ok = marcador in r
            bien &= paso_ok
            traza.append((entrada, marcador, r[:80], paso_ok))
        fl_ok += bien
        if not bien:
            fallas.append((f"[flujo] {nombre}", "", " | ".join(f"{e}->{r}" for e, m, r, o in traza if not o)))
    print(f"Conversaciones con contexto: {fl_ok}/{len(FLUJOS)}")

    if verbose:
        for f in fallas:
            print("  FALLA:", f)
    return 0 if ok == len(CASOS) and fl_ok == len(FLUJOS) else 1


if __name__ == "__main__":
    sys.exit(main("-v" in sys.argv))
