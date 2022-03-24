# Contenidos

## 1. Principios de desarrollo
- Introducción a GIT.
- Conceptos básicos de redes.
- Introducción a la Terminal.
- Python Virtual Enviroments.
- Desarrollo de APIs en python con Fast API.

## 2. Principios de desarrollo: Docker
- Docker
- Desarrollo desde Docker en vscode.
- Kubernetes.

---

## 3. AWS EC2
- Introducción a AWS.
- Máquinas Virtuales en AWS: EC2
- Desarrollo en remoto con vscode y SSH.
- Cronjobs.
- Variables de entorno.
- Despliegue de un API en EC2.

## 4. AWS S3
- Almacenamiento S3.

## 5. AWS Lambda.
- Funciones Lambda.
- Registro de imágenes Docker en AWS ECR.
- Funciones Lambda con Docker.

---

## 6. Contenedores en AWS: ECS y Amazon Lightsail.
- Despliege de imágenes Docker en AWS EC2.
- Despliege de imágenes Docker en AWS ECS.
- Despliege de imágenes Docker en Amazon Lightsail.


---

## 7. Filosodia DevOps, AWS RDS, AWS Dynamo
- Filosofía Devops.
- Acciones de Github.
- Ejemplo DevOps AWS Lambda.
- Ejemplo DevOps AWS EC2 y ECR.

## 8. Bases de datos en AWS: AWS RDS, AWS Dynamo
- Bases de Datos Relacionales en AWS: RDS
- AWS Athenea
- Bases de Datos Relacionales en AWS: Dynamo

## 9. Machine Learing y MLOps: AWS Sagemaker
- Introducción a AWS SageMaker.

---

## 10. Técnicas de visualización
- Introducción a HTML
- Introducción a CSS
- Introducción a Flask
- Gráficos interactivos con Plotly
- Interfaces interactivas con Dash
- Despliege de aplicación web en AWS, Google Cloud y Azure.

### Proyecto final

# Otros
- Para convertir las diapositivas de md a pdf usar el comando:
```bash
docker run --rm --init -v $PWD:/home/marp/app/ -e LANG=$LANG marpteam/marp-cli **/*.md  --pdf --allow-local-files
```