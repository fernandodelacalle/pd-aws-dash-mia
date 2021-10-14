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

# Variables de entorno

---

- Una variable de entorno es una variable dinámica que puede afectar al comportamiento de los procesos en ejecución en un ordenador. 
- Un ejemplo típico es tener almacenar las contraseñas o API keys en estas variables.

---

- En bash, se muestra el valor de una variable mediante:
```bash
echo $PATH
```
- El comando:
```bash
env
```
muestra todas las variables de entorno junto con sus respectivos valores.

----


- La forma de asignar un valor a una variable es:
```bash
variable=valor
```
- Pueden usarse también el siguient comando en bash
```bash
export VARIABLE=valor
```
- Exite un fichero: .bash_profile en el raiz de nuestro usuario donde podemos definir variables y otros comandos que queremos que se ejecuten o esten disponibles cada vez que abrimos una terminal.

---

- Desde python podemos leer estas variables de entorno y incluso cambiarlas.
- Para leer:
```python
import os 
api_key = os.environ["API_KEY"]
api_key = os.environ.get("API_KEY") # mejor
```

- Para modificar:
```python
import os 
os.environ["API_KEY"] = “YOUR_API_KEY”
```

---
# Ejercicio
- Crea una variable de entorno en la terminal.
- Escribe un programa que lea esa variable y la muestre por pantalla.


