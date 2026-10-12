import os
import aiml
from normalizar import normalizar_entrada

kernel = aiml.Kernel()

startup_path = os.path.join("archivos_aiml", "startup.aiml")

if os.path.exists(startup_path):
    kernel.learn(startup_path)
    kernel.respond("CARGAR BOT")
else:
    raise SystemExit(f"Error: No se encontró {startup_path}. Ejecuta main.py desde la raíz del proyecto.")

print("\n=======================================================")
print("  Bienvenido a 'Patitas pa' que las quiero' - Chatbot")
print("=======================================================")
print("Escribe 'salir' para terminar la conversación.\n")

while True:
    try:
        entrada = input("Usuario > ")
    except (KeyboardInterrupt, EOFError):
        print("\n\nBot > ¡Gracias por visitar 'Patitas pa' que las quiero'! ¡Hasta pronto!")
        break
    if entrada.strip().lower() == "salir":
        print("\nBot > ¡Gracias por visitar 'Patitas pa' que las quiero'! ¡Hasta pronto!")
        break
    if not entrada.strip():
        continue

    respuesta = kernel.respond(normalizar_entrada(entrada))
    print(f"Bot > {respuesta}\n")
