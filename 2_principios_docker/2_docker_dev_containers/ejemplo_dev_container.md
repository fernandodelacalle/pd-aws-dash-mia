---
marp: true
theme: default
paginate: true

---
# Entorno de desarrollo con contenedores en vscode

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

---

- La extensión Visual Studio Code Remote - Containers permite usar un contenedor docker como entorno de desarrollo.
<br />
![center](imgs/dev_cont.png)
- Es parecido a la extensión Remote SSH.

---
# Ejemplo
- Un fichero con nombre: devcontainer.json en la carpeta .vscode permite la configuración de todo el entorno.
- Puedes ver un ejemplo en la carpeta ejemplo_dev_container.
---
# Ejemplo
- Abrir la carpeta en vscode.
- Instalar la extensión remote containers.
<br />
![center](imgs/1.png)

---

# Ejemplo
- Pulsar el boton verde: 
![center](imgs/2.png)
- Seleccionar la opción: open in remote container.
![center](imgs/3.png)

---

- Una vez construida la imagen el vscode estará integrdo dentro de nuestro contenedor de desarrollo.
![center height:15cm](imgs/4.png)