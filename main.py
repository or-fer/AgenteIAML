import aiml
import os

kernel = aiml.Kernel()

if os.path.exists("archivos_aiml/startup.aiml"):
    kernel.learn("archivos_aiml/startup.aiml")
    kernel.respond("CARGAR BOT")
else:
    print("Error: No se encontró archivos_aiml/startup.aiml")

print("\n=======================================================")
print("  Bienvenido a 'Patitas pa' que las quiero' - Chatbot")
print("=======================================================")
print("Escribe 'salir' para terminar la conversación.\n")

while True:
    entrada = input("Usuario > ")
    if entrada.lower() == "salir":
        print("\nBot > ¡Gracias por visitar 'Patitas pa' que las quiero'! ¡Hasta pronto!")
        break
    respuesta = kernel.respond(entrada)
    print(f"Bot > {respuesta}\n")
    