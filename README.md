# Deploy de Flask ML API en Google Cloud Platform (GCP) ☁️

### Configuración del entorno

Puedes echar un vistazo a detalle en la siguiente presentación, la cual incluye detalles de configuración y creación del servicio.

### Preparación del modelo

- Se utiliza un cuaderno de Google Colab para entrenar un modelo sencillo de clasificación de especies en Iris. El cuaderno puede ser encontrado en la carpeta [notebooks](/noteboks).
- Una vez entrenado el modelo, deberás descargarlo y guardarlo en la carpeta principal de este repositorio. Puedes encontrar como ejemplo el modelo actual [model.joblib](/model.joblib).

### Preparación de la API

- Es necesario implementar la API con el nmbre de objeto `app` en el archivo `app.py`.
- Ahí se especifican las rutas y métodos que se utilizarán para la API.

### Configuración de Google Cloud Platform

- Crea un nuevo proyecto en GCP (si puedes, guarda el `Project ID`).
- Activa las APIs de Cloud Build y Cloud Run. Para hacerlo, simplemente búscalas en la barra de búsqueda de GCP y actívalas.

### Instalar e inicializar el Google Cloud SDK
- Puedes seguir la guía de instalación a continuación: [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install). Esta guía instalará el SDK de Google Cloud y te permitirá utilizar la terminal para interactuar con los servicios de GCP.
- Una vez instalado el SDK (`gcloud CLI`), deberás inicializarlo con el comando `gcloud init`. Este comando te pedirá que inicies sesión con tu cuenta de Google y te permitirá seleccionar el proyecto que acabas de crear.

### Crear Dockerfile y configuración de la app
- Puedes seguir la guía a continuación: [https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python?hl=es-419](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python?hl=es-419). Esta guía te permitirá crear un archivo `Dockerfile` y configurar tu app para que pueda ser desplegada en Cloud Run.
- Nota que además de crear el `Dockerfile`, deberás crear un archivo llamado `requirements.txt` que incluya las dependencias de tu app (puedes encontrar un ejemplo en [requirements.txt](/requirements.txt)) y crear un archivo llamado `.dockerignore` (puedes encontrar un ejemplo en [.dockerignore](/.dockerignore)).
- Nota que como parte de las configuraciones en la aplicación, tenemos detalles importantes en el método run:
    ```python
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
    ```

### Ejecutrar cloud build & deploy

Finalmente, podremos ejecutar los siguientes comandos para hacer build y deployment del servicio en GCP. Para ello, será necesario utilizar el `Project ID` que guardaste al crear el proyecto y especificar el nombre la función que realiza inferencia en nuetsra aplicación (en nuestro caso es [`predict`](/app.py#L34)).
```bash
gcloud builds submit --tag gcr.io/<project_id>/<function_name>
gcloud run deploy --image gcr.io/<project_id>/<function_name> --platform managed
```

---

### **🔐 SOBRE EL USO DE INFORMACIÓN TOTAL O PARCIAL:**

- Estos documentos fueron originalmente creados por el autor.
- Cualquier uso de estos documentos o sus contenidos están permitidos a través de la licencia provista y sus condiciones.
- Para cualquier aclaración, puedes contactar al autor: https://rodolfoferro.xyz/

**Copyright (c) 2024 Rodolfo Ferro**