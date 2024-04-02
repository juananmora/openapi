
# LLM Service
## Descripción

LLM Service es una API construida con FastAPI que facilita la interacción con Modelos LLM, permitiendo a los usuarios enviar solicitudes de procesamiento de lenguaje natural y recibir respuestas generadas por la inteligencia artificial. Este servicio se diseñó para ser desplegado en Contenedores, aprovechando las capacidades de los diferentes modelos LLM.
### Estructura del Repositorio

    llm/     
        main.py: Archivo principal que inicia la aplicación FastAPI, define las rutas de la API y configura el entorno de ejecución.

    requirements.txt: Lista todas las dependencias necesarias para ejecutar el proyecto, asegurando un entorno consistente.



## Pruebas Locales

### Para probar los cambios localmente, sigue estos pasos:

- Configura tu entorno: Asegúrate de tener Python 3.7+ y pip instalados. Crea un entorno virtual y activarlo:

    bash

        python -m venv venv
        source venv/bin/activate  # Unix/macOS
        venv\Scripts\activate  # Windows

- Instala las dependencias:

    bash

        pip install -r requirements.txt



### Ejecuta la aplicación:

    bash

        uvicorn llm.main:app --host 0.0.0.0 --port 8000 --reload

        Esto iniciará el servidor FastAPI en localhost en el puerto 8000.

- Prueba la API:

    Accede a http://127.0.0.1:8000/docs para ver la documentación de la API y realizar pruebas interactivas.

    Utiliza herramientas como Postman o cURL para hacer solicitudes a tu API localmente y verificar las respuestas.



## Entorno dockerizado

    docker build -t openapi:latest .
    docker run --name openapi -d -p 8001:8000 openapi:latest

- Prueba la API:

    Accede a http://127.0.0.1:8001/docs para ver la documentación de la API y realizar pruebas interactivas.
    
    Utiliza herramientas como Postman o cURL para hacer solicitudes a tu API localmente y verificar las respuestas.