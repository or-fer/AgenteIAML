# Práctica 2: Desarrollo de un Agente Conversacional con AIML

**Asignatura:** Inteligencia Artificial  
**Institución:** Universidad Nacional Autónoma de México (UNAM) — Facultad de Ingeniería  
**Profesor:** Dr. José Fidel Urquiza Yllescas
**Alumno(a):** María Fernanda Ordóñez Figueroa  

---

## 1. Descripción del Proyecto

Este proyecto consiste en el desarrollo de un agente conversacional (chatbot) de dominio cerrado basado en reglas utilizando **AIML (Artificial Intelligence Markup Language) 2.0**. El objetivo principal es estructurar una base de conocimientos modular y robusta capaz de gestionar interacciones deterministas mediante el procesamiento de patrones, comodines, control de contexto, gestión de memoria de sesión y redirección lógica.

El dominio seleccionado para esta implementación es el **[Indicar el sector elegido, ej. Sector E-Commerce / Soporte Técnico]**, simulando un asistente virtual de primera línea capaz de resolver consultas frecuentes de manera autónoma y estandarizada.

---

## 2. Etiquetas AIML Empleadas

Para la construcción del "cerebro" del chatbot se hizo uso de las siguientes etiquetas y características avanzadas de AIML 2.0:

*   **`<category>`, `<pattern>`, `<template>`:** Estructura fundamental para asociar una entrada normalizada del usuario con una respuesta del sistema.
*   **Comodines (`*`, `_`) y `<star/>`:** Utilizados para capturar secuencias de palabras abiertas en los patrones y reutilizar dichos valores dentro de las plantillas.
*   **Redirección con `<srai>`:** Permite centralizar la lógica y manejar sinónimos o variaciones de frases redirigiéndolas a un patrón canónico.
*   **Contexto conversacional con `<that>`:** Restringe la activación de ciertos patrones basándose específicamente en la respuesta previa emitida por el bot (ideal para confirmaciones de tipo Sí/No).
*   **Gestión de memoria de sesión (`<set>`, `<get>`):** Almacenan y recuperan variables de usuario (como su nombre, datos de pedidos o estados temporales).
*   **Estructuras condicionales (`<condition>`):** Permiten evaluar el valor de las variables de sesión para desplegar respuestas personalizadas o alternativas por defecto.
*   **Selección aleatoria (`<random>`):** Introduce variedad en las respuestas dinámicas del asistente.
*   **Carga modular (`<learn>`):** Utilizada en el archivo de arranque (`startup.aiml`) para ensamblar dinámicamente todos los submódulos de conocimiento.

---

## 3. Estructura del Código Fuente

El proyecto se encuentra organizado de forma modular por jerarquías y temáticas en el directorio `aiml/`:

```text
practica02-aiml/
│
├── aiml/
│   ├── startup.aiml          # Archivo de arranque y carga de módulos (<learn>)
│   ├── saludos.aiml          # Interacciones iniciales y bienvenidas
│   ├── horarios.aiml         # Consultas de disponibilidad y tiempos de atención
│   ├── ubicacion.aiml        # Referencias geográficas y de llegada
│   ├── pagos.aiml            # Métodos de pago aceptados y pasarelas
│   ├── productos.aiml        # Disponibilidad de catálogo y alternativas
│   ├── precios.aiml          # Tarifas y costos específicos
│   ├── promos.aiml           # Ofertas y descuentos vigentes
│   ├── pedidos.aiml          # Lógica de pedidos, variables y confirmación (<that>)
│   ├── facturacion.aiml      # Requisitos y procesos fiscales
│   ├── devoluciones.aiml     # Políticas y plazos de devolución
│   └── fallback.aiml         # Manejo de entradas no reconocidas (comodín '*')
│
├── README.md                 # Documentación técnica del proyecto
└── [Opcional: Capturas o scripts de ejecución]