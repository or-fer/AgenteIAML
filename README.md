# Práctica 2: Desarrollo de un Agente Conversacional con AIML

**Asignatura:** Inteligencia Artificial  
**Institución:** Universidad Nacional Autónoma de México (UNAM) — Facultad de Ingeniería  
**Profesor:** Dr. José Fidel Urquiza Yllescas
**Alumno(a):** María Fernanda Ordóñez Figueroa  

---

## ## 1. Descripción del Proyecto

Este proyecto consiste en el desarrollo de un agente conversacional (chatbot) de dominio cerrado basado en reglas utilizando **AIML 2.0**. El objetivo principal es estructurar una base de conocimientos modular y robusta capaz de gestionar interacciones deterministas mediante el procesamiento de patrones, comodines, control de contexto, memoria de sesión y redirección lógica.

El dominio seleccionado es el **5.1. Sector E-Commerce: "Dudas repetitivas"**, implementando un asistente virtual de primera línea para la tienda en línea de calzado deportivo **"Patitas pa' que las quiero"**. El bot atiende de forma autónoma el 70% de las consultas frecuentes del negocio (rastreo de pedidos, envíos a provincia, métodos de pago, catálogo por disciplina y políticas de cambio).
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
AgenteIAML/
├── main.py
└── archivos_aiml/
    ├── startup.aiml
    ├── saludos.aiml
    ├── envios.aiml
    ├── pagos.aiml
    ├── cambios.aiml
    ├── horarios.aiml
    ├── ubicacion.aiml
    ├── productos.aiml
    ├── precios.aiml
    ├── promos.aiml
    ├── pedidos.aiml
    ├── facturacion.aiml
    ├── devoluciones.aiml
    └── fallback.aiml
```