import aiml
import os
import unicodedata
# normalizacion
def normalizar_entrada(texto):
   
    nfkd_form = unicodedata.normalize('NFD', texto)
    texto_sin_acentos = "".join([c for c in nfkd_form if unicodedata.category(c) != 'Mn'])
    texto_limpio = texto_sin_acentos.replace("'", "").replace("’", "")
    return texto_limpio.upper().strip()

kernel = aiml.Kernel()

startup_path = os.path.join("archivos_aiml", "startup.aiml")

if os.path.exists(startup_path):
    kernel.learn(startup_path)
    kernel.respond("CARGAR BOT")
else:
    print(f"Error: No se encontró {startup_path}")

print("\n=======================================================")
print("  Bienvenido a 'Patitas pa' que las quiero' - Chatbot")
print("=======================================================")
print("Escribe 'salir' para terminar la conversación.\n")

while True:
    entrada = input("Usuario > ")
    if entrada.lower() == "salir":
        print("\nBot > ¡Gracias por visitar 'Patitas pa' que las quiero'! ¡Hasta pronto!")
        break
    
    entrada_normalizada = normalizar_entrada(entrada)
    respuesta = kernel.respond(entrada_normalizada)
    print(f"Bot > {respuesta}\n")