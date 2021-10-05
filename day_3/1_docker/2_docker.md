---
marp: true
theme: default
paginate: true
class: invert
---
# Dockerizando una API.
---


---
- Usando el Dockerfile del directorío ejemplo_docker_2, construye la imagen y ejecuta el contenedor usando los siguientes comandos:
```bash
docker build -t my_api .
docker run -p 8080:8080 my_api 
```

--- 
# Volúmenes

- En algunos casos para desarrollar en vez de copiar el código en la construcción de la imagen usamos un volumen.
- Un volumen es un directorio compartido entre el host y el contenedor.

---

- Eliminamos la parte que hace el COPY del dockerfile. Puedes verlo en ejemplo_docker_3.
- Si ejecutas la aplicación de la siguiente manera:
```bash
docker build -t my_api .
docker run -p 8080:8080 -v ${PWD}/src:/code my_api 
```
- Veras que si actualizas el fichero app.py la aplicación se actualiza y no tenemos que construir todo de nuevo.
