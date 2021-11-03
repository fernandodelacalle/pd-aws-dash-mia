---
marp: true
theme: default
paginate: true

---

#  Ejercicio: Dockerizando nuestro Dash.

---

# Ejercicio 
- Vamos a dockerizar nuestro dashboard, para ello seguiremos los siguientes pasos.
1. Crea un repo en github (lo usaremos posteriormente).
2. Añade todo el código. Usa la misma estructura que para el ejemplo: ejemplo_docker_3 de carpeta 1_docker de la parte 2.
---
3. Añade las siguientes librerías al requeriments.txt
```
dash
pandas
requests
```
4. Modifica la forma en la que ejecutamos el dash:
```python
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=False, port=8080)
```
---
5. Modifica el comando del dockerfile para que ejecute dash de la siguiente manera:
```Dockerfile
CMD ["python", "app.py"]
```
6. Añade todos estos cambios a tu repo.

7. Prueba a ejecutar la aplicación con:
```bash
docker build -t my_dash .
docker run -p 8080:8080 my_dash 
```