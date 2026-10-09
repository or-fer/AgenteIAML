# Agente Conversacional para E-Commerce: "Patitas pa' que las quiero"

**Institución:** Universidad Nacional Autónoma de México (UNAM) — Facultad de Ingeniería

**Asignatura:** Inteligencia Artificial

**Profesor:** Dr. José Fidel Urquiza Yllescas

**Autora:** María Fernanda Ordóñez Figueroa

**Fecha:** 10 de Octubre de 2026



## 1. Resumen Ejecutivo y Caso de Negocio

El presente proyecto implementa un agente conversacional (chatbot) de primera línea para la tienda de calzado deportivo **"Patitas pa' que las quiero"**. El sistema está diseñado para operar en un entorno de **dominio cerrado** utilizando el lenguaje estándar **AIML 2.0 (Artificial Intelligence Markup Language)**, garantizando respuestas deterministas, trazables y de alta precisión.

### Problema a Resolver

En el sector e-commerce de calzado deportivo, aproximadamente el 70% de las consultas en vivo corresponden a dudas operativas recurrentes:

* Seguimiento y rastreo de envíos.
* Cobertura de entrega a provincia y costos de flete.
* Métodos de pago aceptados y facturación fiscal.
* Políticas de cambio de talla y devoluciones.

La acumulación de estas consultas satura los canales de atención humana, retrasa la venta y dificulta la resolución de incidencias complejas.

### Solución Implementada

Un asistente virtual determinista estructurado en reglas de coincidencia de patrones que actúa como filtro primario. El agente identifica las variantes léxicas y sintácticas utilizadas por los usuarios, gestiona variables de sesión (como el nombre del cliente y número de guía), sostiene conversaciones contextuales y redirige las intenciones hacia respuestas estandarizadas.



## 2. Arquitectura del Sistema

El sistema adopta una arquitectura **modular y jerárquica**. El código fuente se divide en submódulos temáticos dentro del directorio `archivos_aiml/` (evitando conflictos de *namespace* con la librería ejecutable de Python) y es ensamblado en tiempo de ejecución por un motor central (`startup.aiml`).

```text
AgenteIAML/
├── main.py                   
├── README.md                 
└── archivos_aiml/            
    ├── startup.aiml          
    ├── saludos.aiml          
    ├── horarios.aiml         
    ├── ubicacion.aiml        
    ├── pagos.aiml           
    ├── productos.aiml       
    ├── precios.aiml         
    ├── promos.aiml          
    ├── pedidos.aiml         
    ├── facturacion.aiml   
    ├── devoluciones.aiml     
    └── fallback.aiml         

```


## 3. Especificación Técnica de Etiquetas AIML Empleadas

El desarrollo aprovecha los componentes avanzados de AIML 2.0 para lograr un flujo conversacional natural:

* **Estructura Base (`<category>`, `<pattern>`, `<template>`):** Unidad atómica del conocimiento que mapea las intenciones del usuario hacia salidas estandarizadas.
* **Redirección Canónica (`<srai>`):** Mapea múltiples variantes de lenguaje natural hacia un único patrón canónico, reduciendo la duplicidad de código.
* **Procesamiento de Comodines (`*`, `_`) y Extracción (`<star/>`):** Captura entradas compuestas o información dinámica (ej. nombres, números de guía o modelos de tenis) para procesarla o reincorporarla en la plantilla de respuesta.
* **Control Contextual (`<that>`):** Restringe la activación de una regla evaluando la última respuesta emitida por el bot. Se utiliza primordialmente para flujos de confirmación tipo Sí/No al solicitar números de guía o confirmar compras.
* **Manejo de Temas (`<topic>`):** Delimita un subconjunto de reglas activas únicamente cuando el usuario entra en un flujo específico (ej. la política de cambios y devoluciones), previniendo activaciones accidentales en el hilo general.
* **Memoria de Sesión (`<set>`, `<get>`):** Mantiene el estado de la conversación almacenando datos persistentes del usuario (`usuario`, `num_pedido`, `modelo_compra`, `talla_compra`).
* **Estructuras Condicionales (`<condition>`):** Evalúa el estado de las variables de sesión para personalizar la respuesta (ej. saludar por su nombre si ya se conoce, o pedirlo si es la primera interacción).
* **Respuestas Dinámicas (`<random>`):** Selecciona aleatoriamente entre varias alternativas de texto para evitar la rigidez en los saludos y respuestas por defecto.
* **Carga Dinámica (`<learn>`):** Carga modularizada de archivos `.aiml` invocada desde `startup.aiml`.


