---
marp: true
theme: default
paginate: true
---

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

# Amazon Elastic Container Registry (Amazon ECR) 

---


- Amazon Elastic Container Registry (Amazon ECR) es unAWSUn servicio de registro de imágenes de contenedor administrado de seguro, escalable y fiable.
- Puede utilizar la CLI de Docker para insertar, extraer y administrar imágenes en los repositorios de Amazon ECR.

---


![center](imgs/ecr.png)


---

Necesitamos:
- Tener instalada y configurada la AWS CLI. 
- El usuario debe tener los permisos necesarios de IAM para tener acceso al servicio Amazon ECR. 

---

# Etiquetado de la imagen y envío a Amazon ECR

- Se crea un repositorio de Amazon ECR para almacenar su imagen.
- En los resultados, anote el repositoryUri. 
```bash
aws ecr create-repository --repository-name repository-name --region region
```
- Se puede crear tambien el repositorio en la consola de Amazon ECR. 

---

- Etiquete la imagen  con el valor de repositoryUri del paso anterior.
```bash
docker tag hello-world aws_account_id.dkr.ecr.region.amazonaws.com/repository-name
```

---

- Ejecute el comando aws ecr get-login-password.
-  Especifique el URI del registro en el que desea autenticar. 

```bash
aws ecr get-login-password | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
```

- Tiene que devolver: Login Succeeded

---

- Envíe la imagen a Amazon ECR con el valor repositoryUri del paso anterior.

```bash
docker push aws_account_id.dkr.ecr.region.amazonaws.com/repository-name
```


---

# Ejecicio

- Programa un api con fastapi con un metodo GET.
- Dockeriza el api como vimos anteriormente. No utilices volumenes.
- Construye la imagen localmente y prueba su funcionamiento.
- Cree un nuevo repositorio en ECR, donde almacenaremos nuestra imagen con la aplicación de ejemplo.
- Realiza un push de la imagen del api creada anteriormente al nuevo repositorio en ECR.




