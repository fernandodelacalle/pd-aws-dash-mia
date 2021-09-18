---
marp: true
theme: default
paginate: true
class: invert
---

# Introducción a las API con FastAPI.

--- 
## API

--- 

## FastAPI

- Un framework para crear APIs REST
- Representational state transfer (REST) es una arquitectura usada para crear servicios web

--- 

**FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.**
---

- Rápida: Alto rendimiento, a la par de NodeJS y Go.
- Muy rápida de implementar.
- Con menos posibilidad de errores.
- Fácil de usar.
- Robusta. Lista para ser usada en producción.
- Documentación interactiva.

---

# Instalación

```bash
pip install fastapi
```

---

# Ejemplo

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "FastAPI"}
```

---

Para ejecutar usaremos el servidor ASGI uvicorn con el siguiente comando:

```bash
uvicorn main:app --reload
```

Si con un navegador entramos en  http://localhost:8000/ 
veremos el mensaje {"Hello":"FastAPI"}.

---

- FastAPI nos da una documentación interactiva, puedes verla en:
    - http://localhost:8000/docs para documentación Swagger.
    - http://localhost:8080/redoc para redoc.

---
# Operaciones

- Los métodos HTTP que soporta FastAPI son:
    - POST
    - GET
    - PUT
    - DELETE
    - OPTIONS
    - HEAD
    - PATCH
    - TRACE
---


- Normalmente para construir APIs usamos los métodos específicos de HTTP.
- Normalmente usamos:
    - POST: para creer datos.
    - GET: para leer datos.
    - PUT: para actualizar datos.
    - DELETE: para borrar datos.

---

# Query Parameters


- Cuando declaramos las funciones en FastAPI con parámetros, estos son tratados como parámetros "query".
```python

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_item(user: str):
    return f"hola {user}"
```
- Estas declaraciones están realizadas con Python types, esto permite a FastAPI validarlos.

---

# Ejercicio
- Crea una API usando FastAPI, con un método GET en el path "/echo". Escríbelo en el fichero app.py de la carpeta mi_api.
- Tiene que tener un parámetro name y responder un json:
```json
{"name": "nombre que mandas"}
```





