## 4. Requisitos del Sistema e Instalación

### Prerrequisitos

* **Lenguaje:** Python 3.8 o superior.
* **Paquete de Software:** Intérprete `python-aiml` (versión compatible con Python 3).

### Instalación del Entorno

1. Clonar o extraer el proyecto en el directorio de trabajo:
```bash
cd AgenteIAML

```


2. Crear y activar un entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate

```


3. Instalar la dependencia de AIML:
```bash
pip install python-aiml

```

## 5. Instrucciones de Ejecución y Guía de Pruebas

### Ejecución

Para iniciar el agente conversacional en la terminal, ejecute el archivo principal desde la raíz de la carpeta `AgenteIAML/`:

```bash
python main.py

```

### Casos de Prueba Sugeridos

| Intención / Módulo | Entrada del Usuario (Ejemplo) | Comportamiento Técnico Esperado |
| --- | --- | --- |
| **Bienvenida y Nombre** | `Hola, me llamo Fernando` | Almacena `Fernando` en la variable `usuario` usando `<set>`. |
| **Persistencia de Nombre** | `¿Quién soy?` | Recupera el nombre con `<get name="usuario"/>`. |
| **Rastreo con Contexto** | `¿Dónde está mi paquete?` <br>

<br> `Sí` <br>

<br> `GUIA98765` | Redirige vía `<srai>`, activa filtro contextual con `<that>`, guarda la guía y muestra el estado en tránsito. |
| **Aislamiento por Tema** | `Quiero hacer un cambio` <br>

<br> `Requisitos` | Activa `<topic name="CAMBIOS">` y responde exclusivamente dentro del contexto de devoluciones. |
| **Consultas Abiertas** | `¿Envían a Guadalajara?` | Captura la ciudad mediante el comodín `*` y confirma la cobertura nacional. |
| **Entradas Fuera de Dominio** | `¿Cuál es tu película favorita?` | Activa el patrón `*` en `fallback.aiml` ofreciendo sugerencias de uso de forma aleatoria (`<random>`). |

---

## 6. Dificultades Técnicas Encontradas y Soluciones

1.**Ambigüedad en Respuestas Cortas (Manejo de Contexto)**
* *Problema:* Entradas monosilábicas como "Sí" o "No" generaban colisiones de patrones al no saber a qué pregunta previa del sistema correspondían.
* *Solución:* Se implementó la etiqueta `<that>` en el módulo de envíos y pedidos, garantizando que el patrón "SI" o "NO" solo se active si la oración previa emitida por el bot solicitaba explícitamente dicha confirmación.


2. **Duplicidad de Patrones por Sinonimia**
* *Problema:* Existían múltiples formas en que los usuarios preguntaban por el catálogo o rastreo (ej. "dónde están mis tenis", "seguimiento", "rastrear paquete").
* *Solución:* Se utilizó una arquitectura de reducción donde todas las variantes se redirigen con `<srai>` a un único patrón canónico (`COMO RASTREO MI PEDIDO`), manteniendo el código limpio y fácil de mantener.

3. **Sensibilidad a Tildes y Normalización en Español**
* Problema: `python-aiml` no convierte caracteres con tilde (á, é, í, ó, ú) a sus equivalentes sin tilde, provocando fallos de coincidencia entre entradas del usuario como "CÓMO" y patrones definidos como "COMO".
* Solución: Se implementó un preprocesamiento de entrada en `main.py` mediante el módulo `unicodedata` de Python. La función descompone los caracteres Unicode y remueve las marcas diacríticas, garantizando que el motor AIML reciba siempre texto en mayúsculas sin acentos antes del filtrado de patrones.


---

## 7. Licencia y Créditos

Este software ha sido desarrollado con fines académicos bajo la licencia **GNU General Public License v3.0 (GPL-3.0)** como parte de los entregables de la asignatura de Inteligencia Artificial de la Facultad de Ingeniería, UNAM.