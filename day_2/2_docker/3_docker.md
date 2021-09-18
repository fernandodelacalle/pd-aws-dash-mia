---
marp: true
theme: default
paginate: true
class: invert
--- 
# Docker Compose

--- 
# Docker Compose
- Podemos usar docker-compose para simplificar el proceso de desarrollo.
- Un fichero docker-compose define todo lo necesario para construir las imágenes y ejecutar los contenedores.
- En el repositorio de las clases de optimización tenéis un ejemplo.

---

- Los ficheros Docker Compose están en formato yaml.
- En ejemplo_docker_4 puedes ver un ejemplo:
```yaml
version: '3'
services:

  myapi:
    build: 
      context: .
      dockerfile: ./Dockerfile
    ports:
      - 8080:8080
    volumes:
      - ./src:/code
```

---

- De esta manera para construir la imagen solo tenemos que hacer:
```bash
docker-compose build
```
- Para ejecutar el contenedor:
```bash
docker-compose up
```

---
# Múltiples contenedores
- Podemos ejecutar varios contenedores a la vez usando docker-compose.
![center](imgs/compose.png)



---
- En ejemplo_docker_5, puedes ver un ejemplo donde se ejecutan 2 contenedores:
    - mongo: base de datos mongo.
    - mongo-express: aplicación web para ver los datos del mongo.
    - jupyter: ejecuta un jupyter-lab desde el que podemos hacer pruebas.
- docker-compose genera una red interna haciendo posible la comunicación entre los distintos contenedores.
