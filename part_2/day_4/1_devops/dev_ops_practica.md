---
marp: true
theme: default
paginate: true
class: invert
---

# Introducción a los desplieges automáticos con GitHub Actions

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

---

- Vamos a automatizar el despliege del API.
- Para ello usaremos GitHub Actions, Google Cloud Build y Cloud Run.
- GitHub Actions provisiona una máquina en la que podemos ejecutar una serie de acciones cuando ocurre algún evente en nuestro repositorio.
- En nuestro claso desplegaremos una nueva versión cuando hagamos un push a main.

---

![center](imgs/devopsaction.png)

---
- Definimos el proceso de despliege en una fichero YAML:

```yaml
name: Build and Deploy to Cloud Run

on:
  push:
    branches:
    - main

env:
  PROJECT_ID: ${{ secrets.RUN_PROJECT }}
  RUN_REGION: europe-west1
  SERVICE_NAME: api-cloud-run

jobs:
  setup-build-deploy:
    name: Setup, Build, and Deploy to Cloud Run
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      uses: actions/checkout@v2

    # Setup gcloud CLI
    - uses: GoogleCloudPlatform/github-actions/setup-gcloud@master
      with:
        version: '290.0.1'
        service_account_key: ${{ secrets.RUN_SA_KEY }}
        project_id: ${{ secrets.RUN_PROJECT }}

    # Build and push image to Google Container Registry
    - name: Build
      run: |-
        gcloud builds submit \
          --quiet \
          --tag "gcr.io/$PROJECT_ID/$SERVICE_NAME:$GITHUB_SHA"

    # Deploy image to Cloud Run
    - name: Deploy
      run: |-
        gcloud run deploy "$SERVICE_NAME" \
          --quiet \
          --region "$RUN_REGION" \
          --image "gcr.io/$PROJECT_ID/$SERVICE_NAME:$GITHUB_SHA" \
          --platform "managed" \
          --allow-unauthenticated
```
- Este fichero tiene que estar en la carpeta .github/workflows.

---

- El proceso necesita dos variables de entorno:
    - RUN_PROJECT: Nombre del proyecto donde vamos a desplegar nuestra aplicación.
    - RUN_SA_KEY: Key de un service account con los siguientes permisos:
        - Service Account User
        - Cloud Build Editor
        - Cloud Run Admin
        - Viewer

---
# Ejemplo
- Primero generamos el service account con los permisos necesarios.

![center](imgs/s1.png)

![center](imgs/s2.png)

---

![center](imgs/s3.png)

---

- Podemos poner el permiso de owner aunque no es lo correcto.

![center](imgs/s5.png)

---
![center](imgs/s6.png)

---
- Generamos el json con la key del service account.
![center](imgs/s7.png)

---


![center](imgs/s8.png)
---

![center](imgs/s9.png)

---
- Añadimos las variables a GitHub.

![center](imgs/1.png)

![center](imgs/2.png)

---
![center](imgs/3.png)
![center](imgs/4.png)

---
![center](imgs/5.png)

---
![center](imgs/6.png)

---
- Añadimos el fichero al repositorio.
- Si todo está correcto al hacer el push la aplicación se deplegará automáticamente.
- Podemos verlo en el menú de github actions.
![center](imgs/7.png)
---

![center](imgs/8.png)

---
- Si entramos en el registy veremos que hay una nueva imagen.
![center](imgs/9.png)

---

- Tendremos una nueva revisión en nuestro servico de cloud run.
![center](imgs/10.png)

---
# Ejercicio
- Configura el despliege automático para tu dash.

