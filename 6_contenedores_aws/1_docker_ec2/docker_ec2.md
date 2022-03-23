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

# Docker en EC2

---


- Si tienes problemas para instalar docker en tu máquina  o prefieres usar la instancia EC2. Podemos instalar docker en ella.
- Podemos usar docker para desplegar  apliciones en instancias EC2.

---

# Instalación
- Lance una instancia con la AMI de Amazon Linux 2. 
- Conecte con la instancia, puedes usar ssh, vscode o la interfaz web.
- Actualice la caché de paquetes y los paquetes instalados en la instancia.

```bash
sudo yum update -y
```

---

- Instale el paquete de Docker Engine de más reciente.
```bash
sudo amazon-linux-extras install docker
```
- Abra el servicio de Docker.
```bash
sudo service docker start
```
- Agregue el ec2-user al grupo docker para que pueda ejecutar comandos de Docker sin usar sudo.
```bash
sudo usermod -a -G docker ec2-user
```

---
- Cierre sesión y vuelva a iniciarla para actualizar los nuevos permisos de grupo de docker. Para ello, cierre la ventana de su terminal de SSH actual y vuelva a conectarse a la instancia en una ventana nueva. De esta forma, la nueva sesión de SSH tendrá los permisos de grupo de docker adecuados.

- Compruebe que el ec2-user puede ejecutar comandos de Docker sin sudo.
```bash
docker info
```

---

# Ejercicio
- Instale docker en la máquina EC2.
- Compruebe con una imagen de python si esta correctamente instalado:
```bash
docker run -it python:3.8 bash
```
- Programa un api con fastapi con un metodo GET.
- Dockeriza el api como vimos anteriormente. No utilices volumenes.
- Construye la imagen localmente y prueba su funcionamiento localmente.
- Prueba a cambiar los ajustes de seguridad de la instancia para exponer el puerto en el que funciona la api a internet.
- Comprueba si puedes acceder desde tu ordenador.

