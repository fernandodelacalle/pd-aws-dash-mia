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


# Nuestra primera aplicación en AWS.

--- 


Vamos a desplegar el API que acabamos de hacer en AWS:

- Para ello crearemos una máquina EC2 t2.micro. Es importante que en el proceso de creación abramos el puerto http, para ello al crearla configurar el security group de la siguiente manera:


- Crea un nuevo repositorio de código en github.
- Clona el repositorio.
- Genera un nuevo virtual enviroment.
- Instala los paquetes necesarios y genera un fichero de requeriments.
- Escribe una API con FastApi que tengá un método GET en el path "/suma" que reciva dos parametros de tipo int y los sume.

---
- Realiza un commit con todos los cambios y un push a github (CUIDADO venv!).
- Ejecutamos la aplicación en nuestra máquina EC2.
- Consulata la ip publica de la máquina.
- Prueba desde un navegador si funciona con: ```http://IP_MAQUINA/docs```.
